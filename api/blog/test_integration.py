from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase

from .factories import PostFactory


class PostVIewSetTestCase(APITestCase):
    """
    Tests the /posts/ endpoints.
    """

    def test_get_detail_not_found(self):
        """404"""

        response = self.client.get(reverse("api:post-detail", kwargs={"pk": 0}))
        self.assertEqual(response.status_code, 404)

    def test_get_detail_ok(self):
        """200"""

        o = PostFactory.create(is_active=True)
        response = self.client.get(
            reverse("api:post-detail", kwargs={"pk": o.id}))
        self.assertEqual(response.status_code, 200)

    def test_get_list_ok(self):
        """200"""

        response = self.client.get(reverse("api:post-list"))
        self.assertEqual(response.status_code, 200)
