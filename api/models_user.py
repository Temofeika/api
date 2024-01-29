# cython:language_level=3
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,AbstractBaseUser,PermissionsMixin
)
from .models_work import *


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(username=username,
        )
 
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, username, password):
        user = self.create_user(username,
            password=password,
            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Имя пользователя', 
                                unique=True,
                                max_length=50)
    
    rid = models.CharField(verbose_name='TeamDesk ID', max_length=16)
    uuid = models.CharField(verbose_name='uuid', max_length=60)
    autoLogin = models.BooleanField(verbose_name='autoLogin', default=True)
    rtype = models.CharField(verbose_name='rtype', max_length=20)
    deviceInfo = models.TextField(verbose_name='Данные для входа:', blank=True)
    
    is_active = models.BooleanField(verbose_name='Активировать сейчас', default=True)
    is_admin = models.BooleanField(verbose_name='Это администратор?', default=False)

    objects = MyUserManager()
 
    USERNAME_FIELD = 'username'  # 用作用户名的字段
    REQUIRED_FIELDS = ['password']     #必须填写的字段
    
    
    def get_full_name(self):
        # The user is identified by their email address
        return self.username
 
    def get_short_name(self):
        # The user is identified by their email address
        return self.username
 
    def __str__(self):              # __unicode__ on Python 2
        return self.username
 
    def has_perm(self, perm, obj=None):    #有没有指定的权限
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
 
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
        


    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff 
        return self.is_admin

    class Meta:
    
        verbose_name = "Пользователь"
        verbose_name_plural = "Список пользователей"
        permissions = (
            ("view_task", "Can see available tasks"),
            ("change_task_status", "Can change the status of tasks"),
            ("close_task", "Can remove a task by setting its status as closed"),
        )

