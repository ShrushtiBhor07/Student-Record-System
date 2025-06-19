from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age')
    search_fields = ('name', 'email')
    list_filter = ('age',)

admin.site.register(Student, StudentAdmin)
