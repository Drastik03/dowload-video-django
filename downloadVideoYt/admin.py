from django.contrib import admin
from .models import VideoModel


class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ('download_date',)

admin.site.register(VideoModel, VideoAdmin)
