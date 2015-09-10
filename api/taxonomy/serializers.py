from rest_framework import serializers

from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        fields = (
            "created", "id", "modified", "slug", "title",)
        model = Tag
