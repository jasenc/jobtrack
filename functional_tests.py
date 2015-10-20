from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Adeline wakes up in the middle of the night and starts worrrying about
		# her job search, she isn't tied down and plans on applying to a lot of
		# different cities throughout the country. She hears about this new
		# application and figures even if it is a minimum viable application it
		# would still be useful.
		self.browser.get('http://localhost:8000')
		self.browser.implicitly_wait(3)

		# She notices the page title and header properly mention the name of the
		# site.
		self.assertIn('Job Track', self.browser.title)
		self.fail("Finish the test!")

		# She is invited by an application item straight away.

		# She types "Meridian" into the company name of the application.

		# She types "Python Developer" into the position name.

		# She types "Portland, OR" into the location.

		# She gives it a "10" on a scale for enthusiasm.

		# She gives it a "10" on a scale for location.

		# She copies the url for the job description and places it in the url form.

		# When she presses enter the page updates, and now the page lists:
		# 1. Meridian - Python Developer

		# There is still a form for a new application inviting her to add more.
		# She types "Facebook" into the company name of the application.

		# She types "React Developer" into the position name.

		# She types "Seattle, WA" into the location.

		# She gives it a "7" on a scale for enthusiasm.

		# She gives it a "7" on a scale for location.

		# She copies the url for the job description and places it in the url form.

		# The page updates again, and now shows both items on her list.

		# Adeline wonders whether the site will remember her list. Then she sees
		# that the site has generated a unique URL for her -- there is some
		# explanatory text to that effect.

		# She visits that URL - her applications are still there.

		# Satisfied, she goes back to sleep

if __name__ == '__main__':
	unittest.main(warnings='ignore')
