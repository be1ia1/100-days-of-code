import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

grey = len(data[data['Primary Fur Color'] == 'Gray'])
red = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black = len(data[data['Primary Fur Color'] == 'Black'])

color = ['grey', 'red', 'black']
count = [grey, red, black]

df = pd.DataFrame(list(zip(color, count)), columns=['Fur Color', 'Count'])

df.to_csv('squrrel_count.csv')
