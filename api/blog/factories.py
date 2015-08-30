import factory
from factory import fuzzy

from django.utils.lorem_ipsum import COMMON_P

from .models import Post


class PostFactory(factory.DjangoModelFactory):
    """
    A factory class for Post.
    """

    body = COMMON_P
    is_active = fuzzy.FuzzyChoice([False, True])
    title = factory.Sequence(lambda n: "post-title-{0}".format(n))

    class Meta:
        model = Post

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        """
        Populates the 'tags' M2M model field.
        """

        if create and extracted:
            for tag in extracted:
                self.tags.add(tag)
