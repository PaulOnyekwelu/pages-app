from django.test import SimpleTestCase
from django.urls import reverse
from http import HTTPStatus


def url_compute(viewname):
    """computes url"""
    return reverse(viewname)


class HomePageTest(SimpleTestCase):
    """test suites for home page"""

    def setUp(self):
        url = url_compute("Home")
        self.response = self.client.get(url)

    def test_homepage_status_ok(self):
        """test homepage return 200 status"""
        self.assertEqual(self.response.status_code, HTTPStatus.OK)

    def test_template_name_correct(self):
        """test that response is with correct html template"""
        self.assertTemplateUsed(self.response, "home.html")

    def test_template_content(self):
        """test template content is correct"""
        self.assertContains(self.response, "<h1>Home Page</h1>")


class AboutPageTest(SimpleTestCase):
    """test suites for the about page"""

    def setUp(self):
        url = url_compute("About")
        self.response = self.client.get(url)

    def test_aboutpage_status_ok(self):
        """test aboutpage return 200 status"""
        self.assertEqual(self.response.status_code, HTTPStatus.OK)

    def test_template_name_correct(self):
        """test that response is with correct html template"""
        self.assertTemplateUsed(self.response, "about.html")

    def test_template_content(self):
        """test template content is correct"""
        self.assertContains(self.response, "<h1>About Page</h1>")
