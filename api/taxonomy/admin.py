from django.contrib import admin

from .models import Tag


class TagAdmin(admin.ModelAdmin):
    """
    An admin class for Tags.
    """

    fieldsets = (
        (None, {
            "fields": ("title",)
        }),
        ("Meta", {
            "classes": ("grp-collapse grp-closed",),
            "fields": ("created", "id", "modified", "slug",)
        })
    )
    list_display = ("id", "title", "slug", "created",)
    list_filter = ("tags",)
    readonly_fields = ("created", "id", "modified", "slug",)
    search_fiels = ("title",)


admin.site.register(Tag, TagAdmin)
