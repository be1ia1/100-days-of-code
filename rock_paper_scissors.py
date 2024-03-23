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

#Write your code below this line 👇
from random import choice

variants = ['rock', 'paper', 'scissors']

player1 = choice(variants)
player2 = choice(variants)

print(f"{player1} vs {player2}")

if player1 == player2:
    print('Draw!')

elif player1 == 'rock' and player2 == 'scissors' or player1 == 'paper' and player2 == 'rock' or player1 == 'scissors' and player2 == 'paper':
    print(f"player1 win!")
else:
    print(f"player2 wins!")