from haystack import indexes

from .models import Photo


class PhotoIndex(indexes.SearchIndex, indexes.Indexable):
    """
    """

    description = indexes.CharField(model_attr="description")
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr="title")

    def get_model(self):
        return Photo

    def index_queryset(self, using=None):
        """
        Used when the entire index for the model is updated.
        """

        return self.get_model().objects.filter(is_active=True)
