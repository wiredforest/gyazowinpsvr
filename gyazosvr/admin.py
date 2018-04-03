from django.contrib import admin
from gyazosvr import models


@admin.register(models.ScreenShotUploadLog)
class ScreenShotUploadLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_on')
    # list_display_links = ('id', 'uploaded_on')
    list_filter = ('uploaded_on',)
    # search_fields = ('kanji', 'yomi', 'slug',)
    ordering = ('-id',)


@admin.register(models.ScreenShotResource)
class ScreenShotResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'file')
    ordering = ('-id',)


@admin.register(models.ScreenShotRemoveEvent)
class ScreenShotRemoveEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'deleted_on')
    ordering = ('-id',)
