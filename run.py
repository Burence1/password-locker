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

def generate_password():
  '''
  Function to create a password
  '''
  return Credentials.create_password()

def main():

  print(""*8 + "Password Locker App" + ""*8)
  print("--"*16)
  print("A password managing Application")

  while True:
    print("Enter your name")
    current_user = input().strip(' ').capitalize()
    if current_user != '':
      print(f"\nHello {current_user},")
      while True:
        print("kindly use these short codes to navigate the application: \n CA - create an account \n SI - sign into an existing account \n DA - delete your account \n EX - exit the application")
        short_code = input().upper()

        if short_code == 'CA':
          print("\nCreate an Account")
          print(""*17)
          print("Enter a username of choice")
          print(" "*4 + "*the username must contain alphabetical letters only and no spaces*")

          while True:
            username = input().capitalize()
            if username.isalpha():
              print("Enter Account password")
              print(" "*4 + "*the password must be 6 characters or longer*")
              while True:
                login_password = input()
                if len(login_password) >= 6:
                  add_user(create_user(username,login_password))
                  print(f"\nAccount for{username} has been created.\n Proceed to sign in.\n")
                  break
                else:
                  print(f"\n The entered password is too short")
                  print("Please use a password of 6 characters or more.")
                  continue
            else:
              print("\nThe username you entered is not valid.")
              print("Please use alphabetical letters only with no spaces.")
              continue
            break
          
        elif short_code == 'SI':
            print("\nSIGN IN")
            print("-"*7)

            print("Enter your username")
            username = input().strip(' ').capitalize()
            print("Enter your password")
            login_password = input().strip(' ')

            if check_existing_user(username, login_password):
              print("\nLog in successful")
              print("What would you like to do?")

              while True:
                print("\nUse these short codes for navigation: \n CC: create new credentials \n FC: find a credential \n DC: delete a credential \n SC: see all credentials \n LO: log out")
                credentials_navigation = input().upper()

                if credentials_navigation == 'CC':
                  print("\nCREATE NEW CREDENTIALS")
                  print("-"*22)

                  while True:
                    print("Application name:")
                    print(" "*4 + "*eg. Twitter*")
                    app_name = input().capitalize().strip(' ')

                    if app_name !='':
                      print(f"What is your current/desired username on {app_name}?")
                      acc_username = input()

                      while True:
                         print(f"\nDo you already have a password for your account on {app_name}? (Y/N)")
                         has_password = input().upper()

                         if has_password == 'Y':
                           print(f"Enter your {app_name} password")
                           acc_password = input()
                           add_credentials(create_credentials(app_name, acc_username, acc_password))
                           print(f"\nAccount credentials for your {app_name} account have been successfully saved.")
                           break

                    elif has_password == 'N':
                            while True:
                              print("Would you like a generated password? (Y/N)")
                              gen_pass = input().upper()
                              if gen_pass == 'Y':
                                print(f"\nHow long would you like the password to be?")
                                print(" "*4 + "less than 8 characters: WEAK" + "\n" + " "*4 + "8 characters: STRONG" + "\n" + " "*4 + "8-26 characters: VERY STRONG")
                                while True:
                                  try:
                                    passwordLength = int(input()
                                      if passwordLength in range(27):
                                        acc_password = generate_password(passwordLength)
                                        print(f"Password generated is {acc_password}")
                                        add_credentials(create_credentials(app_name, acc_username, acc_password))
                                        print(f"Account credentials for your {app_name} account have been successfully saved.\n")
                                        break
                                  except ValueError:
                                      print("\nYou did not pick a valid password length")
                                      print("Please pick a number between 0-26 and try again")
                                      continue

                              elif gen_pass == 'N':
                                print(f"Enter a password you wish to use for your {app_name} account")
                                print(" "*4 + "*password must be longer than 6 characters*")
                                while True:
                                  acc_password = input()
                                  if len(account_password) >= 6:
                                      add_credentials(create_credentials(app_name, acc_username, acc_password))
                                      print(f"Account credentials for your {app_name} have been successfully saved.\n")
                                      break
                                    else:
                                      print("\nThe password you entered is too short.")
                                      print("Please use a password of 6 characters or more.")
                                      continue
                              else:
                                  print("You did not select a valid option")
                                  print("Please enter (Y/N) and try again")
                                  continue
                                break

                              else:
                                print("You did not select a valid option")
                                print("Please enter (Y/N) and try again")
                                continue
                              break
                            break
                          else:
                            print("\nSorry, I didn't quite get the application name. Please try again.")
                            continue
                          