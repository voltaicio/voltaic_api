from drf_haystack.viewsets import HaystackViewSet

from .serializers import SearchSerializer


class SearchView(HaystackViewSet):
    """
    """

    serializer_class = SearchSerializer
