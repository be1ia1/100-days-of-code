import sys
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maschine = CoffeeMaker()
money_maschine = MoneyMachine()
menu_item = Menu()

is_online = True
while is_online:
    answer = input("What would you like? (espresso/latte/cappuccino): ")
    if answer == "report":
        coffee_maschine.report()
    elif answer == "off":
        sys.exit()
    else:
        drink = menu_item.find_drink(answer)
        if coffee_maschine.is_resource_sufficient(drink):
            if money_maschine.make_payment(drink.cost):
                coffee_maschine.make_coffee(drink)



# from menu import Menu
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine


# coffee_machine = CoffeeMaker()
# money_machine = MoneyMachine()
# drinks_menu = Menu()


# coffee_machine_on = True
# while coffee_machine_on:
#     choice = input(f"What would you like? ({drinks_menu.get_items()}): ")
#     if choice == 'off':
#         coffee_machine_on = False
#     elif choice == 'report':
#         coffee_machine.report()
#     else:
#         drink = drinks_menu.find_drink(choice)
#         if coffee_machine.is_resource_sufficient(drink):
#             if money_machine.make_payment(drink.cost):
#                 coffee_machine.make_coffee(drink)
