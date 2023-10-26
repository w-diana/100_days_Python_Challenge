import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
count = 0
states = pandas.read_csv("50_states.csv")
state_list = states.state.to_list()
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

while game_is_on:
    answer_state = screen.textinput(title=f"{count}/50 State's Correct", prompt="what's another state's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in state_list:
        # x = states[states.state == answer_state].x.to_list()
        # y = states[answer_state == states.state].y.to_list()
        state_data = states[states.state == answer_state]
        pen.goto(x=int(state_data.x.iloc[0]), y=int(state_data.y.iloc[0]))
        pen.write(answer_state.title(), align="center", font=("Courier", 9, "normal"))
        count += 1
        state_list.remove(answer_state)

    if count == 50:
        game_is_on = False

# states not guessed by the user
pandas.DataFrame(state_list).to_csv("state_missed.csv")

# how to get the coordinates by clicking o the map
# def get_mouse_click_coor(x,y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()