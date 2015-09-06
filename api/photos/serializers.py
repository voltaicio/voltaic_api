from rest_framework import serializers

from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        fields = (
            "created", "modified", "description", "id", "image", "slug", "tags",
            "title",)
        model = Photo
