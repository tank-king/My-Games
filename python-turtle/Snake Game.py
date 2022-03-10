import turtle
import time
import random

# snake game
delay_time = 0.05
screen = turtle.Screen ()
screen.setup (500, 600)
screen.bgcolor ('green')
screen.tracer (0)
# snake head
head = turtle.Turtle ()
head.shape ('square')
head.speed (0)
head.shapesize (0.8, 0.8, 1)
head.penup ()
head.direction = 'stop'
head.color ('black')

# food
food = turtle.Turtle ()
food.shape ('circle')
food.color ('red')
food.penup ()
food.setpos (random.randint (-200, -100), random.randint (-250, 250))
food.shapesize (0.8, 0.8, 1)
# body
body = []
# pen for drawing
pen = turtle.Turtle ()
pen.hideturtle ()

score = -1  # global variable for score


def window_setup ():
    global score, body, status, delay_time
    score = 0
    delay_time = 0.05
    head.direction = 'stop'
    pen.penup ()
    pen.pensize (5)
    pen.color ('white')
    pen.goto (-230, -280)
    pen.seth (90)
    pen.pendown ()
    rect (pen, 530, 460)
    pen.penup ()
    pen.goto (-230, 260)
    pen.pendown ()
    pen.write ('Score = ', font = ('Arial', 20, 'normal'))
    pen.penup ()
    pen.goto (-120, 260)
    pen.pendown ()
    pen.write (score, font = ('Arial', 20, 'normal'))
    while True:
        screen.update ()
        main_code ()
        time.sleep (delay_time)


def rect (t, l, b):
    for i in range (2):
        t.forward (l)
        t.right (90)
        t.forward (b)
        t.right (90)


def up ():
    if head.direction == 'down':
        return
    head.direction = 'up'


def down ():
    if head.direction == 'up':
        return
    head.direction = 'down'


def left ():
    if head.direction == 'right':
        return
    head.direction = 'left'


def right ():
    if head.direction == 'left':
        return
    head.direction = 'right'


def main_code ():
    global score, body, delay_time
    if score == 0 and head.distance (food.pos ()) <= 17:
        return
    if head.direction == 'stop':
        return
    if head.direction == 'left':
        head.setx (head.xcor () - 15)
    elif head.direction == 'right':
        head.setx (head.xcor () + 15)
    elif head.direction == 'up':
        head.sety (head.ycor () + 15)
    elif head.direction == 'down':
        head.sety (head.ycor () - 15)
    # food
    if head.distance (food.pos ()) <= 17:
        score += 1
        delay_time -= 0.001
        pen.undo ()
        pen.write (score, font = ('Arial', 20, 'normal'))
        x = random.randint (-screen.window_width () / 2 + 40,
                            screen.window_width () / 2 - 40)
        y = random.randint (-screen.window_width () / 2 + 40,
                            screen.window_width () / 2 - 40)
        food.goto (x, y)
        temp = turtle.Turtle ()
        temp.speed (0)
        temp.shape ('square')
        temp.color ('white')
        temp.penup ()
        temp.shapesize (0.8, 0.8, 1)
        body.append (temp)

    for i in range (len (body) - 1, 0, -1):
        x = body [i - 1].xcor ()
        y = body [i - 1].ycor ()
        body [i].goto (x, y)
    if len (body) > 0:
        x = head.xcor ()
        y = head.ycor ()
        body [0].goto (x, y)
        body [0].color ('black')

    for i in range (len (body) - 1, 0, -1):
        if head.distance (body [i]) <= 10:
            messageDisplay ('Game Over! You Crashed!')

    if head.xcor () >= screen.window_width () / 2 - 20 \
            or head.xcor () <= -screen.window_width () / 2 + 20:
        messageDisplay ('Game Over! You Crashed!')
    elif head.ycor () >= screen.window_height () / 2 - 50 \
            or head.ycor () <= -screen.window_height () / 2 + 20:
        messageDisplay ('Game Over! You Crashed!')


def messageDisplay (message):
    pen.pensize (5)
    pen.penup ()
    pen.setposition (-150, -200)
    pen.pendown ()
    pen.write (message, font = ('ARIAL', 20, 'normal'))
    pen.penup ()
    pen.setpos (-50, 265)
    pen.pendown ()
    pen.write ('Press Enter to exit or click to Replay', font = ('ARIAL', 12, 'normal'))
    screen.onclick (end)
    screen.mainloop ()


def end (x, y):
    global body, delay_time
    delay_time = 0.05
    i = len (body) - 1
    head.clear ()
    food.clear ()
    pen.clear ()
    head.goto (0, 0)
    while i >= 0:
        body [i].ht ()
        body [i].color ('green')
        body [i].goto (1000, 1000)
        del body [i]
        i -= 1
    body = []
    window_setup ()


def EndGame ():
    screen.bye ()
    exit (0)


screen.onkey (up, 'w')
screen.onkey (down, 's')
screen.onkey (left, 'a')
screen.onkey (right, 'd')
screen.onkey (up, 'Up')
screen.onkey (down, 'Down')
screen.onkey (left, 'Left')
screen.onkey (right, 'Right')
screen.onkey (EndGame, 'Return')
screen.listen ()

print ('Welcome to the Snake Game')
print ('To start growing you have to eat at least 2 apples')
print ('If you collide with walls or yourself you will lose the game')
print ('You can press Enter to exit anytime')

window_setup ()
