
class Users:
  '''
  Class that creates new instances of users
  '''
  users_list = []

  def __init__(self,username, password):
      '''
      __init__ method helps create new instances of the class.

      Args:
           username: new username
           login_password: new login_password
      '''
      self.username = username
      self.login_password = login_password
  
  def add_user(self):
      '''
      add new users to users_list
      '''

      Users.users_list.append(self)

  def delete_user(self):
      '''
      delete users from users_list
      '''

      Users.users_list.remove(self)


  @classmethod
  def user_exists(cls, username, login_password):
      '''
      confirm user details in the users_list to authenticate access
      '''
      '''
      Args:
      ussername: name keyed in by user to login
      login_password: password used by user to login
      '''
      for user in Users.users_list:
        if username == username and user.login_password == login_password:
          return True
      return False

  @classmethod
  def search_username(cls, username):
      '''
      authorize access by username
      '''
      '''
      Args:
        username: name used by user to login
      '''
      for user in Users.users_list:
        if user.username == username:
          return user