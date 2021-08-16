from django.contrib import admin

# Register your models here.

class UserAdminConfig(UserAdmin):
    search_fields = ('email','user_name','first_name')
    ordering = ('email','username','first_name','last_name')