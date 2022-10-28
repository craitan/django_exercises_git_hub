from django.contrib import admin

from music_app_django.web.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass