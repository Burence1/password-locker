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

      def test_display_credentials(self):
        '''
        test case for displaying user's credentials
        '''

        self.assertEqual(Credentials.credentials_list,Credentials.display_credentials())        
      
      def test_credentials_exist(self):
        '''
        test case for confirming credentials that exist
        '''
        self.new_credentials.add_credentials()
        test_credentials = Credentials("Instagram", "Burence","Br1")
        test_credentials.add_credentials()
        
        credential_exist = Credentials.credentials_exist("Instagram")
        self.assertTrue(credential_exist)

      def test_search__app_name(self):
        '''
        test case for searching app by name
        '''
        self.new_credentials.add_credentials()
        test_credentials = Credentials("Instagram", "Burence", "Br1")
        test_credentials.add_credentials()

        found_credentials = Credentials.search_app_name("Instagram")
        self.assertEqual(found_credentials.app_name, test_credentials.app_name)

      def test_delete_credentials(self):
        '''
        test case for delete credentials logic
        '''

        self.new_credentials.add_credentials()
        test_credentials = Credentials("Instagram", "Burence", "Br1")
        test_credentials.add_credentials()

        test_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

if __name__ == '__main__':
    unittest.main()
