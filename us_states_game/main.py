import turtle
from types import NoneType
import pandas

from writer import Writer

data = pandas.read_csv("us_states_game/50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States game")
image = "us_states_game/blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

writer = Writer()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title="State Name",
     prompt="States name",)
    if type(answer_state) == NoneType or answer_state.title() == "Exit":
        break

    answer_state = answer_state.title()
    details = data[data.state==answer_state]
    if not details.empty:
        guessed_states.append( answer_state)
        writer.goto(int( details.x), int(details.y))
        writer.write(answer_state)



