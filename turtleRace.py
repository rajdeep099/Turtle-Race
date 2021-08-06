import turtle
import time
import random


def newChange():
    pass


# dirt
def dirt():
    turtle.hideturtle()
    turtle.pu()
    turtle.setposition(-400, -130)
    turtle.pd()
    turtle.color("sienna")
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(800)
        turtle.right(90)
        turtle.forward(120)
        turtle.right(90)
    turtle.end_fill()
    turtle.pu()
    turtle.pensize(3)
    turtle.color("black")
    turtle.setposition(-400, -130)
    turtle.pd()
    turtle.forward(800)
    turtle.pensize(1)


# starting line
def starting_line():
    turtle.pu()
    turtle.color("black")
    turtle.pensize(3)
    turtle.setposition(-286, 160)
    turtle.pd()
    turtle.setposition(-286, -50)


# finish line
def finish_line():
    turtle.pu()
    turtle.pensize(1)
    for i in range(21):
        turtle.setposition(300, 160 - (i * 10))
        turtle.pd()
        if i % 2 == 0:
            turtle.color("black")
            turtle.begin_fill()
            for j in range(2):
                turtle.forward(10)
                turtle.right(90)
                turtle.forward(10)
                turtle.right(90)
            turtle.end_fill()
        else:
            turtle.color("white")
            turtle.begin_fill()
            for j in range(2):
                turtle.forward(10)
                turtle.right(90)
                turtle.forward(10)
                turtle.right(90)
            turtle.end_fill()
    time.sleep(1)


def drawOnScreen():
    drawTurtle = turtle.Turtle()
    drawTurtle.pu()
    drawTurtle.setposition(-50, -100)
    drawTurtle.pd()
    drawTurtle.color("white")
    i = 3
    while i > 0:
        drawTurtle.write(i, move=False, align='left', font=('Arial', 200, 'bold'))
        time.sleep(0.5)
        drawTurtle.clear()
        time.sleep(0.5)
        i -= 1


# creating player turtles
def turtles(players):
    global turtle1, turtle2, turtle3, turtle4, playersCount
    playersCount = players
    new()
    if players > 0:
        turtle1 = turtle.Turtle()
        turtle1.hideturtle()
        turtle1.shape(name="turtle")
        turtle1.pu()
        turtle1.setposition(380, -240)
        turtle1.showturtle()
        turtle1.color("red")
        turtle1.setposition(-300, 124-((4-players)*17))
        turtle1.pensize(2)
        turtle1.pd()

    if players > 1:
        turtle2 = turtle.Turtle()
        turtle2.hideturtle()
        turtle2.shape(name="turtle")
        turtle2.pu()
        turtle2.setposition(380, -240)
        turtle2.showturtle()
        turtle2.color("dark blue")
        turtle2.setposition(-300, 80-((4-players)*17))
        turtle2.pensize(2)
        turtle2.pd()

    if players > 2:
        turtle3 = turtle.Turtle()
        turtle3.hideturtle()
        turtle3.shape(name="turtle")
        turtle3.pu()
        turtle3.setposition(380, -240)
        turtle3.showturtle()
        turtle3.color("yellow")
        turtle3.setposition(-300, 36-((4-players)*17))
        turtle3.pensize(2)
        turtle3.pd()

    if players > 3:
        turtle4 = turtle.Turtle()
        turtle4.hideturtle()
        turtle4.shape(name="turtle")
        turtle4.pu()
        turtle4.setposition(380, -240)
        turtle4.showturtle()
        turtle4.color("purple")
        turtle4.setposition(-300, -8.5-((4-players)*17))
        turtle4.pensize(2)
        turtle4.pd()

    time.sleep(1)
    drawOnScreen()

    win = 0
    while True:
        if players > 0:
            turtle1.forward(random.randint(1, 10))
            if turtle1.xcor() >= 290:
                win = 1
                break
        if players > 1:
            turtle2.forward(random.randint(1, 10))
            if turtle2.xcor() >= 290:
                win = 2
                break
        if players > 2:
            turtle3.forward(random.randint(1, 10))
            if turtle3.xcor() >= 290:
                win = 3
                break
        if players > 3:
            turtle4.forward(random.randint(1, 10))
            if turtle4.xcor() >= 290:
                win = 4
                break
    find_winner(win, players)


# find winner
def find_winner(win, players):
    turtle.pu()
    global state, turtle1, turtle2, turtle3, turtle4
    turtle.setposition(-145, -200)
    turtle.color("white")
    turtle.pd()
    if win == 1:
        turtle.write("RED TURTLE WON !!", move=False, align='left', font=('Arial', 23, 'bold'))
    elif win == 2:
        turtle.write("BLUE TURTLE WON !!", move=False, align='left', font=('Arial', 23, 'bold'))
    elif win == 3:
        turtle.write("YELLOW TURTLE WON !!", move=False, align='left', font=('Arial', 23, 'bold'))
    elif win == 4:
        turtle.write("PURPLE TURTLE WON !!", move=False, align='left', font=('Arial', 23, 'bold'))
    state = "not running"
    time.sleep(2)
    turtle.clear()
    if players > 0:
        turtle1.clear()
        turtle1.hideturtle()
    if players > 1:
        turtle2.clear()
        turtle2.hideturtle()
    if players > 2:
        turtle3.clear()
        turtle3.hideturtle()
    if players > 3:
        turtle4.clear()
        turtle4.hideturtle()
    new()


def buttons():
    global turtleTwo, turtleThree, turtleFour, state
    turtle.pensize(3)

    # player images
    turtleTwo = turtle.Turtle()
    turtleTwo.hideturtle()
    turtleTwo.speed(0)
    screen = turtle.Screen()
    _2P = "Images//two.gif"
    screen.addshape(_2P)
    turtleTwo.shape(_2P)
    turtleTwo.pu()
    turtleTwo.setposition(-248, 115)
    turtleTwo.showturtle()

    turtleThree = turtle.Turtle()
    turtleThree.hideturtle()
    turtleThree.speed(0)
    screen = turtle.Screen()
    _3P = "Images//three.gif"
    screen.addshape(_3P)
    turtleThree.shape(_3P)
    turtleThree.pu()
    turtleThree.setposition(162, 115)
    turtleThree.showturtle()

    turtleFour = turtle.Turtle()
    turtleFour.hideturtle()
    turtleFour.speed(0)
    screen = turtle.Screen()
    _4P = "Images//four.gif"
    screen.addshape(_4P)
    turtleFour.shape(_4P)
    turtleFour.pu()
    turtleFour.setposition(-43, -25)
    turtleFour.showturtle()

    # player button outlines
    turtle.pu()
    turtle.setposition(-280, 150)
    turtle.pd()
    for i in range(2):
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(70)
        turtle.right(90)

    turtle.pu()
    turtle.setposition(130, 150)
    turtle.pd()
    for i in range(2):
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(70)
        turtle.right(90)

    turtle.pu()
    turtle.setposition(-75, 10)
    turtle.pd()
    for i in range(2):
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(70)
        turtle.right(90)

    # player buttons text
    turtle.pu()
    turtle.color("white")
    turtle.setposition(-190, 97)
    turtle.pd()
    turtle.write("2", move=False, align='left', font=('Arial', 35, 'bold'))
    turtle.pu()
    turtle.setposition(-200, 87)
    turtle.color("black")
    turtle.pd()
    turtle.write("players", move=False, align='left', font=('Arial', 12, 'bold'))

    turtle.pu()
    turtle.color("white")
    turtle.setposition(222, 97)
    turtle.pd()
    turtle.write("3", move=False, align='left', font=('Arial', 35, 'bold'))
    turtle.pu()
    turtle.setposition(205, 87)
    turtle.color("black")
    turtle.pd()
    turtle.write("players", move=False, align='left', font=('Arial', 12, 'bold'))

    turtle.pu()
    turtle.color("white")
    turtle.setposition(10, -47)
    turtle.pd()
    turtle.write("4", move=False, align='left', font=('Arial', 35, 'bold'))
    turtle.pu()
    turtle.setposition(0, -57)
    turtle.color("black")
    turtle.pd()
    turtle.write("players", move=False, align='left', font=('Arial', 12, 'bold'))


def btnClick(x, y):
    global state
    if state == "not running":
        players = 0
        if (-280 <= x <= -130) and (150 >= y >= 80):
            players = 2
        elif (130 <= x <= 280) and (150 >= y >= 80):
            players = 3
        elif (-75 <= x <= 75) and (10 >= y >= -60):
            players = 4
        state = "running"
        turtles(players)


# new window
def new():
    global state, turtleTwo, turtleThree, turtleFour
    if state == "running":
        turtle.clear()
        turtleTwo.hideturtle()
        turtleThree.hideturtle()
        turtleFour.hideturtle()

    turtle.setup(800, 500)
    turtle.title("Turtle Race")
    turtle.speed(0)
    turtle.Screen().bgpic("Images//grass.png")
    turtle.pu()
    turtle.setposition(-100, 210)
    turtle.pencolor("white")
    turtle.write("TURTLE RACE", move=False, align='left', font=('Arial', 23, 'bold'))
    dirt()
    if state == "not running":
        buttons()
        turtle.onscreenclick(btnClick, 1)
    if state == "running":
        starting_line()
        finish_line()


# main window
if __name__ == '__main__':
    global state
    state = "not running"
    new()

    turtle.mainloop()
