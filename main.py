import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. State Game')
# turtle.setup(width=600, height=600)
image = 'blank_states_img.gif'
turtle.addshape(image)
turtle.shape(image)

user_guess = screen.textinput(title='Guess the state', prompt="What's other state name? ")
