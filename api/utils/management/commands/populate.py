from random import randint

from django.core.management.base import BaseCommand

from blog.factories import PostFactory
from photos.factories import PhotoFactory
from projects.factories import ProjectFactory
from taxonomy.factories import TagFactory


class Command(BaseCommand):
    """
    """

    help = "Populates the application with dummy data."

    def __init__(self, *args, **kwargs):
        self.tags = []
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **kwargs):
        """
        """

        self._create_tags()
        self._create_photos()
        self._create_posts()
        self._create_projects()

    def _create_photos(self):
        """
        """

        count = randint(5, 10)
        for i in range(count):
            PhotoFactory.create(
                tags=(self.tags[i] for i in range(randint(1, 10))))

        print("Created {0} Photos".format(count))

    def _create_posts(self):
        """
        """

        count = randint(5, 10)
        for i in range(count):
            PostFactory.create(
                tags=(self.tags[i] for i in range(randint(1, 10))))

        print("Created {0} Posts".format(count))

    def _create_projects(self):
        """
        """

        count = randint(5, 10)
        for i in range(count):
            ProjectFactory.create(
                tags=(self.tags[i] for i in range(randint(1, 10))))

        print("Created {0} Projects".format(count))

    def _create_tags(self):
        """
        """

        for i in range(randint(15, 25)):
            self.tags.append(TagFactory.create())

        print("Created {0} Tags".format(len(self.tags)))
