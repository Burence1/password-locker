import random
import string

class Credentials:

  '''
  class that creates new instances of Credentials
  '''

  credentials_list =[]

  def __init__(self, app_name, acc_username,acc_password):
      '''
      __init__ method helps create new instances of the Credentials class.
      
      Args:
        app_name: Application whose password is stored
        acc_username: Application account username
        acc_password: password for application
        '''
      self.app_name = app_name
      self.acc_username = acc_username
      self.acc_password = acc_password

  def add_credentials(self):
      '''
      method that stores user credentials in credentials_list
      '''
      Credentials.credentials_list.append(self)

  def delete_credentials(self):
      '''
      method for deleting credentials from credentials_list
      '''
      Credentials.credentials_list.remove(self)

  @classmethod
  def search_app_name(cls, app_name):

      '''
      method that enables searching for applications by their names

      Args:
        app_name: Application whose password is stored
      '''
      for credentials in Credentials.credentials_list:
        if credentials.app_name == app_name:
          return credentials
  @classmethod
  def create_password(cls):
      '''
      method that generates passwords randomly
      '''

      created_password = string.ascii_letters + string.digits + string.punctuation
      generated_password = ''.join((random.choice(created_password)))
      return generated_password

  @classmethod
  def credentials_exist(cls, app_name):
      '''
      method that checks for credentials in the credentials_list
      
      Args:
        app_name: Application whose password is stored
      '''

      for credentials in Credentials.credentials_list:
        if credentials.app_name == app_name:
          return True
        return False

  @classmethod
  def display_credentials(cls):
      '''
      method for displaying users credentials
      '''

      return Credentials.credentials_list
