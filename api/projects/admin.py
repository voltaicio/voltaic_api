from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    """
    An admin class for Projects.
    """

    fieldsets = (
        (None, {
            "fields": ("title", "description", "is_active", "tags",)
        }),
        ("Meta", {
            "classes": ("grp-collapse grp-closed",),
            "fields": ("created", "id", "modified", "slug",)
        })
    )
    list_display = ("id", "title", "is_active", "created", "modified",)
    list_filter = ("is_active", "tags",)
    readonly_fields = ("created", "id", "modified", "slug",)
    search_fiels = ("title",)


admin.site.register(Project, ProjectAdmin)
