from django.contrib import admin

# Register your models here.
from  . models import userLogin,userRegister

admin.site.register(userLogin)

admin.site.register(userRegister)
