from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import AbstractBase


class Photo(AbstractBase):
    """
    """

    description = models.TextField(_("description"))
    image = models.ImageField(_("image"), upload_to="photo_image/")

    def __str__(self):
        return self.title
