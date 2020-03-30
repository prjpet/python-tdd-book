#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
        #Enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        #Type "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')
        #Hit enter, page update, page lists
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1. Buy peacock feathers' for row in rows))
        #"1. Buy peacock feathers" as an item in a to-do list
        
        #Still a text box inviting to add another item
        self.fail('Finish the test!')

        # Enter "Use peacock feathers to make a fly"

        #Hit enter, page update page lists both items

        #Unique URL generated

        #Visit URL, to-do list is there and same

        self.browser.quit()

if __name__ == "__main__":
    unittest.main(warnings='ignore')
