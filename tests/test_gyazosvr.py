import os
from django.conf import settings
from django.test import TestCase, override_settings

TESTS_ROOT = os.path.dirname(__file__)
TEST_MEDIA_ROOT = os.path.join(TESTS_ROOT, 'media_root')
RESOURCE_ROOT = os.path.join(TESTS_ROOT, 'resource')


class IndexViewTests(TestCase):
    def test_get(self):
        c = self.client.get('/')
        self.assertEqual(c.status_code, 200)
        self.assertNotEqual(c.content, '')


class UploadViewTests(TestCase):

    def setUp(self):
        super().setUp()
        try:
            os.makedirs(os.path.join(TEST_MEDIA_ROOT, 'up'))
        except FileExistsError:
            pass

    def tearDown(self):
        super().tearDown()
        up_dir = os.path.join(TEST_MEDIA_ROOT, 'up')
        for p in os.listdir(up_dir):
            os.remove(os.path.join(up_dir, p))

    def test_get(self):
        c = self.client.get('/up/')
        self.assertEqual(c.status_code, 400)
        self.assertNotEqual(c.content, '')

    @override_settings(MEDIA_ROOT=TEST_MEDIA_ROOT)
    def test_post(self):
        with open(os.path.join(RESOURCE_ROOT, 'sample.png'), 'rb') as file:
            data = {
                'id': 'hogehoge',
                'imagedata': file,
            }
            c = self.client.post('/up/', data=data)
            self.assertEqual(c.status_code, 200)
            self.assertNotEqual(c.content, '')

            # アップロードされたファイルの確認
            self.assertTrue(os.path.exists(os.path.join(TEST_MEDIA_ROOT, 'up', 'hogehoge.png')))
