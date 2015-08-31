from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    """
    An admin class for Posts.
    """

    fieldsets = (
        (None, {
            "fields": ("title", "body", "is_active", "tags",)
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

    class Media:
        js = [
            "/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js",
            "/static/grappelli/tinymce_setup/tinymce_setup.js"]


admin.site.register(Post, PostAdmin)
