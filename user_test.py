import unittest
from user import Users

class TestingUsers(unittest.TestCase):
      '''
      class that defines Users class test cases
      
      Args:
        unittest.Testcase: aids in creating test cases
      '''
      def setUp(self):
          '''
          method that runs before each test case
          '''
          self.new_user = Users("Burence","1997")

      def test_init(self):
          '''
          test proper object initialization
          '''
          self.assertEqual(self.new_user.username,"Burence")
          self.assertEqual(self.new_user.login_password,"1997")

      def test_add_user(self):
          '''
          test if added user is saved to users_list
          '''

          self.new_user.add_user()
          self.assertEqual(len(Users.users_list),1)

      def tearDown(self):
          '''
          clear user_list after each round of test
          '''

          Users.users_list = []

      def test_add_multiple_users(self):
          '''
          test for posibility of adding many users to user_list
          '''

          self.new_user.add_user()
          test_user = Users("Moringa", "1234")
          test_user.add_user()
          self.assertEqual(len(Users.users_list), 2)

      def test_delete_user(self):
          '''
          test for removing users from users_list
          '''

          self.new_user.add_user()
          test_user = Users("Moringa", "1234")
          test_user.add_user()

          test_user.delete_user()
          self.assertEqual(len(Users.users_list),1)
          
      def test_search_username(self):
          '''
          test finding user via username logic
          '''
          self.new_user.add_user()
          test_user = Users("Moringa", "1234")
          test_user.add_user()

          found_user = Users.search_username("Moringa")
          self.assertEqual(found_user.login_password, test_user.login_password)

      def test_user_exists(self):
          '''
          test if a user exists or not
          '''
          self.new_user.add_user()
          test_user = Users("Moringa", "1234")
          test_user.add_user()

          user_exists = Users.user_exists("Moringa","1234")
          self.assertTrue(user_exists)
            
if __name__ == '__main__':
    unittest.main()