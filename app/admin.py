from django.contrib import admin
from django.contrib.admin.filters import ListFilter

# Register your models here.

from django.contrib.auth.admin import UserAdmin

#Models
from app.models import *

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', )
    list_filter = ('is_staff','created', 'modified')

admin.site.register(UserTable, CustomUserAdmin)
admin.site.register(SuitTable)
admin.site.register(ReserveTable)
admin.site.register(InventPackTable)
admin.site.register(CustomerPurchTable)