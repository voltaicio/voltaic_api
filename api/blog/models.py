from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import AbstractBase


class Post(AbstractBase):
    """
    """

    body = models.TextField(_("body"))
    subtitle = models.CharField(_("subtitle"), blank=False, max_length=128)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
