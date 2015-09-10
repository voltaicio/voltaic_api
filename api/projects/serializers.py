from rest_framework import serializers

from .models import Project
from taxonomy.serializers import TagSerializer


class ProjectSerializer(serializers.ModelSerializer):
    """
    """

    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        fields = (
            "created", "description", "id", "modified", "slug", "tags",
            "title",)
        model = Project
