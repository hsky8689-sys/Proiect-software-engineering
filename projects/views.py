from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

import users.views
from projects.models import Project, UserProjectRole


@login_required
def create_project(request):
    if request.method == 'POST':

        users.views.acces_profile(request,request.user.username)
    else:
        JsonResponse({'status': 'error',
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
    context_data = {
        'role': user_role,
        'user_id': request.user.id,
        'user_username': request.user.username,
        'project_name': project.name,
        'project_id': project.id,
        'staff': staff,
        'roles': list(staff.keys()),
        'visitor_permissions':visitor_permissions
    }

    return render(request, 'html/project_page.html', {'stats': context_data})