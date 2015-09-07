from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        fields = ("body", "created", "id", "modified", "slug", "tags", "title",)
        model = Post
