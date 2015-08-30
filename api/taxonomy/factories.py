import factory

from .models import Tag


class TagFactory(factory.DjangoModelFactory):
    """
    A factory class for Tags.
    """

    title = factory.Sequence(lambda n: "tag-title-{0}".format(n))

    class Meta:
        model = Tag
