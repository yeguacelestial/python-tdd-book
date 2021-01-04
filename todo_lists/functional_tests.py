import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        """
            - Special method. This runs before each test.
        """
        self.browser = webdriver.Firefox()


    def tearDown(self):
        """
            - Special method. This runs AFTER each test, even if it fails.
        """
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        """
            - Test are organised into classes, which inherit from unittest.TestCase
            - Nice descriptive names for test methods are a good idea.
        """
        # Edith has heard about a cool new online to-do app. She goes to check out its homepage.
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)

        # 'instance.fail' just fails no matter what, producing the given error message.
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box (Edith's hobby is trying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists:
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item. She enters "Use peacock feathers to
        # make a fly" (Edith is very methodical)

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees that the site has
        # generated a unique URL for her -- there is some explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisified, she goes back to sleep.


if __name__ == '__main__':
    unittest.main(warnings='ignore')