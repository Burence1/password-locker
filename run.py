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

def delete_user(user):
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


def check_existing_credentials(app_name):
  '''
  Function to check for saved credentials
  '''
  return Credentials.credentials_exist(app_name)

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


def search_app_name(app_name):
  '''
  Function to search for applications by name
  '''
  return Credentials.search_app_name(app_name)

def create_password(Length):
  '''
  Function to create a password
  '''
  generated_password = Credentials.generate_password()
  return generated_password

def main():
  print("*"*15)
  print("\nBienvenu!!!\nWelcome to Password Locker")
  print(' '*10, "🤖")
  print("="*26)
  print("Enter name")
  while True:
    new_user = input().strip(' ').capitalize()
    if new_user != '':
      print(f"\nHey {new_user} 🙋")
      while True:
        print("Use the short codes to navigate the application: \n si - sign into your account \n ca - create account \n da - delete your account \n ex - exit the application")
        print("***"*16)
        short_code = input().upper()

        if short_code == 'CA':
          print("Enter username of preference")

          while True:
            username = input().upper()
            if username.isalpha():
              print("Enter password 🔓")
              while True:
                login_password = input()
                if len(login_password) >= 7:
                  add_user(create_user(username, login_password))
                  print(f"\nHey, {username}'s account has been created ✔️")
                  print(f"\n Sign in")
                  break
                else:
                  print("\nYour password should be more than longer than 7 🥺")
                  continue
            else:
              print("\ninvalid username!!! 😞")
              print("*"*10)
              continue
            break
          

        elif short_code == 'SI':
          print("SIGN IN")
          print("Enter username")
          username = input().strip(' ').capitalize()
          print("Enter password")
          login_password = input().strip(' ').capitalize()

          if find_existing_user(username, login_password):
            print("LOGIN SUCCESSFUL 😊")

            while True:
              print("\nUse these short codes for navigation: \n ad: Add new account details \n fd: find an account details by name \n dd: delete account details \n sd: see all saved details \n lo: log out")
              credentials_logic = input().upper()

              if credentials_logic == 'AD':
                print("Create new Details")
                
                while True:
                  print("Application name:")
                  app_name = input().strip(' ').capitalize()

                  if app_name != '':
                    print(f"Enter your {app_name}'s username")
                    acc_username = input()

                    while True:
                      print(f"\nAlready have an existing password for {app_name}?")
                      print("(Y/N)")
                      existing_password = input().upper()

                      if existing_password == 'Y':
                        print (f"\nEnter current {app_name} password")
                        acc_password = input()
                        add_credentials(create_credentials(app_name,acc_username,acc_password))
                        print(f"\n{app_name}'s details have been saved ✔️")
                        break

                      elif existing_password == 'N':
                        while True:
                          print(f"\nComputer generated or personal-custom password")
                          print("(Y/N)?")
                          
                          generated_pass = input().upper()
                          if generated_pass == 'Y':
                            acc_password = create_password(Length=9)
                            print(f"generated password is {acc_password}")
                            add_credentials(create_credentials(app_name, acc_username, acc_password))
                            break

                          elif generated_pass == 'N':
                            while True:
                              acc_password= input()
                              if len(acc_password) >= 7:
                                add_credentials(create_credentials(app_name, acc_username, acc_password))
                                print(f"{app_name}'s details successfully saved")
                                break
                              else:
                                print("Password entered is invalid ❌")
                                continue

                          else:
                            print("Invalid selection\n Enter (Y/N) ❌")
                            continue
                          break
                        break
                  else:
                    print("Invalid application name ❗")
                    continue
                  break
              elif credentials_logic == 'FD':
                if len(Credentials.credentials_list) >= 1:
                  print("FIND DETAILS ⏳")
                  print("Enter Application name to search")

                  search = input().capitalize()

                  if check_existing_credentials(search):
                    search_cred = search_app_name(search)
                    print(f"\nApplication name: {search_cred.app_name}")
                    print(f"username:{search_cred.acc_username}")
                    print(f"password: {search_cred.acc_password}")

                  else:
                    print(f"\nSorry, application details don't exist ❌")
                    print("--"*15)

                  continue
                else:
                  print(f"\nSorry, no saved credentials ❌")

                continue
              elif credentials_logic == 'DD':
                if len(Credentials.credentials_list)>=1:
                  print("Delete Application details")
                  print("application name:")
                  app_name = input().capitalize()
                  
                  if check_existing_credentials(app_name):
                    while True:
                      print("Delete? \n (Y/N)")
                      remove_cred = input().upper()
                      if remove_cred == 'Y':
                        remove_credentials(search_app_name(app_name))
                        print(f"{app_name} DELETED")
                        break
                      elif remove_cred == 'N':  
                        print("Details not deleted")
                      break
                  else:
                    print(f"\n{app_name}'s details don't exist")
                    continue
                else:
                  print("you don't have any details")
                  continue
              elif credentials_logic == 'SD':
                if len(Credentials.credentials_list) >=1:
                  display_credentials()
                  print("All Details")
                  for credential in display_credentials():
                    print(f"\nApplication name: {credential.app_name}")
                    print(f"\nApplication password: {credential.acc_password}")
                    continue
                else:
                  print(f"\n you do not have any credentials 🥺")
                  continue
              elif credentials_logic == 'LO':
                print("\nYou are logged out!!")
                break
              else:
                print("Invalid selection ❌")
                continue
          else:
            print("Invalid username ❌")
            continue
        
        elif short_code == 'DA':
          if len(Users.users_list) >= 1:
            print("Enter username")
            username = input().upper()

            if find_user(username):
              while True:
                print(f"Delete account?")
                print("(Y/N)")
                del_acc = input().upper()
                if del_acc == 'Y':
                    delete_user(find_user(username))
                    print(f"Deleted {username}'s account 😟\n")
                    break
                elif del_acc == 'N':
                    print("Account not deleted")
                    break
                else:
                  print("Invalid selection ❌")
            
                  continue
            else:
              print("Invalid account ❌")

          else:
            print("No available users for deleting ❌")
            continue

        elif short_code == 'EX':
          print("ADIOS!!! 👋")
          break
        else:
          print("Invalid selection ❌")
          continue
    else:
      print("invalid username, re-enter! ❗")
      continue
    
if __name__ == '__main__':
    main()
