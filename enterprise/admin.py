from django.contrib import admin
from .models import Industry, Enterprise, UserEnterprise, Department, Employee, Project, Task

@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# @admin.register(Enterprise)
# class EnterpriseAdmin(admin.ModelAdmin):
#     list_display = ('name', 'address', 'city', 'country', 'website', 'industry', 'master_group')
#     search_fields = ('name', 'city', 'country', 'industry__name')
#     list_filter = ('industry', 'country')
#     ordering = ('name',)
#     autocomplete_fields = ('industry', 'master_group')


# @admin.register(UserEnterprise)
# class UserEnterpriseAdmin(admin.ModelAdmin):
#     list_display = ('user', 'enterprise')
#     search_fields = ('user__username', 'enterprise__name')
#     autocomplete_fields = ('user', 'enterprise')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'position')
    search_fields = ('user__username', 'department__name', 'position')
    list_filter = ('department',)
    autocomplete_fields = ('user', 'department')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    search_fields = ('name', 'description')
    list_filter = ('start_date', 'end_date')
    ordering = ('name',)
    filter_horizontal = ('employees',)
    autocomplete_fields = ('employees',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'assigned_to', 'due_date', 'completed')
    search_fields = ('name', 'project__name', 'assigned_to__user__username')
    list_filter = ('completed', 'due_date')
    autocomplete_fields = ('project', 'assigned_to')
    ordering = ('due_date',)
