from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import AbstractBase


class Post(AbstractBase):
    """
    """

    body = models.TextField(_("body"))

    def __str__(self):
        return self.title