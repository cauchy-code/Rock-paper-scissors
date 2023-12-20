rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random

game = [rock, paper, scissors]
choice = random.randint(0,2)
user = int(input("Enter Rock paper or scissors as 0, 1 or 2: "))
print(game[user])
print("The computer choose: ")
print(game[choice])
if game[user] == game[choice]:
  print("Its a Draw!!")
  
elif game[user] == rock:
  if game[choice] == scissors:
    print("You win!!")
  else:
    print("You lose!!")

elif game[user] == scissors:
  if game[choice] == paper:
    print("You win!!")
  else:
    print("You lose!!")

elif game[user] == paper:
  if game[choice] == rock:
    print("You win!!")
  else:
    print("You lose!!")

else:
  print("Invalid input")
  
    
  



