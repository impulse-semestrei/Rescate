from django.test import TestCase

# Create your tests here.


###### TEST US-14 ###############
class Tests(TestCase):
    def test_login(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)


###### TEST US-14 ###############

