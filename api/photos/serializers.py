from rest_framework import serializers

from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        fields = (
            "created", "description", "id", "image", "modified", "slug", "tags",
            "title",)
        model = Photo
