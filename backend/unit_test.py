import unittest
from app import add, subtract
from flask import Flask

class TestEndPoints(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)

    def test_add(self):
        # Specify the method and the data to be sent to the add endpoint
        with self.app.test_request_context('/add', method='POST', data={'first_num': '5', 'second_num': '3'}):

            # Calls the add function
            response = add()

            # Get the result and code from the response
            result = response[0].get_json()['result']
            code = response[0].get_json()['code']

            # Check if the result and code are correct
            self.assertEqual(result, 8)
            self.assertEqual(code, 200)


    def test_subtract(self):
        # Specify the method and the data to be sent to the subtract endpoint
        with self.app.test_request_context('/subtract', method='POST', data={'first_num': '5', 'second_num': '3'}):

            # Calls the subtract function
            response = subtract()

            # Get the result and code from the response
            result = response[0].get_json()['result']
            code = response[0].get_json()['code']

            # Check if the result and code are correct
            self.assertEqual(result, 2)
            self.assertEqual(code, 200)

if __name__ == '__main__':
    unittest.main()