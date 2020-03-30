#!/usr/bin/python

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        

        self.browser.get('http://localhost:8000')

        #Check page title and header mention To-Do
        self.assertIn('To-Do', self.browser.title)

        self.fail('Finish the test!')

        #Enter a to-do item straight away

        #Type "Buy peacock feathers" into a text box
        
        #Hit enter, page update, page lists
        #"1. Buy peacock feathers" as an item in a to-do list

        #Still a text box inviting to add another item
        # Enter "Use peacock feathers to make a fly"

        #Hit enter, page update page lists both items

        #Unique URL generated

        #Visit URL, to-do list is there and same

        self.browser.quit()

if __name__ == "__main__":
    unittest.main(warnings='ignore')
