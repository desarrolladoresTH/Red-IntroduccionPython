from turtle import Screen #importa pantalla
from player import Player
from invader import Invader
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(600,600)#tamaño pantalla
#screen.bgcolor("black")#cambia el color del fondo
screen.tracer(0)


player = Player()
invader = Invader()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.turn_right, "Right")#aqui se pueden las teclas fisicas
screen.onkey(player.turn_left, "Left")
screen.onkey(player.create_missile, "space")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    player.fire()
    invader.create_invader()
    invader.move()
    screen.update()


    for i in invader.enemies:
        for m in player.missiles:
            if m.distance(i)<20:
                player.missiles.remove(m)
                invader.enemies.remove(i)
                m.hideturtle()
                i.hideturtle()
                scoreboard.increase_score()

            if m.distance(player)>600:
                player.missiles.remove(m)
                m.hideturtle()

        if i.distance(player)<10:
            scoreboard.game_over()
            game_is_on = False







screen.exitonclick()