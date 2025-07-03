from random import choice

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

variants = ['rock', 'paper', 'scissors']


def game_round():
    player1 = choice(variants)
    player2 = choice(variants)

    for player in (player1, player2):
        if player == 'rock':
            print(rock)
        elif player == 'paper':
            print(paper)
        else:
            print(scissors)

    if player1 == player2:
        print('Draw')
    else:
        if (player1 == 'rock' and player2 == 'scissors') or\
            (player1 == 'paper' and player2 == 'rock') or\
                (player1 == 'scissors' and player2 == 'paper'):
            print('Player 1 Win')
        else:
            print('PLayer 2 Win')


game_round()
