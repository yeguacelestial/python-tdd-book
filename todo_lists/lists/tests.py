from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

# Custom
from lists.views import home_page


class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        # 'resolve' maps the given url, and tries to locate its Django view
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    
    def test_home_page_returns_correct_html(self):
        # This is what Django see when a user asks for a page
        request = HttpRequest()

        response = home_page(request)

        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))

        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))