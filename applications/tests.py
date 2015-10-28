from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from applications.views import home_page
from applications.models import Application, AppList


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)


class ListAndApplicationModelTest(TestCase):

    def test_saving_and_retrieving_applications(self):
        appList = AppList()
        appList.save()

        first_application = Application()
        first_application.company = 'The first (ever) application'
        first_application.app_list = appList
        first_application.save()

        second_application = Application()
        second_application.company = 'The second application'
        second_application.app_list = appList
        second_application.save()

        saved_app_list = AppList.objects.first()
        self.assertEqual(saved_app_list, appList)

        saved_applications = Application.objects.all()
        self.assertEqual(saved_applications.count(), 2)

        first_saved_application = saved_applications[0]
        second_saved_application = saved_applications[1]
        self.assertEqual(first_saved_application.company,
                         'The first (ever) application')
        self.assertEqual(first_saved_application.app_list, appList)
        self.assertEqual(second_saved_application.company,
                         'The second application')
        self.assertEqual(second_saved_application.app_list, appList)


class ApplicationViewTest(TestCase):

    def test_uses_application_template(self):
        response = self.client.get('/applications/the-only-applications-in-the-world/')  # noqa
        self.assertTemplateUsed(response, 'applications.html')

    def test_displays_all_applications(self):
        # Create an appList to hold all of the applications.
        appList = AppList.objects.create()
        # Create an object
        Application.objects.create(company='appy 1', app_list=appList)
        Application.objects.create(company='appy 2', app_list=appList)

        # Pass our request through the home_page
        response = self.client.get('/applications/the-only-applications-in-the-world/')  # noqa
        # Confirm the first object is in the decoded content of the response.
        self.assertContains(response, 'appy 1')
        self.assertContains(response, 'appy 2')


class NewApplicationTest(TestCase):

    def test_saving_a_POST_request(self):
        self.client.post(
            '/applications/new',
            data={'application_company': 'A new application'}
        )

        self.assertEqual(Application.objects.count(), 1)
        new_application = Application.objects.first()
        self.assertEqual(new_application.company, 'A new application')

    def test_redirects_after_POST(self):
        response = self.client.post(
            '/applications/new',
            data={'application_company': 'A new application'}
        )

        self.assertRedirects(response,
                            '/applications/the-only-applications-in-the-world/')
