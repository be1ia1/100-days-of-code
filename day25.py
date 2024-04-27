# import csv

# with open('weather_data.csv') as fo:
#     data = csv.reader(fo)
#     next(data)
#     temperatures = []
#     for row in data:
#         temperatures.append(int(row[1]))
# print(temperatures)

import pandas

data = pandas.read_csv('weather_data.csv')

# print(data['temp'])
data_dict = data.to_dict()
# print(data_dict)

temp_list = data['temp'].to_list()
# print(round(sum(temp_list) / len(temp_list), 2))
# print(round(data['temp'].mean(), 2))
# print(data['temp'].max())

print(data[data['day'] == 'Monday'])

# print(data[data.temp == data['temp'].max()])

# celcium = data[data.day == 'Monday'].temp[0]
# print(celcium * 9 / 5 + 32)


