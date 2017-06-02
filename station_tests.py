from flask import Flask
import application
import unittest
import models as db
import create_user

# from flask_testing import TestCase

class StationTestCase(unittest.TestCase):

    def setUp(self):
        application.application.config['TESTING'] = True
        self.application = application.application.test_client()
        create_user.create_user('station_test', 'test_secret', 1)
    def tearDown(self):
        db.deleteUser('station_test')

    # Find voter helper function
    def find_voter(self, firstname, postcode):
        return self.application.post('/', data=dict(
            firstname=firstname,
            postcode=postcode
        ), follow_redirects=True)

    # Login poll clerk helper function
    def login(self):
        self.application.post('/login', data=dict(
            username='station_test',
            password='test_secret'
        ))

    def test_home_status_code_not_logged_in(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.application.get('/')

        # assert the status code of the response for redirection
        self.assertEqual(result.status_code, 302)

    def test_home_status_code_logged_in(self):
        self.login()
        result = self.application.get('/')

        # assert the status code of the response for redirection
        self.assertEqual(result.status_code, 200)

    # Tests that it asks for a first name
    def test_firstname_field_loaded(self):
        self.login()
        result = self.application.get('/')
        assert b'First name(s)' in result.data

    # Tests that it asks for a postcode
    def test_postcode_field_loaded(self):
        self.login()
        result = self.application.get('/')
        assert b'Postcode' in result.data

if __name__ == '__main__':
    unittest.main()
