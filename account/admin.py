from django.contrib import admin

from account.models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display =('username','nom','prenom','email','is_active', 'token')