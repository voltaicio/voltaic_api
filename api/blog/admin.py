from django.contrib import admin

from .models import Post
from utils.admin import WYSIWYG


class PostAdmin(WYSIWYG, admin.ModelAdmin):
    """
    An admin class for Posts.
    """

    fieldsets = (
        (None, {
            "fields": ("title", "subtitle", "body", "is_active", "tags",)
        }),
        ("Meta", {
            "classes": ("grp-collapse grp-closed",),
            "fields": ("created", "id", "modified", "slug",)
        })
    )
    list_display = ("id", "title", "subtitle", "is_active", "created", "modified",)
    list_filter = ("is_active", "tags",)
    readonly_fields = ("created", "id", "modified", "slug",)
    search_fiels = ("title",)


admin.site.register(Post, PostAdmin)
