import turtle
from move_text import Text


screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
text = Text()


playing_game = True

while playing_game:

    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
    answer = text.move_text(user_answer=answer_state)

    if answer == "already guessed":
        screen.title("Already guessed")

    elif answer == "correct":
        screen.title("Correct")
        screen.title(f'You guessed {len(text.guessed_states)}/50')

    elif answer == "incorrect":
        screen.title("Incorrect")

    if len(text.guessed_states) == 50:
        text.you_win()
        playing_game = False



turtle.mainloop()

