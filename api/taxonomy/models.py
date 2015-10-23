from utils.models import Creatable, Modifiable, Sluggable, Titleable


class Tag(Creatable, Modifiable, Sluggable, Titleable):
    """
    """

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
