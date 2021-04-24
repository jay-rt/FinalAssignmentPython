import login
import json
import urllib.request
from os import system, name, path
from random import randint as r
from replit import audio
import negotiate

#function to clear the screen
def clear():
  system("cls" if name == "nt" else "clear")

#playing audio in game
source = audio.play_file('megalovania.mp3')
source.volume -= .25
source.set_loop(3)

#function to call api
def api_call(url):
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
  return result

#loading user data from local file
with open("current_user.json") as file:
  user = json.load(file)

#assigning values obtained from local file to variables
username = user['username']
password = user['password']
room = user['location']
health = user['health']
money = user['money']

url = 'https://raw.githubusercontent.com/jay-rt/pythonFinal/main/game.json'
response = urllib.request.urlopen(url)
data = json.loads(response.read())

while True:
  clear()

  #printing your status
  print("Your current health:", health)
  print("Money:", money)
  print("Current Location:", data[room]['name'])
  print("\n")

  #checking if your HP is equal to or below 10
  if health <= 10:
    print("Nothing is going as planned. You feel exhausted.")
    print("You took a quick nap.")
    print("\n")
    health += 15

  print(data[room]['story'])

  if data[room]['name'] == "mom room":
    #negotiating mom for money
    cash = negotiate.askMoney()
    print(f"You got ${cash} from mom. You are happy.")
    money += cash
  elif data[room]['name'] == "shop":
    #negotiating with shopkeeper for an old game if you have some money
    if money != 0:
      price = negotiate.bargain(money)
      if price != 0:
        money -= price
        print("You finally got the game you wanted!!!")
        health += 5
      else:
        print("You so badly wanted the game.")
        health -= 5

  #triggering random events
  chance = r(1,4)
  #if chance rolls 1, positive events
  if chance == 1 and data[room]['positive'] != "N/A":
    print(data[room]['positive'])
    if data[room]['name'] == "sister room" or data[room]['name'] == "brother room":
      health += 20
    elif data[room]['name'] == "principal office":
      health += 10
    else:
      health += 5
  #if chance rolls 3, negative events
  elif chance == 3 and data[room]['negative'] != "N/A":
    print(data[room]['negative'])
    if data[room]['name'] == "sister room":
      health -= 20
    if data[room]['name'] == "brother room" or data[room]['name'] == "principal office":
      health -= 10
    else:
      health -= 5
  #if chance rolls 4, events with api calls
  elif chance == 4:
    if data[room]['name'] == "sister room":
      url = "https://ghibliapi.herokuapp.com/films"
      movie = api_call(url)
      index = r(0, len(movie) - 1)
      print(f"You watched '{movie[index]['title']}' with your sister. It was a fun watch.\n")
      health += 20
    elif data[room]['name'] == "brother room":
      url = 'http://api.open-notify.org/astros.json'
      space = api_call(url)
      print("\nYour brother is excited to go space. You told him about people in space now. ")
      print(f"There are currently {space['number']} of people in ISS.")
      print("And they are: ")
      for people in space['people']:
        print(people['name'])
      print("Your brother looks amazed and is very happy\n")
      health += 20
    elif data[room]['name'] == "friend house":
      url = "https://official-joke-api.appspot.com/jokes/random"
      joke = api_call(url)
      print("\nYou told the joke to your friend")
      print(joke['setup'])
      print("She looks curiouos.")
      print(joke['punchline'])
      chance = r(0,1)
      if chance == 0:
        print("She doesn't look impressed. You feel weird.")
        health -= 15
      else:
        print("She is laughing. You feel great.")
        health += 15
      print("\n")

  #checking win and loss condition    
  if data[room]['win'] == 1:
    print("You win !!!")
    print("🏆 🏆 🏆")
    #reset user file
    login.initialize(username, password)
    break
  elif data[room]['lose'] == 1:
    print("You lose !!!")
    print("😞  😞  😞")
    login.initialize(username, password)
    break

  #logging progress to local file
  user['location'] = room
  user['health'] = health
  user['money'] = money

  with open("current_user.json", "w") as write_file:
      json.dump(user, write_file, indent = 2)

  save = False

  #validating player input
  while True:
    print(data[room]['nav'])
    choice = input("Please select one of the options: ")
    if choice == "1":
      room = data[room]['room_one'] - 1
      break
    elif choice == "2":
      room = data[room]['room_two'] - 1
      break
    elif choice == "3":
      room = data[room]['room_three'] - 1
      break
    elif choice == "4":
      print("Your data is being saved....")
      save = True
      #copying local file to user file when quitting
      with open(path.join("users", username + ".json"), "w") as write_file:
        json.dump(user, write_file, indent = 2)
      print("Save successful. You can continue from where you leftoff next time!!!")
      break
    else:
      print("Invalid input.")

  #checking if user selected the quit option
  if save:
    break