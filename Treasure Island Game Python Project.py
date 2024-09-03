print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
cross_road = input('You\'re at a cross road. Where do you want to go?' 'Type  "left" or "right".').lower()
if cross_road == "left":
    print("You've come to a lake. There is an island in the middle of the lake. ")
    choice = input('You\'ve Type Between Two Choices ? "swim" or "wait" ').lower()
    if choice == "swim":
        print("Game Over")
    elif choice == "wait":
      wait = input("You arrived island unharmed. There is a House with three doors. one red , one yellow and one blue. Which color do you choose ? ").lower()
      if wait == "yellow":
          print("You Found the Treasure. You Win")
      elif wait == "red":
          print("It's a room full of fire.Game Over")
      elif wait == "blue":
          print("You enter a room of beasts.Game Over")
      else:
          print("You Choose a door that doesn't exist. Game Over")

if cross_road.lower() == "right":
    print("Game Over")
