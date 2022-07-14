from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,200)
        self.score = 0
        self.write_score()



    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("sans", 30, "bold"))


    def increase_score(self):
        self.score+=1
        self.write_score()


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align="center", font=("sans", 30, "bold"))

