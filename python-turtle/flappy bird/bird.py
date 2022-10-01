import turtle
import random
import time
 
print('Welcome to Flappy Bird')
print('Press UP arrow or w to jump')
print('Press Space Bar to pause / play')
print('Press Esc to exit anytime')
 
try:
    f = open('flappy_bird.txt', 'x')
    f.close()
    f = open('flappy_bird.txt', 'w')
    f.write('0')
    f.close()
except FileExistsError:
    pass
 
bird_jump_time = time.time()
bird_jump = False
bird_animation_time = time.time()
bird_animation_index = 0
 
wait = False
game_start = False
 
score = 0
real_score = 0
 
screen = turtle.Screen()
screen.setup(450, 600)
screen.title('Flappy Bird')
screen.bgpic('bg2.gif')
screen.tracer(0)
screen.register_shape('ground1.gif')
screen.register_shape('heading1.gif')
screen.register_shape('bird_down.gif')
images = ('bird1.gif', 'bird2.gif', 'bird3.gif', 'bird4.gif')
for i in images:
    screen.register_shape(i)
 
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.pencolor('#111111')
pen.fillcolor('#FF3333')
pen.pensize(3)
 
t = turtle.Turtle()
t.penup()
t.hideturtle()
 
score_pen = turtle.Turtle()
score_pen.penup()
score_pen.hideturtle()
score_pen.pencolor('brown')
 
heading = turtle.Turtle()
heading.penup()
heading.goto(-50, 150)
heading.shape('heading1.gif')
 
bird = turtle.Turtle()
wall_a1 = turtle.Turtle()
wall_a2 = turtle.Turtle()
wall_b1 = turtle.Turtle()
wall_b2 = turtle.Turtle()
ground = turtle.Turtle()
ground.shape('ground1.gif')
ground.penup()
ground.setpos(0, -260)
bird.penup()
bird.goto(-150, -150)
wall_a1.pencolor('brown')
wall_a2.pencolor('brown')
wall_b1.pencolor('brown')
wall_b2.pencolor('brown')
wall_a1.pensize(3)
wall_a2.pensize(3)
wall_b1.pensize(3)
wall_b2.pensize(3)
wall_a1.penup()
wall_a2.penup()
wall_b1.penup()
wall_b2.penup()
wall_a1.hideturtle()
wall_a2.hideturtle()
wall_b1.hideturtle()
wall_b2.hideturtle()
 
gx = 0
x1 = 700
x2 = 1050
y1 = random.randint(100, 300)
y2 = 600 - y1 - 150
y3 = random.randint(100, 300)
y4 = 600 - y3 - 150
 
 
def rect(t, l, b):
    t.fillcolor('#00CC00')
    t.pencolor('#223311')
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(l)
        t.right(90)
        t.forward(b)
        t.right(90)
    t.end_fill()
    t.penup()
 
 
def up():
    global bird_jump, bird_jump_time, game_start
    if game_start and wait is False:
        bird_jump = True
        bird_jump_time = time.time()
        bird.sety(bird.ycor() + 10)
 
 
def exit_game():
    screen.bye()
    exit(0)
 
 
def pause():
    global wait
    if wait:
        t.clear()
        wait = False
    elif wait is False:
        wait = True
        t.goto(-80, -280)
        t.write('Game Paused', font=('Comic Sans Ms', 20, 'normal'))
 
 
screen.onkeypress(up, 'Up')
screen.onkeyrelease(up, 'Up')
screen.onkeypress(up, 'w')
screen.onkeyrelease(up, 'w')
screen.onkey(pause, 'space')
screen.onkey(exit_game, 'Escape')
 
screen.listen()
 
 
def replay_check(x, y):
    if x <= 50 and x >= -50:
        if y <= -150 and y >= -180:
            welcome_screen()
 
 
def end_screen():
    bird.shape('bird_down.gif')
    medals = 'none'
    score_pen.clear()
    global real_score, high_score, wait
    if real_score > int(high_score):
        high_score = real_score
        f = open('flappy_bird.txt', 'w')
        f.write(str(real_score))
        f.close()
    while bird.ycor() >= -170:
        bird.goto(bird.xcor(), bird.ycor() - 5)
        screen.update()
        time.sleep(0.01)
    bird.hideturtle()
 
    if real_score >= 25:
        medals = 'bronze !'
    if real_score >= 50:
        medals = 'silver !!'
    if real_score >= 100:
        medals = 'gold !!!'
 
    pen.goto(-200, 200)
    pen.fillcolor('brown')
    pen.pencolor('black')
    box_option_rect(pen, 400, 50)
    pen.goto(-140, 150)
    pen.pencolor('white')
    pen.write('Game Over', font=('ravie', 30, 'normal'))
 
    pen.goto(-150, 100)
    pen.fillcolor('yellow')
    pen.pencolor('brown')
    box_option_rect(pen, 300, 200)
    pen.goto(-100, 30)
    pen.write('Your Score : ', font=('Comic Sans Ms', 20, 'normal'))
    pen.goto(70, 30)
    pen.write(str(real_score), font=('Comic Sans Ms', 20, 'normal'))
    pen.goto(-100, -20)
    pen.write('Best Score : ', font=('Comic Sans Ms', 20, 'normal'))
    pen.goto(70, -20)
    pen.write(str(high_score), font=('Comic Sans Ms', 20, 'normal'))
    pen.goto(-100, -70)
    pen.write('Medals : ', font=('Bauhaus 93', 20, 'normal'))
    pen.goto(20, -70)
    pen.write(medals, font=('Comic Sans Ms', 20, 'normal'))
 
    pen.goto(-50, -150)
    pen.fillcolor('#FF3333')
    pen.pencolor('black')
    box_option_rect(pen, 100, 30)
    pen.pencolor('white')
    pen.goto(-47, -153)
    box_option_rect(pen, 94, 24)
    pen.goto(-29, -179)
    pen.write('Replay', font=('Comic Sans Ms', 15, 'normal'))
    screen.onclick(replay_check)
    screen.mainloop()
 
 
def main_game():
    global score, real_score, high_score, wait
    score = 0
    real_score = 0
    delay_time = 0.01
    heading.hideturtle()
    bird.showturtle()
    global bird_jump, bird_animation_time, bird_animation_index, y1, y2, y3, y4, x1, x2, gx
    score_pen.goto(-10, 250)
    score_pen.write(real_score, font=('Comic Sans Ms', 20, 'normal'))
    screen.update()
    while True:
        score_pen.clear()
        score_pen.write(real_score, font=('Comic Sans Ms', 20, 'normal'))
        if wait is False:
            delay_time = 0.01 - real_score * 0.0001
            real_score = int(score / 15)
            ground.clear()
            ground.setpos(gx, -260)
            gx -= 4.5
            if gx <= -20:
                gx = 20
            if bird.xcor() <= x1 + 100 + 30 and bird.xcor() >= x1 - 30:
                if bird.ycor() >= 300 - y1 - 20 or bird.ycor() <= 300 - y1 - 150 + 20:
                    end_screen()
                    # screen.bye ()
            if bird.xcor() <= x2 + 100 + 30 and bird.xcor() >= x2 - 30:
                if bird.ycor() >= 300 - y3 - 20 or bird.ycor() <= 300 - y3 - 150 + 20:
                    end_screen()
            if bird.ycor() <= -300 + 60 or bird.ycor() >= 300 - 20:
                end_screen()
            if x1 < -150 or x2 < -150:
                if bird.xcor() > x1 + 120 or bird.xcor() > x2 + 120:
                    score += 1
 
            if time.time() - bird_animation_time >= 0.1:
                bird.shape(images[bird_animation_index])
                if bird_animation_index == 3:
                    bird_animation_index = 0
                else:
                    bird_animation_index += 1
                bird_animation_time = time.time()
            if time.time() - bird_jump_time >= 0.1:
                bird_jump = False
            if bird_jump is False:
                bird.sety(bird.ycor() - 3)
            if bird_jump:
                bird.sety(bird.ycor() + 2)
            wall_a1.clear()
            wall_a2.clear()
            wall_b1.clear()
            wall_b2.clear()
            x1 -= 5
            x2 -= 5
            if x1 <= -350:
                x1 = 350
                y1 = random.randint(100, 300)
                y2 = 600 - y1 - 150
            if x2 <= -350:
                x2 = 350
                y3 = random.randint(100, 300)
                y4 = 600 - y3 - 150
 
            wall_a1.goto(x1, 300)
            rect(wall_a1, 100, y1 - 50)
            wall_a1.seth(0)
            wall_a1.goto(x1 - 10, 300 - y1 + 50)
            rect(wall_a1, 120, 50)
            wall_a2.goto(x1, -210)
            wall_a2.seth(90)
            rect(wall_a2, y2 - 50 - 90, 100)
            wall_a2.goto(x1 - 10, -(300 - y2 + 50))
            rect(wall_a2, 50, 120)
 
            wall_b1.goto(x2, 300)
            rect(wall_b1, 100, y3 - 50)
            wall_b1.seth(0)
            wall_b1.goto(x2 - 10, 300 - y3 + 50)
            rect(wall_b1, 120, 50)
            wall_b2.goto(x2, -210)
            wall_b2.seth(90)
            rect(wall_b2, y4 - 50 - 90, 100)
            wall_b2.goto(x2 - 10, -(300 - y4 + 50))
            rect(wall_b2, 50, 120)
 
            time.sleep(delay_time)
            screen.update()
 
 
def box_option_rect(t, l, b):
    t.begin_fill()
    t.pendown()
    for i in range(2):
        t.forward(l)
        t.right(90)
        t.forward(b)
        t.right(90)
    t.end_fill()
    t.penup()
 
 
def main_game_start(x, y):
    global game_start
    if x >= -140 and x <= -40:
        if y >= -180 and y <= -150:
            game_start = True
            pen.clear()
            bird.goto(-150, 150)
            heading.hideturtle()
            main_game()
    elif x >= 40 and x <= 140:
        if y >= -180 and y <= -150:
            pen.goto(-100, 50)
            pen.pencolor('brown')
            pen.fillcolor('yellow')
            box_option_rect(pen, 200, 100)
            pen.goto(-80, -10)
            pen.write('High Score : ', font=('Comic Sans Ms', 15, 'bold'))
            pen.goto(50, -10)
            pen.write(high_score, font=('Comic Sans Ms', 15, 'bold'))
 
 
def welcome_screen():
    global high_score
    f = open('flappy_bird.txt', 'r')
    high_score = f.read()
    f.close()
    global x1, x2
    x1 = 350
    x2 = 700
    score_pen.clear()
    pen.clear()
    wall_a1.clear()
    wall_a2.clear()
    wall_b1.clear()
    wall_b2.clear()
    global game_start
    game_start = False
    dir = +1
    gx = 0
    global bird_animation_time, bird_animation_index
    bird.setpos(140, 150)
    bird.showturtle()
    heading.showturtle()
    heading.setpos(-50, 150)
    pen.pencolor('black')
    pen.fillcolor('#FF3333')
    pen.goto(-140, -150)
    box_option_rect(pen, 100, 30)
    pen.goto(40, -150)
    box_option_rect(pen, 100, 30)
    pen.pencolor('white')
    pen.goto(-137, -153)
    box_option_rect(pen, 94, 24)
    pen.goto(43, -153)
    box_option_rect(pen, 94, 24)
    pen.pencolor('white')
    pen.goto(-124, -179)
    pen.write('START', font=('Comic Sans Ms', 15, 'normal'))
    pen.goto(56, -179)
    pen.write('SCORE', font=('Comic Sans Ms', 15, 'normal'))
    pen.goto(-10, 250)
 
    while True:
        ground.clear()
        ground.setpos(gx, -260)
        gx -= 4.5
        if gx <= -20:
            gx = 20
        if time.time() - bird_animation_time >= 0.1:
            bird.shape(images[bird_animation_index])
            if bird_animation_index == 3:
                bird_animation_index = 0
            else:
                bird_animation_index += 1
            bird_animation_time = time.time()
        if bird.ycor() <= 140 or bird.ycor() >= 160:
            dir *= -1
        bird.sety(bird.ycor() + dir / 2)
        heading.sety(heading.ycor() + dir / 2)
        screen.update()
        time.sleep(0.01)
        screen.onclick(main_game_start)
 
 
# main_game code
welcome_screen()
 
# screen.mainloop ()