import sys
from random import randint

print("Welcome to the Number Guessing Game!")

def game_round():
    number = randint(1,100)
    # print(number)
    print("I'm thinking of a number between 1 and 100.")
    # difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    difficulty = 'easy'
    attempts = 10 if difficulty == 'easy' else 5

    player_wins = False
    while attempts > 0:
        print(f"You have {attempts} attempts.")
        player_guess = int(input("Make a guess: "))
        if player_guess == number:
            player_wins = True
            break
        elif player_guess > number:
            print("Too high.")
            attempts -= 1
        elif player_guess < number:
            print("Too low.")
            attempts -= 1


    if player_wins:
        print("You win!")
    else:
        print("You lose..")
    one_more = input("One more game: ")
    if one_more == 'y':
        game_round()
    else:
        print("Goodbye!")
        sys.exit()

game_round()