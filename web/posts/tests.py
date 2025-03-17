from django.test import TestCase

from .models import Post

class PostTestCase(TestCase):
    
    def test_failure(self):
        self.assertTrue(False)
    
    