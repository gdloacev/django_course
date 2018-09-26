from django.contrib import admin
from .models import Project
from .models import Person

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Project, ProjectAdmin)

class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Person, PersonAdmin)