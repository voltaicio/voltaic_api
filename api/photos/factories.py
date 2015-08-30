import factory
from factory import fuzzy

from django.utils.lorem_ipsum import COMMON_P

from .models import Photo


class PhotoFactory(factory.DjangoModelFactory):
    """
    A factory class for Projects.
    """

    description = COMMON_P
    image = factory.django.ImageField()
    is_active = fuzzy.FuzzyChoice([False, True])
    title = factory.Sequence(lambda n: "photo-title-{0}".format(n))

    class Meta:
        model = Photo

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        """
        Populates the 'tags' M2M model field.
        """

        if create and extracted:
            for tag in extracted:
                self.tags.add(tag)
