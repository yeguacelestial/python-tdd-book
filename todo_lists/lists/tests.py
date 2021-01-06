from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string


# Custom
from lists.views import home_page


class HomePageTest(TestCase):

    
    def test_home_page_returns_correct_html(self):

        # Instead of manually creating an HttpRequest object and calling the view function directly,
        # we call self.client.get, passing it the URL we want to test.
        response = self.client.get('/')

        # This lets us check what template was used to render a response
        # NOTE: Only works for responses retrieved by test client
        self.assertTemplateUsed(response, 'home.html')