from django.contrib import admin

from account.models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display =('username','first_name','last_name','email','password','is_active', 'token')