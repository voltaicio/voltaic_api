from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from model_utils.fields import AutoCreatedField, AutoLastModifiedField


class Activatable(models.Model):
    """
    """

    is_active = models.BooleanField(
        _("is active"),
        default=False)

    class Meta:
        abstract = True


class Creatable(models.Model):
    """
    """

    created = AutoCreatedField(
        _("created"))

    class Meta:
        abstract = True


class Modifiable(models.Model):
    """
    """

    modified = AutoLastModifiedField(
        _("modified"))

    class Meta:
        abstract = True


class Sluggable(models.Model):
    """
    """

    slug = models.SlugField(
        _("slug"),
        unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Creates the slug when the model is saved for the first time.
        """

        if not self.id:
            self.slug = slugify(self.title)

        super(Sluggable, self).save(*args, **kwargs)


class Taggable(models.Model):
    """
    """

    tags = models.ManyToManyField(
        "taxonomy.Tag",
        blank=True,
        verbose_name=_("tags"))

    class Meta:
        abstract = True


class Titleable(models.Model):
    """
    """

    title = models.CharField(
        _("title"),
        max_length=128)

    class Meta:
        abstract = True


class AbstractBase(
        Activatable,
        Creatable,
        Modifiable,
        Sluggable,
        Taggable,
        Titleable):
    """
    """

    class Meta:
        abstract = True

    def get_model_type(self):
        return self._meta.verbose_name
