
from turtle import Turtle
from get_cords import get_cords



class Text(Turtle):
    states_dictionary = get_cords()
    def __init__(self):
        self.guessed_states = []

        super().__init__()
        self.penup()
        self.hideturtle()

    def move_text(self,user_answer):
        if user_answer.title() in self.guessed_states:
            return "already guessed"


        elif user_answer.title() in self.states_dictionary:
            cords = self.states_dictionary[user_answer.title()]
            x_cord = cords[0]
            y_cord = cords[1]

            self.goto(x_cord, y_cord)
            self.write(user_answer.title(), align="center", font=("Arial", 12, "normal"))
            self.guessed_states.append(user_answer.title())
            return "correct"
        else:
            return "incorrect"
    def you_win(self):
        self.goto(0, -200)
        self.write("You win!", align="center", font=("Arial", 12, "normal"))
