#Created first function test in python.
from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

        def test_cannot_add_empty_list_items(self):
            #Rachael goes to the home page and accidentally tries to submit
            #an empty list item. She hits Enter on the the empty input box

            #The home page refreshes, and there is an error message saying
            #that list items cannot be blank.

            #She tries again with some text for the item, which now works

            #Perversely, she now decides to submit a second blank list item

            #And she can correct it by filling some text in

            self.fail('write me')

if __name__ == "__main__":
    unittest.main()
