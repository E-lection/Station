from flask import Flask
import application
import unittest

# from flask_testing import TestCase

class StationTestCase(unittest.TestCase):

    def setUp(self):
        application.application.config['TESTING'] = True
        self.application = application.application.test_client()

    def tearDown(self):
        pass

    # Initial test, ensure flask set up correctly
    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.application.get('/')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    # Tests that the station.html page is actually loaded
    # def test_page_render(self):
    #     # sends HTTP GET request to the application
    #     # on the specified path
    #     result = self.application.get('/')
    #     # assert the correct template has been used
    #     self.assert_template_used('station.html')

    # Find voter helper function
    def find_voter(self, firstname, postcode):
        return self.application.post('/', data=dict(
            firstname=firstname,
            postcode=postcode
        ), follow_redirects=True)

    # Tests that it asks for a first name
    def test_firstname_field_loaded(self):
        result = self.application.get('/')
        assert b'First name(s)' in result.data

    # Tests that it asks for a postcode
    def test_postcode_field_loaded(self):
        result = self.application.get('/')
        assert b'Postcode' in result.data

    # # Tests that it throws an error if the name is invalid
    # def test_invalid_name_validation(self):
    #     rv = self.find_voter(
    #         application.application.config['FIRSTNAME'] + '&',
    #         application.application.config['POSTCODE'],
    #     )
    #     assert b'Invalid first name entered' in rv.data
    #
    # # Test that it throws an error if the postcode is invalid
    # def test_invalid_postcode_validation(self):
    #     rv = self.find_voter(
    #         application.application.config['FIRSTNAME'],
    #         application.application.config['POSTCODE'] + '666',
    #     )
    #     assert b'Invalid postcode entered' in rv.data

    # Test that it redirects to the correct page if name
    # and postcode are both valid

if __name__ == '__main__':
    unittest.main()
