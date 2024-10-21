# print("The Love Calculator is calculating your score...")
# name1 = input() # What is your name?
# name2 = input() # What is their name?
name1 = "NAISTA VIKTORIIA"
name2 = "HULA ANDRII"

# 🚨 Don't change the code above 👆
# Write your code below this line 👇
both = (name1 + name2).lower()
first = str(sum([both.count(char) for char in 'true']))
second = str(sum([both.count(char) for char in 'love']))
score = int(first + second)
print("The Love Calculator is calculating your score...")

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")