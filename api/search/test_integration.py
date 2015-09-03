from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase


class SearchTestCase(APITestCase):
    """
    """

    def test_get_ok(self):
        """200"""

        response = self.client.get(reverse("api:search-list") + "?q=test")
        self.assertEqual(response.status_code, 200)
