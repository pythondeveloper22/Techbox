from django.contrib import admin
from .models import Employee, Item, ItemAssigment

@admin.register(Employee)
class EmployeeRegister(admin.ModelAdmin):
    list_display = ['name', 'designation', 'email', 'mobile']

@admin.register(Item)
class ItemRegister(admin.ModelAdmin):
    list_display = ['name', 'status']

@admin.register(ItemAssigment)
class ItemAssignmentRegister(admin.ModelAdmin):
    list_display = ['name', 'get_item']

