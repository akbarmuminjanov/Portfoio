from django.contrib import admin
from .models import Resume, Languages, Interests
# Register your models here.
class LanguagesInline(admin.TabularInline):
    model = Languages

class InterestsInline(admin.TabularInline):
    model = Interests

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ["full_name"]
    inlines = [LanguagesInline, InterestsInline]