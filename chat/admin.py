from django.contrib import admin
from .models import Message,User
#Register models here
admin.site.register(Message)
admin.site.register(User)