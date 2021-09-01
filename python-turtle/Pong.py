import turtle
import time
import random

win_score = 10
wait = True
speed = 15
length = 800
width = 350
mode = 1
delay_time = 0.01
min_pos = 250
screen = turtle.Screen()
screen.title('Pong Game')
screen.setup(length, width)
screen.bgcolor('#000011')
screen.tracer(0)
pen = turtle.Turtle()
pen.hideturtle()
pen2 = turtle.Turtle()
pen2.color('white')
pen2.hideturtle()
score_pen1 = turtle.Turtle()
score_pen1.penup()
score_pen1.hideturtle()
score_pen1.color('white')
score_pen2 = turtle.Turtle()
score_pen2.penup()
score_pen2.hideturtle()
score_pen2.color('white')
score_pen1.setpos(-length / 4, width / 2 - 40)
score_pen2.setpos(length / 4, width / 2 - 40)

bat1 = turtle.Turtle()
bat1.color('#00DDFF')
bat1.shape('square')
bat1.shapesize(7, 1, 2)
bat1.penup()
bat1.setpos(-length / 2 + 15, -width / 2 + 80)
bat2 = turtle.Turtle()
bat2.color('#00DDFF')
bat2.shape('square')
bat2.shapesize(7, 1, 2)
bat2.penup()
bat2.setpos(length / 2 - 22, width / 2 - 75)

ball = turtle.Turtle()
ball.penup()
ball.color('#FFFFFF')
ball.shape('circle')
ball.shapesize(1.7, 1.7, 1)
ball.seth(45)

ball.hideturtle()
bat2.hideturtle()
bat1.hideturtle()


def up_p1():
    if wait is False:
        if bat1.ycor() <= width / 2 - 80:
            bat1.sety(bat1.ycor() + speed)


def down_p1():
    if wait is False:
        if bat1.ycor() >= (-width / 2 + 80):
            bat1.sety(bat1.ycor() - speed)


def up_p2():
    if wait is False:
        if mode == 2:
            if bat2.ycor() <= width / 2 - 80:
                bat2.sety(bat2.ycor() + speed)


def down_p2():
    if wait is False:
        if mode == 2:
            if bat2.ycor() >= (-width / 2 + 80):
                bat2.sety(bat2.ycor() - speed)


def waiting():
    global wait
    if wait:
        wait = False
        print('Game is Resumed')
        pen2.clear()
    else:
        wait = True
        print('Game is Paused')
        pen2.penup()
        pen2.clear()
        pen2.goto(-80, 40)
        pen2.write('( Game Paused )', font=('Arial', 15, 'normal'))


def finish():
    print('Application Quitting. Thank You For Playing :)))')
    screen.bye()
    exit(0)


screen.onkeypress(up_p1, 'Up')
screen.onkeypress(down_p1, 'Down')
screen.onkeyrelease(up_p1, 'Up')
screen.onkeyrelease(down_p1, 'Down')
screen.onkeypress(up_p1, 'w')
screen.onkeypress(down_p1, 's')
screen.onkeyrelease(up_p1, 'w')
screen.onkeyrelease(down_p1, 's')
screen.onkeypress(up_p2, 'i')
screen.onkeypress(down_p2, 'k')
screen.onkeyrelease(up_p2, 'i')
screen.onkeyrelease(down_p2, 'k')
screen.onkey(waiting, 'space')
screen.onkey(finish, 'Escape')
screen.listen()
ball.seth(ball.towards(bat1))


def ball_calculate_trajectory():
    h = -999
    if ball.heading() <= 90 or ball.heading() >= 270:
        h = ball.heading()
        pen.penup()
        pen.pencolor('orange')
        pen.goto(ball.pos())
        pen.seth(h)
        # pen.pendown ()
    # time.sleep(1)
    if h != -999:
        while pen.xcor() <= length / 2:
            pen.forward(10)
        return pen.ycor()


def end_screen(message):
    global wait
    wait = True
    pen.clear()
    score_pen2.clear()
    score_pen1.clear()
    ball.hideturtle()
    bat1.hideturtle()
    bat2.hideturtle()
    pen2.clear()
    pen2.penup()
    pen2.goto(-130, 0)
    pen2.write(message, font=('Comic Sans Ms', 20, 'normal'))
    screen.update()
    time.sleep(3)
    pen2.clear()
    welcome_screen()
    screen.onclick(mode_select)
    screen.mainloop()


def main_game():
    global min_pos, delay_time, win_score, wait, mode
    if mode == 1:
        pen2.penup()
        pen2.goto(-190, 0)
        pen2.write('<--- Player', font=('Lucida Console', 15, 'normal'))
        pen2.goto(70, 0)
        pen2.write('Machine --->', font=('Lucida Console', 15, 'normal'))
        pen2.goto(-350, -50)
        pen2.write('[Press Space Bar to start]', font=('Lucida Console', 15, 'normal'))
    elif mode == 2:
        pen2.penup()
        pen2.goto(-190, 0)
        pen2.write('<--- Player 1', font=('Lucida Console', 15, 'normal'))
        pen2.goto(40, 0)
        pen2.write('Player 2 --->', font=('Lucida Console', 15, 'normal'))
        pen2.goto(-350, -50)
        pen2.write('[Press Space Bar to start]', font=('Lucida Console', 15, 'normal'))
    elif mode == 3:
        pen2.penup()
        pen2.goto(-190, 0)
        pen2.write('<--- Player', font=('Lucida Console', 15, 'normal'))
        pen2.goto(70, 0)
        pen2.write('Machine --->', font=('Lucida Console', 15, 'normal'))
        pen2.goto(-350, -50)
        pen2.write('[Press Space Bar to start]', font=('Lucida Console', 15, 'normal'))
    wait = True
    bat1.setpos(-length / 2 + 15, -width / 2 + 80)
    bat2.setpos(length / 2 - 22, width / 2 - 75)
    ball.setpos(0, 0)
    ball.seth(ball.towards(bat1.pos()))
    bat1_score = 0
    bat2_score = 0
    pos = 0
    ball_speed = 5
    prev_time1 = time.time()
    prev_pos1 = bat1.ycor()
    velocity1 = 0
    prev_time2 = time.time()
    prev_pos2 = bat2.ycor()
    velocity2 = 0
    screen.setup(length, width)
    ball.showturtle()
    bat1.showturtle()
    bat2.showturtle()
    pen.pensize(10)
    pen.color('#777777')
    pen.penup()
    pen.goto(0, width / 2)
    pen.seth(270)
    pen.pendown()
    pen.goto(0, -width / 2)
    pen.penup()
    while True:
        if wait is False:
            score_pen1.clear()
            score_pen1.write(bat1_score, font=('Arial', 25, 'normal'))
            score_pen2.clear()
            score_pen2.write(bat2_score, font=('Arial', 25, 'normal'))
            # print (bat1_score, '\t', bat2_score)
            ball.forward(ball_speed)  # ball movement
            if ball.xcor() > length + 50:
                ball.setpos(0, random.randint(-width / 2, width / 2))
                bat1_score += 1
                if delay_time >= 0.001:
                    delay_time -= 0.0004
            if ball.xcor() < -length - 50:
                ball.setpos(0, random.randint(-width / 2, width / 2))
                bat2_score += 1
                if mode == 2 and delay_time >= 0.001:
                    delay_time -= 0.0002
                elif mode == 3 and delay_time >= 0.001:
                    delay_time -= 0.0001
            # bat2 movement
            if mode == 1 or mode == 3:
                if ball.xcor() >= min_pos:
                    if ball.heading() <= 90 or ball.heading() >= 270:
                        pos = ball_calculate_trajectory()
                        if bat2.ycor() > pos + 10:
                            if not bat2.ycor() - 70 < -width / 2:
                                bat2.sety(bat2.ycor() - speed / 3)
                        elif bat2.ycor() < pos - 10:
                            if not bat2.ycor() + 70 > width / 2:
                                bat2.sety(bat2.ycor() + speed / 3)
            if time.time() - prev_time1 >= 0.2:
                velocity1 = int(
                    (((bat1.ycor() - prev_pos1)) / (time.time() - prev_time1)) / 5)
                prev_time1 = time.time()
                prev_pos1 = bat1.ycor()
            if time.time() - prev_time2 >= 0.2:
                velocity2 = int(
                    (((bat2.ycor() - prev_pos2)) / (time.time() - prev_time2)) / 5)
                prev_time2 = time.time()
                prev_pos2 = bat2.ycor()
            # wall collisions
            if ball.ycor() >= width / 2 - 20:
                ball.sety(width / 2 - 20)
                ball.seth(360 - ball.heading() % 360)
            if ball.ycor() <= -width / 2 + 20:
                ball.sety(-width / 2 + 20)
                ball.seth(360 - ball.heading() % 360)
            # wall collisions end
            # bat collisions
            if ball.xcor() >= length / 2 - 40 and ball.xcor() <= length / 2 - 20:
                if ball.ycor() > bat2.ycor() - 80 and ball.ycor() < bat2.ycor() + 80:
                    if ball.heading() <= 90:
                        ball.seth(180 - ball.heading() % 360 + velocity2 / 6)
                        if (ball.heading() >= 80 and ball.heading() <= 110):
                            ball.seth(ball.heading() - velocity2 / 6)
                        ball.forward(ball_speed * 5)
                    else:
                        ball.seth(180 + 360 - ball.heading() % 360 + velocity2 / 6)
                        if (ball.heading() >= 250 and ball.heading() <= 300):
                            ball.seth(ball.heading() - velocity2 / 6)
                        ball.forward(ball_speed * 5)
            if ball.xcor() <= -length / 2 + 40 and ball.xcor() >= -length / 2 + 20:
                if ball.ycor() > bat1.ycor() - 80 and ball.ycor() < bat1.ycor() + 80:
                    if ball.heading() <= 180:
                        ball.seth(180 - ball.heading() % 360 + velocity1 / 6)
                        if (ball.heading() >= 80 and ball.heading() <= 110):
                            ball.seth(ball.heading() - velocity1 / 6)
                        ball.forward(ball_speed * 5)
                    else:
                        ball.seth(180 + 360 - ball.heading() % 360 + velocity1 / 6)
                        if (ball.heading() >= 250 and ball.heading() <= 300):
                            ball.seth(ball.heading() - velocity1 / 6)
                        ball.forward(ball_speed * 5)
            # bat collisions
            if bat2_score % win_score == 0 and bat2_score > 0:
                bat1_score = 0
                bat2_score = 0
                if mode == 1:
                    print('Machine Wins!')
                    end_screen('Machine has won!!!')
                elif mode == 2:
                    print('Player 2 Wins')
                    end_screen('Player 2 has won!!!')
            elif bat1_score % win_score == 0 and bat1_score > 0:
                bat1_score = 0
                bat2_score = 0
                if mode == 1:
                    print('Player Wins!')
                    end_screen('You have won!!!')
                elif mode == 2:
                    print('Player 1 Wins')
                    end_screen('Player 1 has Won!!!')
        screen.update()
        time.sleep(delay_time)


def rect(t, l, b):
    t.pendown()
    for i in range(2):
        t.forward(l)
        t.right(90)
        t.forward(b)
        t.right(90)


def welcome_screen():
    print('Welcome to the Classic Pong Game')
    print('The Tutorial....\n')
    print('*' * 50)
    print('For 1 player mode : ')
    print('use arrow keys or w,s for movement of ur bat (left screen)')
    print('the velocity with which you strike the ball affects its angle too\n')
    print('For 2 player mode : ')
    print('for left player : w,s / (arrows)')
    print('for right player : i,k for movement\n')
    print('*' * 50)
    print('Press space bar to pause the game anytime')
    print('Press escape to exit the game anytime')
    print('Thank you for choosing to play Pong game :)))')
    print('The player who reaches 10 scores first wins the game!')
    screen.setup(500, 400)
    pen.penup()
    pen.goto(-100, 50)
    pen.color('white')
    pen.write('PONG', font=('jokerman', 50, 'normal'))
    pen.pensize(2)
    pen.goto(-150, 20)
    pen.seth(0)
    rect(pen, 300, 50)
    pen.penup()
    pen.goto(-150, -60)
    pen.seth(0)
    pen.pendown()
    rect(pen, 300, 50)
    pen.penup()
    pen.goto(-110, -20)
    pen.write('1 Player (machine)', font=('comic sans ms', 20, 'normal'))
    pen.goto(-100, -100)
    pen.write('2 Player (human)', font=('comic sans ms', 20, 'normal'))
    screen.update()


def level_screen():
    pen.clear()
    pen.penup()
    pen.goto(-205, 120)
    pen.write('Select the Difficulty', font=('ravie', 22, 'normal'))
    pen.goto(-150, 80)
    pen.pendown()
    rect(pen, 300, 40)
    pen.penup()
    pen.goto(-150, 20)
    pen.pendown()
    rect(pen, 300, 40)
    pen.penup()
    pen.goto(-150, -40)
    pen.pendown()
    rect(pen, 300, 40)
    pen.penup()
    pen.goto(-150, -100)
    pen.pendown()
    rect(pen, 300, 40)
    pen.penup()
    pen.goto(-35, 45)
    pen.write('Easy', font=('comic sans ms', 20, 'normal'))
    pen.goto(-55, -17)
    pen.write('Medium', font=('comic sans ms', 20, 'normal'))
    pen.goto(-35, -77)
    pen.write('Hard', font=('comic sans ms', 20, 'normal'))
    pen.goto(-65, -137)
    pen.write('Unlimited', font=('comic sans ms', 20, 'normal'))
    screen.update()
    screen.onclick(level_select)
    screen.mainloop()


def level_select(x, y):
    global min_pos, delay_time, win_score, mode
    if x >= -150 and x <= 150:
        if y <= 80 and y >= 40:
            min_pos = length / 2 - 100
            delay_time = 0.006
            win_score = 10
            pen.clear()
            main_game()
        elif y <= 20 and y >= -20:
            min_pos = length / 2 - 200
            delay_time = 0.005
            win_score = 10
            pen.clear()
            main_game()
        elif y <= -40 and y >= -80:
            min_pos = length / 2 - 300
            delay_time = 0.002
            win_score = 10
            pen.clear()
            main_game()
        elif y <= -100 and y >= -140:
            min_pos = length / 2 - 200
            mode = 3  # special unlimited mode
            delay_time = 0.005
            win_score = 999
            pen.clear()
            main_game()


def mode_select(x, y):
    global mode, delay_time
    if y >= -30 and y <= 20:
        if x >= -150 and x <= 150:
            mode = 1
            pen.clear()
            level_screen()
    elif y >= -110 and y <= -60:
        if x >= -150 and x <= 150:
            mode = 2
            delay_time = 0.007
            pen.clear()
            main_game()


welcome_screen()
screen.onclick(mode_select)
screen.mainloop()
