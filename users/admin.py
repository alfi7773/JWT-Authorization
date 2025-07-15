from django.contrib import admin
from users.models import *
from django.utils.safestring import mark_safe


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ( 'email', 'password')



    