
from turtle import *

from freegames import line

casillas = []

def grid():
    """Dibuja el tablero en el que se va a jugar"""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibuja el primer jugador que es el jugador X con su cambio de color"""
    color("red")
    line(x + 75, y + 75, x + 50, y + 50)
    line(x + 75, y + 50, x + 50, y + 75)


def drawo(x, y):
    """Dibuja el segundo jugador que es el jugador O con su cambio de color"""
    color("blue")
    up()
    goto(x + 70, y + 45)
    down()
    circle(20)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Marca la jugada que hizo el jugador en el cuadro que se la asigno"""
    global casillas
    x = floor(x)
    y = floor(y)
    coor = [x, y]
    player = state["player"]
    draw = players[player]
    if coor not in casillas:
        casillas.append(coor)
        draw(x, y)
        update()
        state["player"] = not player
    else:
        return
        


"""Nos da el tamaño que va a tener el tablero al ser desplegado"""
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
