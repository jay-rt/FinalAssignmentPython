from random import randint as r

#negotiating mom for some money
def askMoney():
  print("You need some money, so you asked mom polietly!!!")
  print("Mom, I am going to see my friend, can you lend me some money?")
  money = r(25,100)
  choice = int(input("How much do you need? "))
  while True:
    if choice >= money + 15:
      choice = int(input("That is a lot of money. Ever thought of asking less. "))
    elif choice <= money + 15 and choice >= money:
      choice = int(input("I still think that's a lot. Little bit less and I will think about it. "))
    elif choice < money and choice >= money - 5:
      choice = int(input("$5 less and I might agree. "))
    elif choice <= money - 5:
      print("Fine. Take it!!! Don't waste on silly things though")
      print("Sure mom!!!")
      break
  return choice


#bargaining with shopkeeper for game
def bargain(cash):
  print("There is an old game in there. Maybe you can get it for cheap!!!")
  print("Hello shopkeeper! How much for that old game?")
  money = r(1, 20)
  choice = int(input("How much can you pay? "))
  while True:
    if choice <= money - 10:
      choice = int(input("Don't make me laugh. Come back in 10 years and I will think about it. "))
    elif choice >= money - 10 and choice < money - 5:
      choice = int(input("How about a little bit more?"))
    elif choice >= money -5 and choice <= money:
      choice = int(input("$5 more and its all yours. "))
    elif choice > money and choice < money + 5:
      if choice > cash - 15:
        print("Sorry, looks like I dont have enough money. I will come later.")
        choice = 0
      else:
        print("You make a fine bargain. Here, it's all yours!!!")
      break
  return choice