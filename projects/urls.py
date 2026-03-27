from django.urls import path

from projects.views import open_project_page

app_name = 'projects'

urlpatterns = [
    path("project-page/<str:name>/",open_project_page,name="project-page"),
]


