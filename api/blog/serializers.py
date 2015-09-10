from rest_framework import serializers

from .models import Post
from taxonomy.serializers import TagSerializer


class PostSerializer(serializers.ModelSerializer):
    """
    """

    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        fields = (
            "body", "created", "id", "modified", "slug", "tags", "title",)
        model = Post
