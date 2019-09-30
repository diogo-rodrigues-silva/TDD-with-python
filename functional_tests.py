# unzip chromedriver_linux64.zip
# sudo chmod +x chromedriver
# sudo mv chromedriver /usr/bin/
# rm chromedriver_linux64.zip

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Diogo heard about a cool new online to-do app. He goes
        # to check out its homepage
        self.browser.get('http://127.0.0.1:8000')

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!!!')

    # He is invited to enter a to-do item straight away

    # He types "Buy peacock feathers" into a text box (Diogo's hobby
    # is tying fly-fishing lures)

    # When she hits enter, the page updates, and now the page lists
    # "1: Buy peacock feathers" as an item in a to-do list

    # There is still a text box inviting him to add another item. He
    # enter's "Use peacock feathers to make a fly" (Diogo is very methodical)

    # The page updates again, and now shows both items an her list

    # Diogo wonders whethers the site will remember him list. Then he sees
    # that the site has generated a unique URL for him -- there is some
    # explanatory text to that effect

    # He visits that URL - His to-do list is still there.

    # Satisfied, he goes back to sleep
    # browser.quit()


if __name__ == "__main__":
    unittest.main(warnings='ignore')
