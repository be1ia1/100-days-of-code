import sys
from random import randint

from art import logo, vs
from game_data import data


def get_person(number):
    return data[number]


def compare_person(person1, person2, user_answer):
    answer = {
        'a': person1["follower_count"] > person2["follower_count"],
        'b': person2["follower_count"] > person1["follower_count"]
    }
    return answer[user_answer]


score = 0
game_over = False


def game_round(person1, person2):
    print(f"Compare A: {person1["name"]}, a {
          person1["description"]}, from {person1["country"]}.")
    print(f"Against B: {person2["name"]}, a {
          person2["description"]}, from {person2["country"]}.")

    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_answer == 'a':
        if person1["follower_count"] > person2["follower_count"]:
            return person1
        # else:
        #     return False
    elif user_answer == 'b':
        if person2["follower_count"] > person1["follower_count"]:
            return person2
        # else:
        #     return False


while not game_over:
    if score == 0:
        person1 = get_person(randint(0, len(data)-1))
    person2 = get_person(randint(0, len(data)-1))
    result = game_round(person1, person2)
    if not result:
        print(f"{person1["name"]} has {person1["follower_count"]} vs {
              person2["name"]} has {person2["follower_count"]}")
        print(f"Final score is: {score}")
        print("Game Over..")
        game_over = True
    else:
        person1 = result
        score += 1
