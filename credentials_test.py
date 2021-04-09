import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
      '''
      class that defines TestCredentials' test cases

      Args:
      unittest.TestCase: aids in creating new testcases.
      '''

      def setUp(self):
        '''
        runs before every test case
        '''

        self.new_credentials = Credentials("Instagram","Burence", "Br1")

      def test_init(self):
        '''
        test for testing proper object initialization
        '''

        self.assertEqual(self.new_credentials.app_name, "Instagram")
        self.assertEqual(self.new_credentials.acc_username, "Burence")
        self.assertEqual(self.new_credentials.acc_password, "Br1")

      def tearDown(self):
        '''
        test case to clear credentials list after every test has run
        '''
        Credentials.credentials_list = []

      def test_add_mutliple_credentials(self):
        '''
        test case for add credentials logic
        '''
        self.new_credentials.add_credentials()
        test_credentials = Credentials ("Twitter", "Moringa", "123r")
        test_credentials.add_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
      
if __name__ == '__main__':
    unittest.main()
