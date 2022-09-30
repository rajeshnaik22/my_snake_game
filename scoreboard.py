from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.goto(0,270)
        self.penup()
        self.color("white")
        self.refresh()
        self.hideturtle()

    def increment(self):
        self.score +=1
        self.clear()
        self.refresh()

    def refresh(self):
        self.write(f"Score is {self.score}",align="center",font=("Arial",24,"normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial",24,"normal"))
        self.save_score()

    def save_score(self):
        with open("scores.text", mode="a") as file:
            file.write(f"\nYour score was {self.score}")


    