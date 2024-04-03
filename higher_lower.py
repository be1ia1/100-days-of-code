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

# print(logo)
person1 = get_person(randint(0,len(data)-1))
person2 = get_person(randint(0,len(data)-1))


def game_round(person1, person2):
    print(f"Compare A: {person1["name"]}, a {person1["description"]}, from {person1["country"]}.")
    print(f"Against B: {person2["name"]}, a {person2["description"]}, from {person2["country"]}.")
    # print(person1["follower_count"], person2["follower_count"])
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    print(person1["follower_count"], person2["follower_count"])
    print(person1["follower_count"] > person2["follower_count"])
    if user_answer == 'a':
        print(person1)
        if person1["follower_count"] > person2["follower_count"]:
            return person1
        else:
            return False
    elif user_answer == 'b':
        print(person2)
        if person2["follower_count"] > person1["follower_count"]:
            return person2
        else:
            return False

# print(game_round(person1, person2))
# next = game_round(person1, person2)
next = get_person(randint(0,len(data)-1))
while not game_over:
    if not next:
        print(score)
        game_over = True

    game_round(next, get_person(randint(0,len(data)-1)))
    score +=1



# print(answer[user_answer])