print('Welcome to the Band Name Generator.')
city_name = input("What's the name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")
pet_sex = input('Pet sex? m/f\n')
suffix = 'skiy' if pet_sex == 'm' else 'ska'
print(f'Your band name could be {city_name}{suffix} {pet_name}')
