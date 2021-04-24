import os
import json

#creating a folder name user if it doesn't exist
path = 'users'
if not os.path.exists(path):
  os.makedirs(path)

#initializing the game vaiables
def initialize(username, password):
  user = {}
  user['username'] = username
  user['password'] = password
  user['health'] = 100
  user['money'] = 0
  user['location'] = 0
  with open(os.path.join(path, username + ".json"), "w") as write_file:
    json.dump(user, write_file, indent = 2)

def login():
  print("Please enter your username and password to login:")
  username = input("Username: ")
  username = username.lower()
  password = input("Password: ")

  try:
    with open(os.path.join(path, username + ".json"), "r") as read_file:
      data = json.load(read_file)
  except FileNotFoundError:
    print("We don't have your account information. Please register and try again.")
    signUp()
  else:
    if data['username'] == username and data['password'] == password:
      print("Logged in. Loading data....")
      with open('current_user.json', 'w') as current_file:
        json.dump(data, current_file, indent = 2)
    else:
      print("Incorrect username or password. Try again!")
      login()
    
def signUp():
  print("Please fill in the details below to register!")
  username = input("Username: ")
  username = username.lower()

  #checking if the file with entered username exists or not
  if os.path.isfile(os.path.join(path, username + ".json")):
    print("Sorry, but looks like the username is already taken! Try again with different username!")
    signUp()
  else:
    password1 = input("Password: ")
    password2 = input("Re-type your password: ")
    if password1 != password2:
      signUp()
    else:
      print("Congratulations! You have created an account\n")
      initialize(username, password1)
      login()

#asking if the user has an account or not
choice = input("Do you have an account: y/n ")
if choice.lower() == "y":
  login()
else:
  signUp()