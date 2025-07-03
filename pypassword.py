import random
import string
print('Welcome to the PyPassword Generator!')


def generate_password(letters_len=12, symbols_len=2, numbers_len=2):
    letters = string.ascii_letters
    symbols = '!#$%&()_*+'
    pass_list = []
    pass_list.extend(random.choices(letters, k=letters_len))
    pass_list.extend(random.choices(symbols, k=symbols_len))
    pass_list.extend(random.choices(string.digits, k=numbers_len))
    random.shuffle(pass_list)
    password = ''.join(pass_list)
    return password


generate_password()
