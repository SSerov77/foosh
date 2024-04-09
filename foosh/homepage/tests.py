from http import HTTPStatus

from django.test import Client, TestCase


# Create your tests here.
class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)


class CheckContext(TestCase):
    def test_user_in_context(self):
        response = Client().get("/")
        self.assertIn("user", response.context)


__all__ = []
