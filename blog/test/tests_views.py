from django.test import TestCase

from django.contrib.auth.models import User
from blog.models import Post

# Create your tests here.
class PostViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        u = User.objects.create(first_name='Angela', last_name='Bob')
        for x in range(20):
            Post.objects.create(title=f'My first post {x}', slug = f'my-first-post-{x}', author=u, content=f'This is my first post content {x}')

    def test_urls(self):
        '''
        Comprobar que el de posts devuelve 20 posts
        ''' 
        # Página Inicial 
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        # Admin
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 302)
        # Primer Post
        p = Post.objects.first()
        slug = p.slug
        response = self.client.get(f'/{slug}/')
        self.assertEquals(response.status_code, 200)