from django.contrib import admin
from .models import Position,Service,Employee


@admin.register(Position)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['position', 'active', 'modified_date']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service', 'icon', 'active', 'modified_date']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'active', 'modified_date']
