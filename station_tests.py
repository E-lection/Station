from flask import Flask
import application
import unittest
import models as db
import create_user

# from flask_testing import TestCase

TEST_USERNAME = 'station_test'
TEST_PASSWORD = 'test_secret'
BAD_LOGIN = 'bad'

class StationTestCase(unittest.TestCase):

    def setUp(self):
        application.application.config['TESTING'] = True
        self.application = application.application.test_client()
        create_user.create_user(TEST_USERNAME, TEST_PASSWORD, 1)
    def tearDown(self):
        db.deleteUser(TEST_USERNAME)

    # Find voter helper function
    def find_voter(self, firstname, postcode):
        return self.application.post('/', data=dict(
            firstname=firstname,
            postcode=postcode
        ), follow_redirects=True)

    # Login poll clerk helper function
    def login(self, username, password):
        return self.application.post('/login', data=dict(
            username=username,
            password=password
        ))

    # Test for error code 302 when you're not logged in
    def test_home_status_code_not_logged_in(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.application.get('/')

        # assert the status code of the response for redirection
        self.assertEqual(result.status_code, 302)

    # Test for success code 200 when you are logged in
    def test_home_status_code_logged_in(self):
        self.login(TEST_USERNAME, TEST_PASSWORD)
        result = self.application.get('/')

        # assert the status code of the response for redirection
        self.assertEqual(result.status_code, 200)

    # Test login screen asks for username and password
    def test_login_username_password(self):
        result = self.application.get('/login')
        assert b'Username' and b'Password' in result.data

    # Test that logging in with an incorrect username
    # and password combination asks you again
    def test_incorrect_login(self):
        result = self.login(BAD_LOGIN, BAD_LOGIN)
        assert b'Login unsuccessful' and b'Username' and b'Password' in result.data

    # Test that logging in with correct credentials
    # takes you to the search voter page
    def test_correct_login(self):
        self.login(TEST_USERNAME, TEST_PASSWORD)
        result = self.application.get('/')
        assert b'First name(s)' and b'Postcode' in result.data

    # Tests that it asks for a first name
    def test_firstname_field_loaded(self):
        self.login(TEST_USERNAME, TEST_PASSWORD)
        result = self.application.get('/')
        assert b'First name(s)' in result.data

    # Tests that it asks for a postcode
    def test_postcode_field_loaded(self):
        self.login(TEST_USERNAME, TEST_PASSWORD)
        result = self.application.get('/')
        assert b'Postcode' in result.data

if __name__ == '__main__':
    unittest.main()
