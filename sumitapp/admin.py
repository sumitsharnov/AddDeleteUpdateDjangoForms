from django.contrib import admin

# Register your models here.

from .models import University
from .models import Countries


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['university_name']


@admin.register(Countries)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['country_unique_Id']
