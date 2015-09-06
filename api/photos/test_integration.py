from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase

from .factories import PhotoFactory


class PhotoViewSetTestCase(APITestCase):
    """
    Tests the /photos/ endpoints.
    """

    def test_get_detail_not_found(self):
        """404"""

        response = self.client.get(
            reverse("api:photo-detail", kwargs={"pk": 0}))
        self.assertEqual(response.status_code, 404)

    def test_get_detail_ok(self):
        """200"""

        o = PhotoFactory.create(is_active=True)
        response = self.client.get(
            reverse("api:photo-detail", kwargs={"pk": o.id}))
        self.assertEqual(response.status_code, 200)

    def test_get_list_ok(self):
        """200"""

        response = self.client.get(reverse("api:photo-list"))
        self.assertEqual(response.status_code, 200)
