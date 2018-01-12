from django.test import TestCase


class IndexViewTests(TestCase):
    def test_get(self):
        c = self.client.get('/')
        self.assertEqual(c.status_code, 200)
        self.assertNotEqual(c.content, '')


class UploadViewTests(TestCase):
    def test_get(self):
        c = self.client.get('/up/')
        self.assertEqual(c.status_code, 400)
        self.assertNotEqual(c.content, '')
