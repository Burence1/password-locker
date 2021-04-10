from user import Users
from credentials import Credentials

def create_user(username, login_password):
  '''
  Function that creates a new user
  '''
  new_user = Users(username, login_password)
  return new_user

def add_user(user):
  '''
  Function for saving users
  '''
  user.add_user()

def remove_user(user):
  '''
  Function for deleting users
  '''
  user.delete_user()

def find_user(username):
  '''
  Function that searches for users via username
  '''
  return Users.search_username(username)

def find_existing_user(username,login_password):
  '''
  Function that authenticates users
  '''
  return Users.user_exists(username,login_password)

def create_credentials(app_name, acc_username, acc_password):
  '''
  Function for creating new credentials
  '''
  new_credentials = Credentials(app_name, acc_username, acc_password)
  return new_credentials


