import turtle
import pandas as pd 

screen = turtle.Screen()
screen.title('U.S. State Game')
image = 'blank_states_img.gif'
turtle.addshape(image)
turtle.shape(image)

user_guess = screen.textinput(title='Guess the state', prompt="What's other state name? ").title()

data = pd.read_csv('50_states.csv')
state_data = data['state']
x_data = data['x']
y_data = data['y']
