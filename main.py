import turtle as t
import random
import tkinter as tk

screen = t.Screen()
screen.setup(400, 400)
icon = tk.PhotoImage(file="snakeicon.png")
t.title("AsserSnake")
screen._root.iconphoto(True, icon)
screen.cv._rootwindow.resizable(False, False)
player = t.Turtle()
player.width(6)
player.color("green")
player.shape("square")
player.penup()
gameover = t.Turtle()
gameover.color("red")
gameover.hideturtle()
gameover.penup()
gameover.goto(0, 30)
dx, dy = 20, 0

food = t.Turtle()
food.shape("square")
food.color("red")
food.width(3)
food.penup()
food.goto(random.randint(-160, 160), random.randint(-160, 160))
gamerun = True
score = t.Turtle()
score.color("black")
score.penup()
score.hideturtle()
score.goto(0, 150)
restartbtn = t.Turtle()
restartbtn.hideturtle()
restartbtn.penup()
restartbtn.color("black")
restartbtn.goto(0, 0)

body = []
scorecount = 0

def grow():
    newbody = t.Turtle()
    newbody.shape("square")
    newbody.color("green")
    newbody.penup()
    newbody.width(3)
    newbody.goto(0, 0)
    body.append(newbody)

def up():
    global dx, dy
    dx, dy = 0, 20

def down():
    global dx, dy
    dx, dy = 0, -20

def left():
    global dx, dy
    if dx == 0:
        dx, dy = -20, 0

def right():
    global dx, dy
    if dx == 0:
        dx, dy = 20, 0

def game_over():
    global gamerun
    gamerun = False
    gameover.write("Game over", font=("Arial", 50, "normal"), align="center")
    restartbtn.write("[ Restart ]", font=("Arial", 25, "normal"), align="center")

def move():

    global gamerun, oldx, oldy, dx, dy, scorecount
    if not gamerun:
     return

    oldx = player.xcor()
    oldy = player.ycor()

    player.goto(oldx + dx, oldy + dy)

    if player.distance(food) < 20:
        food.goto(random.randint(-160, 160), random.randint(-160, 160))
        scorecount += 1
        grow()

    for i in range(len(body)-1, 0, -1):
        body[i].goto(body[i-1].xcor(), body[i-1].ycor())

    if len(body) > 0:
        body[0].goto(oldx, oldy)

    if player.xcor() > 180 or player.xcor() < -180 or player.ycor() > 180 or player.ycor() < -180:
        game_over()
        return

    for colide in body:
        if player.distance(colide) < 8:
            game_over()
            return

    if len(body) == 10:
        for this in range(5):
            body[0].hideturtle()
            body.pop(0)

    if len(body) == 20:
        for this in range(10):
            body[0].hideturtle()
            body.pop(0)

    if len(body) == 30:
        for this in range(20):
            body[0].hideturtle()
            body.pop(0)

    if len(body) == 40:
        for this in range(30):
            body[0].hideturtle()
            body.pop(0)

    if len(body) == 50:
        for this in range(40):
            body[0].hideturtle()
            body.pop(0)

    screen.ontimer(move, 80)

    score.clear()
    score.write("Score: " + str(scorecount), font=("Arial", 12, "normal"), align="center")

def restart(x, y):
    global dx, dy, body, scorecount, gamerun
    if -80 < x < 80 and -30 < y < 30:
        gamerun = True
        dx, dy = 20, 0
        scorecount = 0
        for every in body:
            every.hideturtle()
        player.goto(0, 0)
        food.goto(random.randint(-160, 160), random.randint(-160, 160))
        body.clear()
        gameover.clear()
        restartbtn.clear()
        move()

screen.listen()
screen.onkey(up, "w")
screen.onkey(down, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")

move()
screen.onclick(restart)
screen.mainloop()
