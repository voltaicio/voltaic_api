from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import AbstractBase


class Project(AbstractBase):
    """
    """

    description = models.TextField(_("description"))

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
