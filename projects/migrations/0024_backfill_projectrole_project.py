from django.db import migrations

DEFAULT_ROLE_NAMES = ['owner', 'admin', 'project_manager', 'developer', 'tester', 'viewer', 'newbie']
PERMISSION_FIELDS = [
    'can_accept_invites', 'can_invite_others', 'can_kick_others', 'can_change_roles',
    'can_create_branches', 'can_modify_branches', 'can_merge_branches', 'can_delete_branches',
    'can_add_tasks', 'can_delete_tasks', 'can_modify_tasks', 'can_modify_files',
    'can_execute_code', 'can_share_file_access', 'can_change_project_settings',
]


def backfill_project_roles(apps, schema_editor):
    Project = apps.get_model('projects', 'Project')
    ProjectRole = apps.get_model('projects', 'ProjectRole')
    UserProjectRole = apps.get_model('projects', 'UserProjectRole')

    # snapshot the current (still-global, shared-by-name) permission values for
    # each default role name before any row below gets claimed/mutated
    canonical = {}
    for row in ProjectRole.objects.filter(project__isnull=True, name__in=DEFAULT_ROLE_NAMES):
        canonical[row.name] = {field: getattr(row, field) for field in PERMISSION_FIELDS}

    for project in Project.objects.all().order_by('id'):
        for role_name, perms in canonical.items():
            existing_membership = UserProjectRole.objects.filter(
                project=project, role__name=role_name
            ).select_related('role').first()

            if existing_membership is None:
                # this project has no members under this default role yet -
                # still give it its own copy so every project ends up with a
                # full set of 7
                ProjectRole.objects.create(project=project, name=role_name, **perms)
                continue

            current_role = existing_membership.role
            if current_role.project_id is None:
                # unclaimed shared row: claim it as-is for this project
                ProjectRole.objects.filter(id=current_role.id).update(project=project)
            elif current_role.project_id != project.id:
                # already claimed by a different project: make our own copy
                # and repoint every member of this project off the old row
                new_role = ProjectRole.objects.create(project=project, name=role_name, **perms)
                UserProjectRole.objects.filter(
                    project=project, role_id=current_role.id
                ).update(role=new_role)
            # else: already correctly scoped to this project - nothing to do

    # any custom (non-default-name) role that's still unscoped: claim it for
    # whichever single project actually uses it, if any
    for role in ProjectRole.objects.filter(project__isnull=True):
        owning_project_id = UserProjectRole.objects.filter(role=role).values_list('project_id', flat=True).first()
        if owning_project_id is not None:
            ProjectRole.objects.filter(id=role.id).update(project_id=owning_project_id)

    # anything still unscoped now is genuinely orphaned (a default role that
    # was never snapshotted, or a custom role nobody uses)
    ProjectRole.objects.filter(project__isnull=True).delete()


def noop_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('projects', '0023_projectrole_project_nullable'),
    ]
    operations = [
        migrations.RunPython(backfill_project_roles, noop_reverse),
    ]
