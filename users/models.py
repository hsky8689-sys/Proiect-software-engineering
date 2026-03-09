from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from datetime import datetime

class CustomUserManager(BaseUserManager):
    def create_user(self,username,email,password=None,**extra_fields):
        if not  username:
            raise ValueError('Trebuie username!')
        if not email:
            raise ValueError('Trebuie email')
        email = self.normalize_email(email)
        user = self.model(username=username,email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)
    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD:username})
class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=100, blank=False, unique=True)
    login_date = models.DateTimeField(default=datetime.now)
    email = models.CharField(max_length=100, blank=False, unique=True)
    birthday = models.DateField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    class Meta:
        db_table = 'users'
        #managed = False

class UserProfileSection(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='users/profiles/%Y/%m/%d/',
        blank=True,
        null=True,
        default='users/profile_pictures/sbcf-default-avatar.png'
    )
    background_picture = models.ImageField(
        upload_to='users/background_pictures/%Y/%m/%d/',
        blank=True,
        null=True,
        default='users/background_pictures/sbcf-default-backgrounds.png'
    )
    name = models.CharField(max_length=100,blank=False)
    content = models.CharField(max_length=500,blank=False)
    hidden = models.BooleanField(default=False)
    class Meta:
        db_table = 'profile_sections'