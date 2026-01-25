from django.contrib import admin

# Register your models here.
from blog.models import Student

from blog.models import Profile
admin.site.register(Profile)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'enrollment_date', 'city')
    search_fields = ('name', 'email', 'city')
    list_filter = ('city', 'enrollment_date', 'age')
    ordering = ('name',)
