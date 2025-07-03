from random import choice
from hangman_words import word_list
from hangman_art import stages
import pyfiglet

print(pyfiglet.figlet_format('hangman'))

lives = 6
# # word_list = ["ardvark", "baboon", "camel"]

chosen_word = choice(word_list)
print(chosen_word)

display = ["_"] * len(chosen_word)
print(display)

end_of_game = False

while not end_of_game:
    print(f'You have {lives} lives')
    guess = input("Guess a letter: ").lower()

    for index, letter in enumerate(chosen_word):
        if guess == letter:
            display[index] = letter
    if guess not in chosen_word:
        lives -= 1

    print(display)
    print(stages[lives])

    if not "_" in display:
        end_of_game = True
        print("You win!")
    elif lives == 0:
        end_of_game = True
        print("You lose..")
        print(f"Pssst, the solution is {chosen_word}.")
