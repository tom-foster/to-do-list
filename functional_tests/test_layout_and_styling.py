#Created first function test in python.
from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):

        def test_layout_and_styling(self):
            #Mary goes to the home page
            self.browser.get(self.server_url)
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
