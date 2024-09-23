from django.contrib import admin
from .models import FacultyDetail, StudentDetail, Notes

# Register your models here.

@admin.register(StudentDetail)
class StudentDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'name', 'enrollment_number', 'roll_number',
        'python_t1', 'python_t2', 'python_t3', 'python_t4',
        'full_stack_development_t1', 'full_stack_development_t2',
        'full_stack_development_t3', 'full_stack_development_t4',
        'discrete_mathematics_t1', 'discrete_mathematics_t2',
        'discrete_mathematics_t3', 'discrete_mathematics_t4',
        'theory_of_computation_t1', 'theory_of_computation_t2',
        'theory_of_computation_t3', 'theory_of_computation_t4',
        'computer_organization_and_architecture_t1', 
        'computer_organization_and_architecture_t2',
        'computer_organization_and_architecture_t3', 
        'computer_organization_and_architecture_t4',
        'attendance'
    )
    search_fields = ('name', 'roll_number', 'enrollment_number')
    list_filter = ('user',)
    ordering = ('name', 'roll_number')

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing record
            return ('user',)  # Make the 'user' field read-only
        return super().get_readonly_fields(request, obj)
    
@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ['title']

class FacultyDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'faculty_id', 'subject', 'number', 'short_name')  # Fields to display in the admin list view
    search_fields = ('name', 'faculty_id')  # Fields to search by

admin.site.register(FacultyDetail, FacultyDetailsAdmin)
