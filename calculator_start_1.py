import sys
from random import randint

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b



def calculation():
    operations = {
        "+": add,
        "-": substract,
        "*": multiply,
        "/": divide
    }
    num1 = float(input("Insert number #1: "))

    keep_calculating = True
    while keep_calculating:
        num2 = float(input("Insert number #2: "))
        for operation in operations:
            print(operation)
        selected_operation = input("Select operation: ")
    
        result = operations[selected_operation](num1, num2)

        print(f"The result is: {num1} {selected_operation} {num2} = {result}")

        continue_calc = input("Do you want continue calculate with result? ")
        if continue_calc == 'q':
            sys.exit()
        elif continue_calc == 'y':
            num1 = result
        elif continue_calc == 'n':
            keep_calculating = False
            calculation()

calculation()