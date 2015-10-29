from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_item_in_application_list(self, row_text):
        appList = self.browser.find_element_by_id('application_list')
        items = appList.find_elements_by_tag_name('li')
        self.assertIn(row_text, [item.text for item in items])

    def test_can_start_an_application_and_retrieve_it_later(self):
        # Adeline wakes up in the middle of the night and starts worrrying
        # about her job search, she isn't tied down and plans on applying to a
        # lot of different cities throughout the country. She hears about this
        # new application and figures even if it is a minimum viable
        # application it would still be usefulself.
        self.browser.get(self.live_server_url)
        self.browser.implicitly_wait(3)

        # She notices the page title and header properly mention the name of
        # the site.
        self.assertIn('Job Track', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h3').text
        self.assertIn('Applications', header_text)

        # She is invited by an application item straight away.
        inputbox = self.browser.find_element_by_id('company_name')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Google'
        )

        # She types "Meridian" into the company name of the application.
        inputbox.send_keys('Meridian')

        # She types "Python Developer" into the position name.

        # She types "Portland, OR" into the location.

        # She gives it a "10" on a scale for enthusiasm.

        # She gives it a "10" on a scale for location.

        # She copies the url for the job description and places it in the url
        # form.

        # When she presses enter the page updates, and now the page lists:
        # 1. Meridian - Python Developer
        inputbox.send_keys(Keys.ENTER)
        adeline_list_url = self.browser.current_url
        ## Use assertRegex to check REST URLs
        self.assertRegex(adeline_list_url, '/applications/.+')
        self.check_for_item_in_application_list('1: Meridian')

        # There is still a form for a new application inviting her to add more.
        # She types "Facebook" into the company name of the application.
        inputbox = self.browser.find_element_by_id('company_name')
        inputbox.send_keys('Facebook')
        inputbox.send_keys(Keys.ENTER)

        # She types "React Developer" into the position name.

        # She types "Seattle, WA" into the location.

        # She gives it a "7" on a scale for enthusiasm.

        # She gives it a "7" on a scale for location.

        # She copies the url for the job description and places it in the url
        # form.

        # The page updates again, and now shows both items on her list.
        self.check_for_item_in_application_list('1: Meridian')
        self.check_for_item_in_application_list('2: Facebook')

        # Now a new user, Francis, comes along to the site.

        ## We use a new browser session to make sure that no information
        # of Adeline's is coming through from cookies.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis vists the home page. There is no sign of Adeline's list.
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Meridian', page_text)
        self.assertNotIn('Facebook', page_text)

        # Francis starts a new list by entering a new application.
        inputbox = self.browser.find_element_by_id('company_name')
        inputbox.send_keys('Google')
        inputbox.send_keys(Keys.ENTER)

        # Francis gets his own unqiue URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/applications/.+')
        self.assertNotEqual(francis_list_url, adeline_list_url)

        # Again, there is no trace of Adeline's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Meridian', page_text)
        self.assertNotIn('Facebook', page_text)

        # Satisfied, they both go back to sleep.

    def test_layout_and_styling(self):
        # Adeline goes to the home page.
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered.
        inputbox = self.browser.find_element_by_id('company_name')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )

        # She starts a new list and notices the input is nicely centered there
        # as well.
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('company_name')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )
