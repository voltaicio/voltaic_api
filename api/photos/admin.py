from django.contrib import admin

from .models import Photo
from utils.admin import WYSIWYG


class PhotoAdmin(WYSIWYG, admin.ModelAdmin):
    """
    An admin class for Photos.
    """

    fieldsets = (
        (None, {
            "fields": ("title", "image", "description", "is_active", "tags",)
        }),
        ("Meta", {
            "classes": ("grp-collapse grp-closed",),
            "fields": ("created", "id", "modified", "slug",)
        })
    )
    list_display = ("id", "title", "description", "is_active", "created",)
    list_filter = ("is_active", "tags",)
    readonly_fields = ("created", "id", "modified", "slug",)
    search_fiels = ("title", "description",)


admin.site.register(Photo, PhotoAdmin)
