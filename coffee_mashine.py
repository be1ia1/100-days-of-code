from coffee_mashine_start import MENU, resources


def user_input():
    '''Ask user about drink to make'''
    choose = input("What would you like? (espresso/latte/cappuccino): ")
    return choose

def check_resources(drink):
    '''Check if machine have enough resources to make drink'''
    check_list = []
    for k, v in MENU[drink]['ingredients'].items():
        if v <= resources.get(k):
            check_list.append(True)
        else:
            check_list.append(False)
            print(f"Sorry there is not enough {k}")
    return all(check_list)

def calculate_coins():
    '''Calculate user coints'''
    print('Please insert coins.')
    quaters = int(input("How many quaters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    # quaters = 12
    # dimes = 12
    # nickles = 12
    # pennies = 12
    user_sum = quaters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return round(user_sum, 2)

def check_transaction(user_sum, user_input):
    drink_cost = MENU[user_input]["cost"]
    if user_sum >= drink_cost:
        return True
    else:
        return False

def transaction(user_sum, user_input):
    drink_cost = MENU[user_input]["cost"]
    change = round(user_sum - drink_cost, 2)
    resources['money'] += drink_cost
    if change:
        print(f"Here is ${change} in change.")

def make_coffee(user_input):
    for k, v in MENU[user_input]['ingredients'].items():
        resources[k] -= v
    return f"Here is your {user_input}. Enjoy!"

coffee_machine_on = True
while coffee_machine_on:
    next_step = user_input()
    if next_step == 'off':
        coffee_machine_on = False
    elif next_step == 'report':
        for k, v in resources.items():
            if k == 'water' or k == 'milk':
                print(f"{k.title()}: {v}ml")
            elif k == 'coffee':
                print(f"{k.title()}: {v}g")
            elif k == 'money':
                print(f"{k.title()}: ${v}")
    else:
        drink = next_step
        if check_resources(drink):
            user_sum = calculate_coins()
            if check_transaction(user_sum, drink):
                transaction(user_sum, drink)
                print(make_coffee(drink))
