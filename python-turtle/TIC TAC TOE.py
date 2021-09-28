import os
import turtle

# global variables declarations
no_of_moves = 0
turn = 1
mode = 0
player = 'x'
machine = 'o'
winScoreArray = []
board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
# global declarations end here
os.system ('CLS')
move = turtle.Turtle ()
move.hideturtle ()
move.speed (0)
screen = turtle.Screen ()
screen.setup (500, 500)
screen.bgcolor ('black')
move.color ('white')
move.pensize (5)
move.undo ()


class moves:
    x = 0
    y = 0


def messageDisplay (message):
    move.pensize (5)
    move.penup ()
    move.setposition (-130, -200)
    move.pendown ()
    move.write (message, font = ('ARIAL', 20, 'normal'))
    move.penup ()
    move.setpos (-130, 200)
    move.pendown ()
    move.write ('click anywhere to continue', font = ('ARIAL', 10, 'normal'))
    screen.onclick (endScreen)
    screen.mainloop ()


def endScreen (x, y):
    move.clear ()
    move.pensize (1)
    move.penup ()
    move.setpos (-100, 50)
    move.seth (0)
    move.pendown ()
    rect (move, 200, 50)
    move.penup ()
    move.setpos (-100, -50)
    move.seth (0)
    move.pendown ()
    rect (move, 200, 50)
    move.penup ()
    move.setpos (-50, 10)
    move.pendown ()
    move.write ('REPLAY', font = ('ARIAL', 20, 'normal'))
    move.penup ()
    move.setpos (-30, -90)
    move.pendown ()
    move.write ('QUIT', font = ('ARIAL', 20, 'normal'))
    screen.onclick (endChoice)
    screen.mainloop ()


def endChoice (x, y):
    if x >= -100:
        if y <= 50 and y >= 0:
            welcomeScreen ()
        elif y <= -50 and y >= -100:
            screen.bye ()


def winAnimation ():
    global winScoreArray
    # converting rows and columns to coordinates
    if winScoreArray == []:
        return
    else:
        x = winScoreArray [0] [1] * 100 - 100
        y = 100 - winScoreArray [0] [0] * 100
        move.penup ()
        move.setpos (x, y)
        x = winScoreArray [2] [1] * 100 - 100
        y = 100 - winScoreArray [2] [0] * 100
        move.seth (move.towards (x, y))
        move.pendown ()
        move.backward (50)
        move.forward (300)


def checkWin (b):
    if mode == 2:
        score = evaluate (b)
        if score == 10:
            print ('O Won')
            for i in range (0, 3):
                for j in range (0, 3):
                    b [i] [j] = 'o'
            winAnimation ()
            return ('O Won')
        elif score == -10:
            print ('X Won')
            for i in range (0, 3):
                for j in range (0, 3):
                    b [i] [j] = 'x'
            winAnimation ()
            return ('X Won')
        elif score == 0:
            if isMovesLeft (b) == False:
                print ("It's a Tie")
                return ("It's a Tie")
        return
    score = evaluate (b)
    if score == 10:
        print ('Computer won')
        for i in range (0, 3):
            for j in range (0, 3):
                b [i] [j] = 'o'
        winAnimation ()
        return ('Computer Won')
    elif score == -10:
        print ('You won')
        for i in range (0, 3):
            for j in range (0, 3):
                b [i] [j] = 'x'
        winAnimation ()
        return ('You Won')
    elif score == 0:
        if isMovesLeft (b) == False:
            print ("It's a Tie")
            return ("It's a Tie")
        else:
            return


def isMovesLeft (b):
    # checks whether any moves left or not
    for i in range (0, 3):
        for j in range (0, 3):
            if b [i] [j] == '_':
                return True
    return False


def evaluate (b):
    global winScoreArray
    # horizontal checking
    for i in range (0, 3):
        if b [i] [0] == b [i] [1] and b [i] [1] == b [i] [2]:
            winScoreArray = [[i, 0], [i, 1], [i, 2]]
            if b [i] [1] == player:
                return -10
            elif b [i] [1] == machine:
                return +10

    # vertical checking
    for i in range (0, 3):
        if b [0] [i] == b [1] [i] and b [1] [i] == b [2] [i]:
            winScoreArray = [[0, i], [1, i], [2, i]]
            if b [1] [i] == player:
                return -10
            elif b [1] [i] == machine:
                return +10

    # diagonal checking
    if b [0] [0] == b [1] [1] and b [1] [1] == b [2] [2]:
        winScoreArray = [[0, 0], [1, 1], [2, 2]]
        if b [1] [1] == player:
            return -10
        elif b [1] [1] == machine:
            return +10
    elif b [0] [2] == b [1] [1] and b [1] [1] == b [2] [0]:
        winScoreArray = [[0, 2], [1, 1], [2, 0]]
        if b [1] [1] == player:
            return -10
        elif b [1] [1] == machine:
            return +10

    return 0


def minimax (board, depth, ismax):
    # ismax denotes whether it is the maximiser's turn or not
    score = evaluate (board)
    if score == +10 or score == -10:
        return score
    if isMovesLeft (board) == False:
        return 0

    if ismax:
        bestval = -1000
        # check for empty positions
        for i in range (0, 3):
            for j in range (0, 3):
                if board [i] [j] == '_':
                    # make the move
                    board [i] [j] = 'o'
                    value = minimax (board, depth + 1, False)
                    # undo the move
                    board [i] [j] = '_'
                    if bestval == value:
                        value -= depth
                    bestval = max (bestval, value)
        return (bestval)

    else:
        bestval = +1000
        # check for empty positions
        for i in range (0, 3):
            for j in range (0, 3):
                if board [i] [j] == '_':
                    # make the move
                    board [i] [j] = 'x'
                    value = minimax (board, depth + 1, True) - 1
                    # undo the move
                    board [i] [j] = '_'
                    bestval = min (bestval, value)
        return (bestval)


def findBestMove (b):
    bestval = -1000
    bestmove = moves ()
    # check for empty positions
    for i in range (0, 3):
        for j in range (0, 3):
            if b [i] [j] == '_':
                # make the move
                b [i] [j] = 'o'
                value = minimax (b, 0, False)
                b [i] [j] = '_'
                if value > bestval:
                    bestval = value
                    bestmove.x = i
                    bestmove.y = j
    return (bestmove)


# drawing grid
def grid ():
    move.penup ()
    move.setpos (-150, 50)
    move.pendown ()
    move.forward (300)
    move.seth (0)
    move.penup ()
    move.setpos (-150, -50)
    move.seth (0)
    move.pendown ()
    move.forward (300)
    move.penup ()
    move.setpos (-50, -150)
    move.seth (90)
    move.pendown ()
    move.forward (300)
    move.penup ()
    move.setpos (50, -150)
    move.seth (90)
    move.pendown ()
    move.forward (300)
    # grid finished


def cross (n):
    if no_of_moves == 9:
        return
    x = 0
    y = 0
    if n in (1, 4, 7):
        x = -100
    elif n in (2, 5, 8):
        x = 0
    elif n in (3, 6, 9):
        x = 100

    if n in (1, 2, 3):
        y = 100
    elif n in (4, 5, 6):
        y = 0
    elif n in (7, 8, 9):
        y = -100
    move.penup ()
    move.setpos (x, y)
    move.pendown ()
    move.seth (45)
    move.forward (50)
    move.back (100)
    move.forward (50)
    move.seth (135)
    move.forward (50)
    move.back (100)
    move.forward (50)


def circle (n):
    x = 0
    y = 0
    if n in (1, 4, 7):
        x = -100
    elif n in (2, 5, 8):
        x = 0
    elif n in (3, 6, 9):
        x = 100

    if n in (1, 2, 3):
        y = 100
    elif n in (4, 5, 6):
        y = 0
    elif n in (7, 8, 9):
        y = -100
    move.penup ()
    move.setpos (x + 30, y + 28)
    move.pendown ()
    move.circle (40)


def draw (x, y):
    global board, no_of_moves
    row = 0
    column = 0
    global turn, mode
    n = 5
    if x >= -150 and x <= -50:
        if y <= 150 and y >= 50:
            n = 1
        elif y <= 50 and y >= -50:
            n = 4
        elif y <= -50 and y >= -150:
            n = 7
    elif x >= -50 and x <= 50:
        if y <= 150 and y >= 50:
            n = 2
        elif y <= 50 and y >= -50:
            n = 5
        elif y <= -50 and y >= -150:
            n = 8
    elif x >= 50 and x <= 150:
        if y <= 150 and y >= 50:
            n = 3
        elif y <= 50 and y >= -50:
            n = 6
        elif y <= -50 and y >= -150:
            n = 9
    else:
        return
    if n in (1, 2, 3):
        row = 0
    elif n in (4, 5, 6):
        row = 1
    elif n in (7, 8, 9):
        row = 2
    if n in (1, 4, 7):
        column = 0
    elif n in (2, 5, 8):
        column = 1
    elif n in (3, 6, 9):
        column = 2

    if board [row] [column] != '_':
        return
    if mode == 1:
        cross (n)
        no_of_moves += 1
        board [row] [column] = 'x'
        bestMove = findBestMove (board)
        if no_of_moves >= 9:
            message = checkWin (board)
            if message != None:
                messageDisplay (message)
            return
        p = bestMove.x
        q = bestMove.y
        board [p] [q] = 'o'
        no_of_moves += 1
        # print (board [0], '\n', board [1], '\n', board [2])
        # converting coordinate to value of board
        if p == 0:
            if q == 0:
                n = 1
            elif q == 1:
                n = 2
            elif q == 2:
                n = 3
        elif p == 1:
            if q == 0:
                n = 4
            elif q == 1:
                n = 5
            elif q == 2:
                n = 6
        elif p == 2:
            if q == 0:
                n = 7
            elif q == 1:
                n = 8
            elif q == 2:
                n = 9
        circle (n)
        message = checkWin (board)
        if message != None:
            messageDisplay (message)
    elif mode == 2:
        if turn == 1:
            cross (n)
            board [row] [column] = 'x'
            turn = 2
        else:
            circle (n)
            board [row] [column] = 'o'
            turn = 1
        message = checkWin (board)
        if message != None:
            messageDisplay (message)


def rect (t, l, b):  # turtle object, length, breadth
    for i in range (2):
        t.forward (l)
        t.right (90)
        t.forward (b)
        t.right (90)


def choose (x, y):
    global mode
    if x >= -100 and x <= 100:
        if y >= -100 and y <= -50:
            mode = 1
            print ('machine')
            move.clear ()
            grid ()
            screen.onclick (draw)
            screen.mainloop ()
        elif y >= -170 and y <= -120:
            mode = 2
            print ('human')
            move.clear ()
            grid ()
            screen.onclick (draw)
            screen.mainloop ()


def welcomeScreen ():
    global winScoreArray, mode, board, turn, no_of_moves
    winScoreArray = []
    mode = 0
    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    turn = 1
    no_of_moves = 0
    move.speed (0)
    move.clear ()
    move.penup ()
    move.setpos (-100, -50)
    move.pendown ()
    move.seth (0)
    rect (move, 200, 50)
    move.penup ()
    move.setpos (-100, -120)
    move.pendown ()
    move.seth (0)
    rect (move, 200, 50)
    move.pensize (5)
    move.penup ()
    move.setposition (-150, 40)
    move.pendown ()
    move.write ('TIC TAC TOE', font = ('ARIAL', 40, 'normal'))
    move.pensize (5)
    move.penup ()
    move.setposition (-70, -20)
    move.pendown ()
    move.write ('PLAY WITH', font = ('ARIAL', 20, 'normal'))
    move.pensize (5)
    move.penup ()
    move.setposition (-60, -90)
    move.pendown ()
    move.write ('MACHINE', font = ('ARIAL', 20, 'normal'))
    move.pensize (5)
    move.penup ()
    move.setposition (-47, -160)
    move.pendown ()
    move.write ('HUMAN', font = ('ARIAL', 20, 'normal'))
    screen.onclick (choose)
    screen.mainloop ()


# main program
welcomeScreen ()
# end of program
