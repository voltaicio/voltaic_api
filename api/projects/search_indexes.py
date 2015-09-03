from haystack import indexes

from .models import Project


class ProjectIndex(indexes.SearchIndex, indexes.Indexable):
    """
    """

    description = indexes.CharField(model_attr="description")
    model_type = indexes.CharField(model_attr="get_model_type")
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr="title")

    def get_model(self):
        return Project

    def index_queryset(self, using=None):
        """
        Used when the entire index for the model is updated.
        """

        return self.get_model().objects.filter(is_active=True)
