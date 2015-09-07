from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        fields = (
            "created", "description", "id", "modified", "slug", "tags",
            "title",)
        model = Project
