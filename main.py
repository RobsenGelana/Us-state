import turtle
import pandas as pd 


screen = turtle.Screen()
screen.title('U.S. State Game')
image = 'blank_states_img.gif'
turtle.addshape(image)
turtle.shape(image)



FONT = ('arial',8,'bold')

data = pd.read_csv('50_states.csv')
state_data = data['state']
class Map:
    def __init__(self) -> None:
        self.user_guessed = []
    def user_input(self):
        user_guess = screen.textinput(title=f"{len(self.user_guessed)}/ {len(state_data)} State Correct", prompt="What's other state name? ").title()
        for state in state_data:
            if user_guess in state:
                self.user_guessed.append(user_guess)
                df = data[data['state'] == f"{user_guess}"]
                x_pos = int(df['x'])
                y_pos = int(df['y'])
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                t.setposition(x_pos, y_pos)
                t.write(f'{user_guess}', font=FONT)
                

map = Map()


game_on = True
while game_on:
    map.user_input()