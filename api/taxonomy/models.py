from utils.models import Creatable, Modifiable, Sluggable, Taggable, Titleable


class Tag(Creatable, Modifiable, Sluggable, Taggable, Titleable):
    """
    """

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
