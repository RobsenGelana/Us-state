import turtle
import pandas as pd 


screen = turtle.Screen()
screen.title('U.S. State Game')
image = 'blank_states_img.gif'
turtle.addshape(image)
turtle.shape(image)
turtle = turtle.Turtle()


FONT = ('arial',8,'bold')

data = pd.read_csv('50_states.csv')
state_data = data['state']

def user_input():
    user_guess = screen.textinput(title=f" Guess the state", prompt="What's other state name? ").title()
    for state in state_data:
        if user_guess in state:
            df = data[data['state'] == f"{user_guess}"]
            x_pos = int(df['x'])
            y_pos = int(df['y'])
            turtle.hideturtle()
            turtle.penup()
            turtle.setposition(x_pos, y_pos)
            turtle.write(f'{user_guess}', font=FONT)
          

   


game_on = True
while game_on:
    user_input()
