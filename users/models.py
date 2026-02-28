from django.db import models

from datetime import datetime
class User(models.Model):
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False, unique=True)
    login_date = models.DateTimeField(default=datetime.now())
    birthday = models.DateField()
    email = models.CharField(max_length=100, blank=False, unique=True)

    class Meta:
        db_table = 'users'
        managed = False