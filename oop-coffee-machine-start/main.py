from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
drinks_menu = Menu()


coffee_machine_on = True
while coffee_machine_on:
    choice = input(f"What would you like? ({drinks_menu.get_items()}): ")
    if choice == 'off':
        coffee_machine_on = False
    elif choice == 'report':
        coffee_machine.report()
    else:
        drink = drinks_menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
