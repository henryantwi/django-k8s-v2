from django.test import TestCase

from .models import Post

class PostTestCase(TestCase):
    
    def setUp(self):
        Post.objects.create(title="Test Post", content="This is a test post.")
    
    
    def test_failure(self):
        qs = Post.objects.all()
        self.assertTrue(qs.exists())
    
    