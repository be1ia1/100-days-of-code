from random import randint
import pyfiglet

banner = pyfiglet.figlet_format('Guess The Number')
print(banner)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")
number = randint(1, 100)
print(f"Pssst, the correct answer is: {number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
attempts = 10 if difficulty == 'easy' else 5
game_continue = True
while game_continue and attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    answer = int(input("Make a guess: "))
    if answer == number:
        print(f"You got it! The answer was {answer}.")
        game_continue = False
    elif answer > number:
        print("Too high.")
        attempts -= 1
    elif answer < number:
        print("Too low.")
        attempts -= 1
if attempts == 0 and answer != number:
    print("You lose.")


# import sys
# from random import randint

# print("Welcome to the Number Guessing Game!")

# def game_round():
#     number = randint(1,100)
#     # print(number)
#     print("I'm thinking of a number between 1 and 100.")
#     # difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
#     difficulty = 'easy'
#     attempts = 10 if difficulty == 'easy' else 5

#     player_wins = False
#     while attempts > 0:
#         print(f"You have {attempts} attempts.")
#         player_guess = int(input("Make a guess: "))
#         if player_guess == number:
#             player_wins = True
#             break
#         if player_guess > number:
#             print("Too high.")
#             attempts -= 1
#         if player_guess < number:
#             print("Too low.")
#             attempts -= 1


#     if player_wins:
#         print("You win!")
#     else:
#         print(f"You lose.. The number is: {number}")
#     one_more = input("One more game: ")
#     if one_more == 'y':
#         game_round()
#     else:
#         print("Goodbye!")
#         sys.exit()

# game_round()
