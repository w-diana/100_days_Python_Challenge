from turtle import Turtle, Screen, colormode
import random
import colorgram

# # This code extracts a color list from an image.
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(56, 107, 149), (226, 133, 56), (196, 146, 172), (234, 201, 101), (145, 82, 54), (139, 179, 207), (228, 236, 234), (233, 226, 196), (139, 131, 73), (141, 100, 129), (131, 184, 132), (218, 94, 60), (187, 78, 128), (49, 156, 195), (65, 156, 88), (235, 224, 231), (60, 141, 107), (212, 178, 193), (24, 68, 110), (115, 124, 147), (229, 174, 166), (184, 189, 207), (18, 62, 99), (174, 202, 181), (166, 201, 210), (70, 60, 49), (79, 64, 41)]

tim = Turtle()
tim.hideturtle()
tim.speed("fastest")
colormode(255)

num_of_dots = 10
x_spacing = -300
y_spacing = -300

for _ in range(10):
    for _ in range (10):
        tim.penup()
        tim.color(random.choice(color_list))
        tim.goto(x_spacing, y_spacing)
        tim.dot(50)
        x_spacing += 66
    y_spacing += 66
    x_spacing = -300

screen = Screen()
screen.exitonclick()