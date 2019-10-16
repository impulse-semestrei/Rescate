from django.test import TestCase

# Create your tests here.


###### TEST US-14 ###############
class Tests(TestCase):
    def test_login(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)

    def test_google(self):
        response = self.client.get('/auth/google/login/google-oauth2/')
        self.assertEqual(response.status_code, 302)
###### TEST US-14 ###############
