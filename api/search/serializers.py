from drf_haystack.serializers import HaystackSerializer

from blog.search_indexes import PostIndex
from photos.search_indexes import PhotoIndex
from projects.search_indexes import ProjectIndex


class SearchSerializer(HaystackSerializer):
    """
    """

    class Meta:
        index_classes = [PhotoIndex, PostIndex, ProjectIndex]
        fields = ["body", "description", "id", "model_type", "title"]
