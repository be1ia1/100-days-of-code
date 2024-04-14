# import colorgram

# def get_tuple(rgb_obj):
#     return rgb_obj[0],rgb_obj[1],rgb_obj[2]

# colors = colorgram.extract('image.jpg', 30)
# all_colors = [get_tuple(color.rgb) for color in colors]
# print(all_colors)

import turtle
import random

palette = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

screen = turtle.Screen()
screen.colormode(255)

timmy = turtle.Turtle()
timmy.penup()

def write_line(start_position):
    # timmy.penup()
    timmy.goto(start_position)
    # timmy.pendown()
    for _ in range(10):
        timmy.dot(20, random.choice(palette))
        
        timmy.forward(50)
    end_position = timmy.position()
    return -250, end_position[1] + 50

y = -250
for _ in range(10):
    write_line((-250, y))
    y += 50

# print(write_line((-250, -250)))

screen.exitonclick()