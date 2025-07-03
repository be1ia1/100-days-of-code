import sys


def calculation():
    while True:
        first_num = int(input('Enter first number: '))
        keep_calculation = True
        while keep_calculation:
            second_num = int(input('Enter second number: '))
            print('+\n-\n*\n/')
            operation = input('Pick an operation: ')
            match operation:
                case '+':
                    answer = first_num + second_num
                case '-':
                    answer = first_num - second_num
                case '*':
                    answer = first_num * second_num
                case '/':
                    answer = first_num / second_num
            print(f'The result of {first_num} {operation} {second_num} = {answer}')
            use_result = input('Do you want use result in next calculation? ')
            if use_result == 'y':
                first_num = answer
            elif use_result == 'n':
                break
            else:
                sys.exit()


calculation()
