from art import logo, vs
from game_data import data
from random import choice

print(logo)

first = choice(data)

score = 0
game_not_over = True


def compare_variants(variant_a, variant_b, user_answer):
    if variant_a['follower_count'] > variant_b['follower_count'] and user_answer == 'a':
        return variant_a
    if variant_a['follower_count'] < variant_b['follower_count'] and user_answer == 'b':
        return variant_b
    if variant_a['follower_count'] == variant_b['follower_count']:
        return variant_a if user_answer == 'a' else variant_b
    return False


def game_round(variant_a):
    variant_b = choice(data)
    while variant_b == variant_a:
        variant_b = choice(data)
    print(f"Compare A: {variant_a['name']}, a {variant_a['description']}, from {variant_a['country']}.")
    print(vs)
    print(f"Compare B: {variant_b['name']}, a {variant_b['description']}, from {variant_b['country']}.")
    user_answer = (input('Who has more followers? Type "A" or "B": ')).lower()
    result = compare_variants(first, variant_b, user_answer)
    return result


while game_not_over:
    round_result = game_round(first)
    if not round_result:
        print(f'Game over.. Score: {score}')
        game_not_over = False
    else:
        score += 1
        first = round_result


# import sys
# from random import randint

# from art import logo, vs
# from game_data import data


# def get_person(number):
#     return data[number]

# score = 0
# game_over = False


# def game_round(person1, person2):
#     print(f"Compare A: {person1["name"]}, a {
#           person1["description"]}, from {person1["country"]}.")
#     print(f"Against B: {person2["name"]}, a {
#           person2["description"]}, from {person2["country"]}.")

#     user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

#     if user_answer == 'a':
#         if person1["follower_count"] > person2["follower_count"]:
#             return person1
#     elif user_answer == 'b':
#         if person2["follower_count"] > person1["follower_count"]:
#             return person2

# while not game_over:
#     if score == 0:
#         person1 = get_person(randint(0, len(data)-1))
#     person2 = get_person(randint(0, len(data)-1))
#     result = game_round(person1, person2)
#     if not result:
#         print(f"{person1["name"]} has {person1["follower_count"]} vs {
#               person2["name"]} has {person2["follower_count"]}")
#         print(f"Final score is: {score}")
#         print("Game Over..")
#         game_over = True
#     else:
#         person1 = result
#         score += 1
