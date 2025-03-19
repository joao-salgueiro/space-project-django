from django.contrib import admin

from gallery.models import Photograph

class ListPhotographs(admin.ModelAdmin):
    list_display = ("id", "name", "subtitle", "description")
    list_display_links = ("id", "name")
    search_fields = ("id", "name")
admin.site.register(Photograph, ListPhotographs)
