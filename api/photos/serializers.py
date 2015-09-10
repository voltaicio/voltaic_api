from rest_framework import serializers

from .models import Photo
from taxonomy.serializers import TagSerializer


class PhotoSerializer(serializers.ModelSerializer):
    """
    """

    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        fields = (
            "created", "description", "id", "image", "modified", "slug",
            "tags", "title",)
        model = Photo
