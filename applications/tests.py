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
        request.POST['application_text'] = 'A new application'

        response = home_page(request)

        self.assertEqual(Application.objects.count(), 1)
        new_application = Application.objects.first()
        self.assertEqual(new_application.company, 'A new application')

        self.assertIn('A new application', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_application_text': 'A new application'}
        )
        self.assertEqual(response.content.decode(), expected_html)


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
