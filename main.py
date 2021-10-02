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

game_images = [rock, paper, scissors]

player_choice = int(input("What do you choose, 0 for 'rock', 1 for 'paper' and 2 for 'scissors'!\n"))

if player_choice > 2 or player_choice < 0:
  print("You typed an invalid number. You lose!")
else:

  print(f"You choose: {player_choice}")
  print(game_images[player_choice])

  computer_choice = random.randint(0, 2)
  print(f"Computer choose: {computer_choice}")
  print(game_images[computer_choice])

  if computer_choice == 0 and player_choice == 1:
    print("Congratuations. You Win!")

  elif computer_choice == 0 and player_choice == 2:
    print("You lose. Try again!")

  elif computer_choice == player_choice:
    print("It is a draw!")

  elif computer_choice == 1 and player_choice == 0:
    print("You lose. Try again!")

  elif computer_choice == 1 and player_choice == 2:
    print("Congratulation, You win!")

  elif computer_choice == 2 and player_choice == 0: 
    print("You lose. Try again!")

  elif computer_choice == 2 and player_choice == 1: 
    print("You lose. Try again!")



