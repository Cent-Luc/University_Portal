from django.contrib import admin
from .models import Course, Unit, Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'code', 'summary']
    prepopulated_fields = {'code': ('title',)}

class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'created']
    list_filter = ['created', 'course']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'code': ('title',)}
    inlines = [ModuleInline]

