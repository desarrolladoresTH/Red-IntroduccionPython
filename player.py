from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")#forma tortuga
        self.penup()
        self.shapesize(2,2)#dimensionesTortuga
        self.setheading(90)#orientacionTortuga
        self.goto(0,-200)#usar goto para movimiento, crear funciones
        self.color("turquoise")
        self.missiles = []



    def turn_right(self):
        new_heading = self.heading() - 30
        self.setheading(new_heading)

    def turn_left(self):
        new_heading = self.heading() + 30
        self.setheading(new_heading)

    def create_missile(self):
        new_missile = Turtle()
        new_missile.penup()
        new_missile.goto(0,-200)
        new_missile.color("green")
        new_missile.setheading(self.heading())
        self.missiles.append(new_missile)



    def fire(self):
        for m in self.missiles:
            m.forward(10)



