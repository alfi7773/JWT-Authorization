from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from users.manages import MyUserManager



class MyUser(AbstractBaseUser, PermissionsMixin):
    
    class Meta:
        verbose_name_plural = 'пользователи'
        verbose_name = 'пользователь'
        
    username = models.CharField(max_length=40, blank=True, null=True)
    email = models.EmailField('электронная почта', unique=True)
    
    
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    
    USERNAME_FIELD =  'email'
    REQUIRED_FIELDS = ['username',]  
    
    
    objects = MyUserManager()
    
    
    def __str__(self):
        return self.email
    
    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True





# Create your models here.
