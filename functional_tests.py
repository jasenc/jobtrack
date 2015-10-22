from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Adeline wakes up in the middle of the night and starts worrrying
        # about her job search, she isn't tied down and plans on applying to a
        # lot of different cities throughout the country. She hears about this
        # new application and figures even if it is a minimum viable
        # application it would still be usefulself.
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(3)

        # She notices the page title and header properly mention the name of
        # the site.
        self.assertIn('Job Track', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Applications', header_text)

        # She is invited by an application item straight away.
        inputbox = self.browser.find_element_by_id('id_new_application')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter an application'
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

        table = self.browser.find_element_by_id('id_application_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Meridian' for row in rows),
            "New application did not appear in table -- its text was:\n\
            {0}".format(table.text)
        )

        # There is still a form for a new application inviting her to add more.
        # She types "Facebook" into the company name of the application.
        self.fail("Finish the test!")

        # She types "React Developer" into the position name.

        # She types "Seattle, WA" into the location.

        # She gives it a "7" on a scale for enthusiasm.

        # She gives it a "7" on a scale for location.

        # She copies the url for the job description and places it in the url
        # form.

        # The page updates again, and now shows both items on her list.

        # Adeline wonders whether the site will remember her list. Then she
        # sees that the site has generated a unique URL for her -- there is
        # some explanatory text to that effect.

        # She visits that URL - her applications are still there.

        # Satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
