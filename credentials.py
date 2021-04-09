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

  def