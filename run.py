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

def add_credentials(new_credentials):
  '''
  Function that saves new credentials
  '''
  new_credentials.add_credentials()

def remove_credentials(new_credentials):
  '''
  Function for deleting credentials
  '''
  new_credentials.delete_credentials()

def display_credentials():
  '''
  Function to display saved credentials
  '''
  return Credentials.display_credentials()
def check_existing_credentials(app_name):
  '''
  Function to check for saved credentials
  '''
  return Credentials.credentials_exist(app_name)

def search_app_name(app_name):
  '''
  Function to search for applications by name
  '''
  return Credentials.search_app_name(app_name)

def create_password(passwordLength):
  '''
  Function to create a password
  '''
  return Credentials.generate_password()

def main():
  print("*"*15)
  print(f"\nbienvenu!!!\nWelcome to Password Locker")
  print("Enter username")
  username = input()
  print(f"\nHey {username} enter your pick")

  while True:
    print("Enter username")
    new_user = input().strip(' ').capitalize()
    if new_user != '':
      print(f"\nHey {new_user}")
      while True:
        print("Use the short codes to navigate the application:  \n CA - create an account \n SI - sign into an existing account \n DA - delete your account \n EX - exit the application")
        short_code = input().upper()

        if short_code == 'CA':
          print("Enter username of preference")

          while True:
            username = input().upper()
            if username.isalpha():
              print("Enter password")
              while True:
                login_password = input()
                if len(login_password) >= 7:
                  add_user(create_user(username, login_password))
                  print(f"\nHey, {username}'s account has been created")
                  break
                else:
                  print("Your password shoul be more than longer than 7")
                  continue
            else:
              print("invalid username!!!")
              continue
            break
          break

        elif short_code == 'SI':
          print("SIGN IN")
          print("Enter username")
          username = input().strip(' ').capitalize()
          print("Enter password")
          login_password = input().strip(' ').capitalize()

          if find_existing_user(username, login_password):
            print("LOGIN SUCCESSFUL")

            while True:
              print("\nUse these short codes for navigation: \n CC: create new credentials \n FC: find a credential \n DC: delete a credential \n SC: see all credentials \n LO: log out")
              
if __name__ == '__main__':
    main()
