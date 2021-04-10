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

            if find_existing_user(username, login_password):
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
                                    passwordLength = int(input())
                                    if passwordLength in range(27):
                                      acc_password = create_password(passwordLength)
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
                                  if len(acc_password) >= 6:
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
                              
                            # break
                            # break
                    else:
                      print("\nSorry, I didn't quite get the application name. Please try again.")
                    continue
                elif credentials_navigation == 'FC':
                          if len(Credentials.credentials_list) >= 1:
                              print("\nFIND CREDENTIALS")
                              print("-"*16)
                              print("Enter the application whose credentials you'd like to find:")
                              print(" "*4 + "*eg. Instagram*")
                              searched_application = input().capitalize()

                              if check_existing_credentials(searched_application):
                                  searched_credential = search_app_name(searched_application)
                                  print(f"\nApplication name: {searched_credential.app_name}, \n username: {searched_credential.acc_username} \n password: {searched_credential.acc_password}")
                                  
                              else:
                                 print(f"\nThe credentials for {searched_application} don't exist.")

                              continue
                          else:
                            print("\nYou don't seem to have any credentials saved.")
                            continue

                elif credentials_navigation =='DC':
                        if len(Credentials.credentials_list) >= 1:
                          print("\nDELETE CREDENTIALS")
                          print("-"*18)
                          print("Application name:")
                          print(" "*4 + "*eg. Twitter*")
                          app_name=input().capitalize()

                          if check_existing_credentials(app_name):
                            while True:
                              print(f"Are you sure you want to delete credentials for your {app_name}? (Y/N)")
                              delete_credential = input().upper()
                              if delete_credential == 'Y':
                                remove_credentials(search_app_name(app_name))
                                print(f"\nCredentials for {app_name} have been successfully deleted")
                                break
                              elif delete_credential == 'N':
                                print("\nPhew! Your credentials are still intact.")
                                break
                              else:
                                print("You did not select a valid option")
                                print("Please enter (Y/N) and try again\n")
                                continue

                        else:
                          print(f"\nCredentials for {app_name} don't exist.")
                          continue
                    
                else:
                      print("\nYou don't seem to have any credentials saved.")
                      continue
                
            elif  credentials_navigation == 'SC':
                  if len(Credentials.credentials_list)>=1:
                    display_credentials

                    print("\nHERE ARE ALL YOUR CREDENTIALS")
                    print("-"*29)
                    for credential in display_credentials():
                      print(f"\nApplication name: {credential.app_name} \n Username: {credential.acc_username} \n Password: {credential.acc_password}")
                    continue
                  else:
                    print("\nYou don't seem to have any credentials saved.")
                    continue
            elif credentials_navigation =='LO':
              print("\nYou have successfully logged out..\n")
              break

            else:
                  print("\nYou did not select a valid option.")
                  print("Please try again.")
                  continue
        else:
              print("\nInvalid username and password")
              print("Try again or create an account\n")
              continue
        
    elif short_code == 'DA':
          if len(Users.users_list) >= 1:
              print("\nDELETE YOUR ACCOUNT")
              print("-"*19)
              print("Enter your username")
              username = input().capitalize()
              print("Enter your password")
              login_password = input()

              if find_existing_user(username, login_password):
                while True:
                      print(f"Are you sure you want to delete your account? (Y/N)")
                      delete_account=input().upper()
                      if delete_account == 'Y':
                          remove_user(find_user(username))
                          print(f"\nYour account has been successfully deleted.\n")
                          break
                      elif delete_account == 'N':
                          print("\nPhew! Your account is still active.\n")
                          break
                      else:
                          print("You did not select a valid option")
                          print("Please enter (Y/N) and try again")
                          continue
                else:
                  print("\nSeems like you do not have an active account or you entered the wrong details.")
                  print("Please try again.\n")
                  continue
              else:
                  print("\nSorry, there are no active accounts at the moment.\n")
                  continue
          elif short_code == 'EX':
            print("\nAdios!!!....")
            break

          else:
            print("\nYou did not select a valid option.")
            print("Please try again.\n")
            continue

    else:
          print("\nSorry, I didn't quite get your name. Please try again")
          continue

    break

if __name__ == '__main__':
    main()