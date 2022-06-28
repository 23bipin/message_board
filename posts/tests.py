from django.test import TestCase

from .models import Post


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="this is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "this is a test!")
