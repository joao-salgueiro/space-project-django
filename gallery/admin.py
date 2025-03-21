from django.contrib import admin

from gallery.models import Photograph

class ListPhotographs(admin.ModelAdmin):
    list_display = ("id", "name", "subtitle", "description", "publicated")
    list_display_links = ("id", "name")
    search_fields = ["id", "name"]
    list_filter = ("category",)
    list_editable = ("publicated",)
    list_per_page = 10
    
admin.site.register(Photograph, ListPhotographs)