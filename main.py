import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States guessing game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True

states_file = pandas.read_csv("50_states.csv")
states = states_file.state
correct_guesses = []

while len(correct_guesses) < 50:

    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct" , prompt="What's another state's "
                                                                                               "name?").title()
    if answer_state == 'Exit':
        missing_states = []
        for item in states:
            if item not in correct_guesses:
                missing_states.append(item)
        new_df = pandas.DataFrame(missing_states)
        new_df.to_csv("states_to_learn.csv")
        break

    for item in states:
        if item == answer_state:
            correct_guesses.append(answer_state)
            turtle2 = turtle.Turtle()
            turtle2.hideturtle()
            turtle2.penup()
            answer_state_x = float(states_file[states_file['state'] == answer_state]['x'])
            answer_state_y = float(states_file[states_file['state'] == answer_state]['y'])
            # print(answer_state_x)
            # print(answer_state_y)
            turtle2.goto(answer_state_x, answer_state_y)
            turtle2.write(answer_state)


# states_to_learn.csv