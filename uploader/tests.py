from django.test import TestCase
from django.urls import reverse


class ViewsTest(TestCase):

    def test_expected_index_view(self):
        response = self.client.get(reverse('uploader:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'uploader/index.html')
