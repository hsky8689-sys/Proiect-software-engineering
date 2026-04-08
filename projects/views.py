from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

import users.views
from projects.models import Project, UserProjectRole, ProjectDomain, ProjectRole, UserProjectRoleManager


@login_required
def create_project(request):
    if request.method == 'POST':

        users.views.acces_profile(request,request.user.username)
    else:
        return JsonResponse({'status': 'error',
                      'code' : 404
                      })
@login_required
def open_project_page(request,name):
    project = Project.objects.filter(name=name).first()
    if not project:
        return JsonResponse({'status': 'failed', 'code': 404})
    staff = UserProjectRole.objects.get_all_users_in_project(project)
    user_role = UserProjectRole.objects.get_user_role_in_project(project, request.user)
    visitor_permissions = UserProjectRole.objects.get_role_permissions(user_role,project)
    project_domains = ProjectDomain.objects.get_project_domains(project)
    context_data = {
        'role': user_role,
        'user_id': request.user.id,
        'user_username': request.user.username,
        'project_name': project.name,
        'project_id': project.id,
        'staff': staff,
        'roles': list(staff.keys()),
        'domains':list(project_domains),
        'description':project.description,
        'visitor_permissions':visitor_permissions
    }
    return render(request, 'html/project_page.html', {'stats': context_data})
@login_required
def open_project_members_page(request,name):
    project = Project.objects.filter(name=name).first()
    result = UserProjectRole.objects.get_all_users_in_project(project)
    stats = {'members': result, 'project_name': project.name}
    return render(request, 'html/project_members_page.html', {'stats': stats})

@login_required
@csrf_exempt
def open_project_settings(request,name):
    project = get_object_or_404(Project,name=name)
    project_role = UserProjectRole.objects.get_user_role_in_project(project=project,user=request.user)
    permissions = UserProjectRole.objects.get_role_permissions(role_name=project_role,project=project)
    if permissions['can_change_project_settings']:
        return render(request,'html/project_settings_page.html',{'user':request.user,'permisions':permissions})
    return JsonResponse({'status': 'error',
                         'code': 404
                         })
@login_required
def send_project_join_request(request,project):
    pass
