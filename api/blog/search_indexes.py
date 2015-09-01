from haystack import indexes

from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    """
    """

    body = indexes.CharField(model_attr="body")
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr="title")

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        """
        Used when the entire index for the model is updated.
        """
        return self.get_model().objects.filter(is_active=True)
