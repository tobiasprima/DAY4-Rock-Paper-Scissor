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

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors")
print("You choose:")
if user_choice == '3':
  print("I am pretty sure my instruction was clear.")
else:
  if user_choice == '0':
    print(rock)
  elif user_choice == '1':
    print(paper)
  elif user_choice =='2':
    print(scissors)
  print("The computer choose:")
  import random
  computer_choice = random.randint(0,2)
  if computer_choice == '0':
    print(rock)
  elif computer_choice == '1':
    print(paper)
  elif computer_choice == '2':
    print(scissors)
theirchoice = user_choice + str(computer_choice)
draw = ["11", "22", "00"]
win = ["02", "10", "21"]
lose = ["01", "12", "20"]
if theirchoice in draw:
  print("It is a draw")
elif theirchoice in win:
  print("You win!)
elif theirchoice in lose:
  print("You lose!)
