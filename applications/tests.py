from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from applications.views import home_page
from applications.models import Application


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['application_company'] = 'A new application'

        response = home_page(request)

        self.assertEqual(Application.objects.count(), 1)
        new_application = Application.objects.first()
        self.assertEqual(new_application.company, 'A new application')

    def test_home_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['application_company'] = 'A new application'

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'],
                         '/applications/the-only-applications-in-the-world')

    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Application.objects.count(), 0)

    def test_home_page_displays_all_list_items(self):
        # Create an object
        Application.objects.create(company='appy 1')
        # Create a second object
        Application.objects.create(company='appy 2')

        # Make an HTTP request
        request = HttpRequest()
        # Pass our request through the home_page
        response = home_page(request)
        # Confirm the first object is in the decoded content of the response.
        self.assertIn('appy 1', response.content.decode())
        # Confirm the first object is in the decoded content of the response.
        self.assertIn('appy 2', response.content.decode())


class ApplicationModelTest(TestCase):

    def test_saving_and_retrieving_applications(self):
        first_application = Application()
        first_application.company = 'The first (ever) application'
        first_application.save()

        second_application = Application()
        second_application.company = 'The second application'
        second_application.save()

        saved_applications = Application.objects.all()
        self.assertEqual(saved_applications.count(), 2)

        first_saved_application = saved_applications[0]
        second_saved_application = saved_applications[1]
        self.assertEqual(first_saved_application.company,
                         'The first (ever) application')
        self.assertEqual(second_saved_application.company,
                         'The second application')
