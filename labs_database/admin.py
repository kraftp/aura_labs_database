from django.contrib import admin
from .models import Lab

admin.AdminSite.site_header = 'AURA Labs Database'

# Register your models here.

class LabAdmin(admin.ModelAdmin):
    fields = ('pi_name', 'university')
    list_display = ('pi_name', 'university')
    list_filter = ['university']

admin.site.register(Lab, LabAdmin)
