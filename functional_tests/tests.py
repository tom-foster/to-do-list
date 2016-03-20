#Created first function test in python.
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(StaticLiveServerTestCase):

        def setUp(self):
            self.browser = webdriver.Firefox()
            self.browser.implicitly_wait(3)

        def tearDown(self):
            self.browser.quit()

        def check_for_row_in_list_table(self, row_text):
            table = self.browser.find_element_by_id('id_list_table')
            rows = table.find_elements_by_tag_name('tr')
            self.assertIn(row_text, [row.text for row in rows])

        def test_can_start_a_list_and_retrieve_it_later(self):
            #Mary has heard about a cool new online to-do app. She goes to check out it's
            #homepage.
            self.browser.get(self.live_server_url)
            #She notices ithe page title and header mention to-do lists
            self.assertIn('To-Do', self.browser.title)
            header_text = self.browser.find_element_by_tag_name('h1').text
            self.assertIn('To-Do', header_text)
            #She is invited to enter a to-do item straight away
            inputbox = self.browser.find_element_by_id('id_new_item')
            self.assertEqual(inputbox.get_attribute('placeholder'),
                             'Enter a to-do item')


            # She types "Buy peacock feathers" into a text box (Mary's hobby is tying
            # fly-fishing lures)
            inputbox.send_keys('Buy peacock feathers')
            #When she hits enter, the page updates, and now the page lists
            #"1: Buy peacock feathers" as an item in a to-do list
            inputbox.send_keys(Keys.ENTER)
            mary_list_url = self.browser.current_url
            self.assertRegex(mary_list_url, '/lists/.+')
            self.check_for_row_in_list_table('1: Buy peacock feathers')
            #There is still a text box inviting her to add another item. She enters
            #"Use peacock feahters to make a fly" (Mary is very methodical)
            inputbox = self.browser.find_element_by_id('id_new_item')
            inputbox.send_keys('Use peacock feathers to make a fly')
            inputbox.send_keys(Keys.ENTER)

            #The page updates again, and now shows both items on her list
            self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
            self.check_for_row_in_list_table('1: Buy peacock feathers')
            #Now a new user, Rachael, comes along to the site.

            ##We use a new browser session to make sure that no information
            ##of Mary's is coming through to cookies etc
            self.browser.quit()
            self.browser = webdriver.Firefox()

            #Rachael vists the home page. There is no sign of Mary's lists.
            self.browser.get(self.live_server_url)
            page_text = self.browser.find_element_by_tag_name('body').text
            self.assertNotIn('Buy peacock feathers', page_text)
            self.assertNotIn('make a fly', page_text)
            #Rachael starts a new list by entering a new item. She is
            #less interesting than Mary...
            inputbox = self.browser.find_element_by_id('id_new_item')
            inputbox.send_keys('Buy milk')
            inputbox.send_keys(Keys.ENTER)
            #Rachael gets her own unique URL
            rachael_list_url = self.browser.current_url
            self.assertRegex(rachael_list_url, '/lists/.+')
            self.assertNotEqual(rachael_list_url, mary_list_url)
            #Again there is no trace of Mary's list.
            page_text = self.browser.find_element_by_tag_name('body').text
            self.assertNotIn('Buy peacock feathers', page_text)
            self.assertIn('Buy milk', page_text)

            #Satisfied, they both go back to sleep

        def test_layout_and_styling(self):
            #Mary goes to the home page
            self.browser.get(self.live_server_url)
            self.browser.set_window_size(1024, 786)

            #She notices the input box is nicely centered
            inputbox = self.browser.find_element_by_id('id_new_item')
            self.assertAlmostEqual(
                inputbox.location['x'] + inputbox.size['width'] / 2,
                512,
                delta=10
            )

            #She starts a new list and sees the input is nicely
            #centered there too
            inputbox.send_keys('testing\n')
            inputbox = self.browser.find_element_by_id('id_new_item')
            self.assertAlmostEqual(
                    inputbox.location['x'] + inputbox.size['width'] / 2,
                    512,
                    delta=10
            )

if __name__ == "__main__":
    unittest.main()
