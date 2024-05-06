import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(700, 510)

turtle.shape(image)

state_data = pandas.read_csv('50_states.csv')

correct_guessed_answer = []
correct_answer = state_data.state.to_list()
state_guessed = 0
game_is_on = True
while game_is_on:
    if state_guessed < 50:
        user_answer = screen.textinput(title=f"{state_guessed}/50 Guess the state",
                                       prompt="What's another state's name?").title()

        if user_answer == "Exit":
            not_guessed_state = [answer for answer in correct_answer if answer not in correct_guessed_answer]
            df = pandas.DataFrame(not_guessed_state)
            df.to_csv('missing_state')
            break

        if user_answer in correct_guessed_answer:
            continue
        elif user_answer in correct_answer:
            text = turtle.Turtle()
            text.speed('fastest')
            text.pu()
            text.ht()
            answer_row = state_data[state_data.state == user_answer]
            x_coor = int(answer_row.x.iloc[0])
            y_coor = int(answer_row.y.iloc[0])
            text.setpos(x_coor, y_coor)
            text.write(f"{user_answer}", align='center', font=('Arial', 8, 'normal'))
            correct_guessed_answer.append(user_answer)
            state_guessed += 1
    else:
        turtle.write("CONGRATULATION! YOU'VE COMPLETED THE GAME!", align='center', font=('Arial', 18, 'bold'))
        game_is_on = False

screen.exitonclick()
