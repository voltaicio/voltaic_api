from drf_haystack.serializers import HaystackSerializer

from blog.search_indexes import PostIndex


class SearchSerializer(HaystackSerializer):
    """
    """

    class Meta:
        index_classes = [PostIndex]
        fields = ["body", "title"]
