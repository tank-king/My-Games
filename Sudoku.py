import turtle
import random
import math
import time
import os

screen = turtle.Screen()
screen.setup(600, 600)
screen.title('Sudoku')
screen.tracer(0)

is_game_over = False


class Sudoku:  # a sudoku puzzle class
    def __init__(self, n = 9, missing = 0, demo = True):
        # n is order of matrix
        # missing is the number of missing numbers (depends on difficulty level)
        self.n = n
        self.board = [[0 for i in range(n)] for j in range(n)]
        self.unsolved_board = []
        self.srn = int(math.sqrt(n))  # n should be ideally a perfect square
        self.missing = missing
        self.demo = demo
        self.timer = time.time()

    def fill_box(self, row, col):
        num = [i for i in range(1, self.n + 1)]
        for i in range(self.srn):
            for j in range(self.srn):
                x = random.choice(num)
                num.remove(x)
                self.board[row + i][col + j] = x

    def diagonal(self):
        for i in range(0, self.n, self.srn):
            self.fill_box(i, i)

    def is_used_in_row(self, n, r):
        for i in range(self.n):
            if self.board[r][i] == n:
                return True
        return False

    def is_used_in_column(self, n, c):
        for i in range(self.n):
            if self.board[i][c] == n:
                return True
        return False

    def is_used_in_box(self, n, r, c):
        box_r = self.srn * (r // self.srn)
        box_c = self.srn * (c // self.srn)
        for i in range(self.srn):
            for j in range(self.srn):
                # self.board[box_r + i][box_c + j] = '*'
                if self.board[box_r + i][box_c + j] == n:
                    return True
        return False

    def isvalid(self, k, i, j):
        # check row
        if not self.is_used_in_row(k, i):
            # check column
            if not self.is_used_in_column(k, j):
                # check box
                if not self.is_used_in_box(k, i, j):
                    return True
        return False

    def solve_board(self, row, col):
        r = row
        c = col
        screen.update()
        # return False if the board has some erroneous numbers already
        # s.show_board()
        for i in range(self.n):
            for j in range(self.n):
                num = self.board[i][j]
                self.board[i][j] = 999
                if not self.isvalid(num, i, j) and num != 0:
                    self.board[i][j] = num
                    return False
                self.board[i][j] = num
        # r and c acts a cursor to which cell is currently being accessed
        # r means row and c means column

        # the recursion ends when we complete the last cell
        # that means the current cell will be self.board[self.n - 1][self.n]
        # so we will return True when we encounter this situation
        if r == self.n - 1 and c == self.n:
            return True
        if time.time() - self.timer > 60:
            return False  # too long time to find a solution
        # as we are incrementing the column value with each recursion
        # once we get to c = self.n then it should 'cycle' and become c = 0
        # and the row value should be incremented by 1
        if c == self.n:
            c -= c
            r += 1
        # if current cell is filled then continue to next cell
        if self.board[r][c] != 0:
            return self.solve_board(r, c + 1)

        for i in range(1, self.n + 1):
            # if safe to put value in this cell
            # then move to next cell
            if self.isvalid(i, r, c):
                self.board[r][c] = i
                if self.demo:
                    os.system('CLS')
                    self.show_board()
                    response = input('Press Enter to see next stage ({skip} to skip preview) : ')
                    if response == 'skip':
                        self.demo = False
                if self.solve_board(r, c + 1):
                    return True
            self.board[r][c] = 0

        # if reached this line, it means that no valid solution
        # has been found for this number placement
        # so it will return False indicating no valid solution
        return False

    def remove_elements(self):
        already_removed = []
        count = 0
        while count < self.missing:
            r = random.randint(0, self.n - 1)
            c = random.randint(0, self.n - 1)
            if [r, c] not in already_removed:
                self.board[r][c] = 0
                count += 1
            already_removed.append([r, c])

    def board_generate(self):
        while True:
            for i in range(n):
                for j in range(n):
                    self.board[i][j] = 0
            s.diagonal()
            if s.solve_board(0, srn):
                break
        self.remove_elements()

    def show_board(self):
        # print('*───────*───────*───────*')
        t = '*' + '─' * (2 * self.srn + 1)
        print(t * self.srn + '*')
        for i in range(self.n):
            for j in range(self.n):
                if j % self.srn == 0:
                    print('│', end = ' ')
                if self.board[i][j] != 0:
                    print(self.board[i][j], end = ' ')
                else:
                    print('-', end = ' ')
                if j == self.n - 1:
                    print('│', end = ' ')
            print('')
            if (i + 1) % self.srn == 0:
                t = '*' + '─' * (2 * self.srn + 1)
                print(t * self.srn + '*')
                # print('*' + '─' * (2 * self.srn + 1))
                # print('*───────*───────*───────*')


'''s.board = [[1, 4, 2, 0, 0, 0, 0, 0, 0],
           [3, 6, 5, 0, 0, 0, 0, 0, 0],
           [8, 7, 9, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 7, 3, 0, 0, 0],
           [0, 0, 0, 6, 9, 2, 0, 0, 0],
           [0, 0, 0, 8, 4, 5, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 8, 7, 1],
           [0, 0, 0, 0, 0, 0, 3, 9, 4],
           [0, 0, 0, 0, 0, 0, 5, 2, 6]]'''

'''s.solve_board(0, s.srn)
s.remove_elements()
os.system('CLS')
print('Final Board : ')
s.show_board()
x = input()'''

# the commented part is only for testing purposes
# it is a read-made selected puzzle that took long time to solve

# making the GUI
screen.bgcolor('black')
pen = turtle.Turtle()
pen.pencolor('white')
pen.hideturtle()
pen.penup()


def draw_board(n):
    d = 50
    if n == 4:
        d = 113
    if n == 16:
        d = 30

    x_shift = -160
    # y_shift = 0
    pen.goto(-d * n // 2 + x_shift, d * n // 2)
    pen.setheading(0)
    pen.pendown()
    pen.pensize(5)
    for i in range(4):
        pen.forward(d * n)
        pen.right(90)
    pen.pensize(1)
    pen.penup()
    for i in range(n):
        if i == 0:
            continue
        pen.goto(-d * n // 2 + i * d + x_shift, d * n // 2)
        pen.setheading(270)
        pen.pendown()
        pen.forward(d * n)
        pen.penup()
    for i in range(n):
        if i == 0:
            continue
        pen.goto(-d * n // 2 + x_shift, d * n // 2 - i * d)
        pen.setheading(0)
        pen.pendown()
        pen.forward(d * n)
        pen.penup()
    pen.pensize(4)
    for i in range(0, n, int(math.sqrt(n))):
        if i == 0:
            continue
        pen.goto(-d * n // 2 + i * d + x_shift, d * n // 2)
        pen.setheading(270)
        pen.pendown()
        pen.forward(d * n)
        pen.penup()
    for i in range(0, n, int(math.sqrt(n))):
        if i == 0:
            continue
        pen.goto(-d * n // 2 + x_shift, d * n // 2 - i * d)
        pen.setheading(0)
        pen.pendown()
        pen.forward(d * n)
        pen.penup()
    screen.update()


class Button:
    def __init__(self, msg = '0'):
        self.x = 0
        self.y = 0
        self.length = 75
        self.width = 75
        self.is_selected = False
        self.message = msg
        self.is_active = True


buttons = []
for button in range(16):
    temp = Button(str(button + 1))
    # temp.x = 150 + (i % 3) * 75
    # temp.y = 150 - (i // 3) * 75
    '''if i + 1 > 4:
        temp.is_active = False'''
    buttons.append(temp)


def draw_buttons(n):
    srn = math.sqrt(n)
    active_buttons = [i for i in buttons if buttons.index(i) < n]
    for i in buttons:
        i.is_active = False
    for i in active_buttons:
        i.is_active = True
        size = 25
        if n == 4:
            size = 30
        if n == 9:
            i.width = 75
            i.length = 75
        if n == 4:
            i.width = 100
            i.length = 100
        if n == 16:
            i.width = 60
            i.length = 60

        i.x = 150 + (buttons.index(i) % srn) * i.length
        if n == 4:
            i.y = 125 - (buttons.index(i) // srn) * i.width
        else:
            i.y = 150 - (buttons.index(i) // srn) * i.width
        pen.goto(i.x, i.y)
        pen.setheading(0)
        pen.pendown()
        for j in range(2):
            pen.forward(i.length)
            pen.left(90)
            pen.forward(i.width)
            pen.left(90)
        pen.penup()
        if int(i.message) < 10:
            pen.goto(i.x + i.length // 2 - size * 1 // 3, i.y + i.width // 2 - size * 3 // 4)
        else:
            pen.goto(i.x + i.length // 2 - size * 2 // 3, i.y + i.width // 2 - size * 3 // 4)
        pen.write(i.message, font = ('Arial', size, 'normal'))
        if not i.is_active:
            pen.goto(i.x, i.y + i.width)
            pen.pendown()
            pen.goto(i.x + i.length, i.y)
            pen.penup()
        if i.is_selected:
            pen.goto(i.x + 5, i.y + i.width - 5)
            pen.pendown()
            for k in range(2):
                pen.forward(i.length - 10)
                pen.right(90)
                pen.forward(i.width - 10)
                pen.right(90)
            screen.update()
            pen.penup()


n = 9
srn = int(math.sqrt(n))

curr_number = 'none'

s = Sudoku(n, 0, False)
# s.board_generate()

unmodifiable_cells = []


def update_unmodifiable_cells():
    global s, unmodifiable_cells
    unmodifiable_cells = []
    for row_no in range(n):
        for col_no in range(n):
            if s.board[row_no][col_no] != 0:
                unmodifiable_cells.append([row_no, col_no])


def is_solved():
    if is_board_filled():
        for i in range(n):
            for j in range(n):
                num = s.board[i][j]
                s.board[i][j] = 999
                if not s.isvalid(num, i, j):
                    s.board[i][j] = num
                    return False
                s.board[i][j] = num
        return True


def is_board_filled():
    global n, s
    for i in range(n):
        for j in range(n):
            if s.board[i][j] == 0:
                return False
    return True


def number_buttons_check(x, y):
    global curr_number, n, srn
    if buttons[0].x < x < buttons[srn - 1].x + buttons[srn - 1].length:
        if buttons[n - 1].y < y < buttons[0].y + buttons[0].width:
            for i in buttons:
                if i.is_active:
                    if i.x < x < i.x + i.length:
                        if i.y < y < i.y + i.width:
                            for k in buttons:
                                if k == i:
                                    continue
                                k.is_selected = False
                            i.is_selected = not i.is_selected
                            if i.is_selected:
                                curr_number = int(i.message)
                            else:
                                curr_number = 'none'
                            pen.clear()
                            if mode == 'machine':
                                pen.pensize(4)
                                pen.goto(150, -100)
                                rect(pen, 200, 50)
                                pen.goto(200, -150)
                                pen.write('Solve', font = ('Arial', 30, 'normal'))
                            pen.pensize(4)
                            pen.goto(150, -175)
                            rect(pen, 200, 50)
                            pen.goto(175, -220)
                            pen.write('Main Menu', font = ('Arial', 25, 'normal'))
                            draw_board(n)
                            draw_buttons(n)


def grid_check(x, y):
    d = 50
    if n == 4:
        d = 113
    if n == 16:
        d = 30

    x_shift = -160
    if -d * n // 2 + x_shift < x < d * n // 2 + x_shift:
        if -d * n // 2 < y < d * n // 2:
            # we are calculating box count from a new x-coordinate
            # which is not the origin
            # so we calculate the shift in origin and calculate the respective distance
            # so if the new point is at -a with respect to origin, and d is length of each box
            # then the current box number (starting from 0) is :
            # (x - (-a)) // d
            c = int((x - (-d * n // 2 + x_shift)) // d)
            # similar for y-coordinate but slightly changed formula because
            # we calculate the box number from the top, not from the bottom of the grid
            # so we multiply the net by -1, as instead of bottom to top we need top to bottom
            r = int(-(y - (d * n // 2)) // d)
            # s.board[0][0] = 15
            if [r, c] not in unmodifiable_cells:
                if curr_number != 'none':
                    if s.board[r][c] == int(curr_number):
                        s.board[r][c] = 0
                    else:
                        s.board[r][c] = int(curr_number)
                    pen2.clear()
                    draw_numbers_on_grid()
                    screen.update()


pen2 = turtle.Turtle()
pen2.hideturtle()
pen2.pencolor('white')
pen2.penup()


def draw_numbers_on_grid():
    d = 50
    size = 25
    if n == 4:
        d = 113
        size = 50
    if n == 16:
        d = 30
        size = 14
    x_shift = -160
    # s.show_board()
    for i in range(n):
        for j in range(n):
            if s.board[i][j] != 0:
                if [i, j] in unmodifiable_cells:
                    # pen2.goto(-d * n // 2 + x_shift + j * d + 5, d * n // 2 - i * d - 5)
                    # pen2.begin_fill()
                    pen2.setheading(0)
                    pen2.fillcolor('white')
                    pen2.color('#0099FF')
                    # pen2.end_fill()
                else:
                    pen2.pencolor('white')
                    num = s.board[i][j]
                    s.board[i][j] = 999
                    if s.isvalid(num, i, j):
                        pen2.pencolor('white')
                    else:
                        pen2.pencolor('#FF0000')
                    s.board[i][j] = num
                # a point to note is that i means row and j means column
                # hence we will add j to x coordinate while i to y coordinate
                # because column indicates the horizontal shift while row is the vertical shift
                if is_solved():
                    pen2.color('#00FF00')
                if n == 4:
                    pen2.goto(-d * n // 2 + x_shift + j * d + 40, d * n // 2 - i * d - 90)
                if n == 9:
                    pen2.goto(-d * n // 2 + x_shift + j * d + 15, d * n // 2 - i * d - 45)
                if n == 16:
                    if s.board[i][j] >= 10:
                        pen2.goto(-d * n // 2 + x_shift + j * d + 5, d * n // 2 - i * d - 27)
                    else:
                        pen2.goto(-d * n // 2 + x_shift + j * d + 12, d * n // 2 - i * d - 27)
                pen2.write(str(s.board[i][j]), font = ('Arial', size, 'normal'))


def check_buttons(x, y):
    global is_game_over
    number_buttons_check(x, y)
    grid_check(x, y)
    if 150 < x < 350:
        if -150 < y < -100:
            if mode == 'machine':
                pen.goto(150, -75)
                pen.write('Solving...', font = ('Arial', 20, 'normal'))
                if s.solve_board(0, 0):
                    # pen.undo()
                    pen.clear()
                    draw_buttons(n)
                    draw_board(n)
                    pen.goto(150, -75)
                    pen.write('Solved!', font = ('Arial', 20, 'normal'))
                else:
                    # pen.undo()
                    pen.clear()
                    draw_buttons(n)
                    draw_board(n)
                    pen.goto(150, -75)
                    pen.write('No Solution!', font = ('Arial', 20, 'normal'))
                    if time.time() - s.timer > 60:
                        pen.goto(-250, -280)
                        pen.write('Reason : Solution took longer than time limit (60 seconds)',
                                  font = ('Arial', 10, 'normal'))
                    else:
                        pen.goto(-250, -280)
                        pen.write(
                            'Reason : One or more numbers may not be possible to put in a location',
                            font = ('Arial', 10, 'normal'))
            if mode == 'machine':
                pen.pensize(4)
                pen.goto(150, -100)
                rect(pen, 200, 50)
                pen.goto(200, -150)
                pen.write('Solve', font = ('Arial', 30, 'normal'))
            pen.pensize(4)
            pen.goto(150, -175)
            rect(pen, 200, 50)
            pen.goto(175, -220)
            pen.write('Main Menu', font = ('Arial', 25, 'normal'))
            draw_numbers_on_grid()
        if -225 < y < -175:
            is_game_over = True
    # print(is_solved())


def rect(t, l, b):
    t.pendown()
    for i in range(2):
        t.forward(l)
        t.right(90)
        t.forward(b)
        t.right(90)
    t.penup()


is_menu_over = False


def welcome_screen_check(x, y):
    global is_welcome_screen_over
    if -95 < x < 105:
        if -75 < y < 0:
            is_welcome_screen_over = True
        elif -175 < y < -100:
            screen.bye()
            quit()


def welcome_screen():
    screen.setup(600, 600)
    pen.clear()
    pen2.clear()
    pen.goto(-210, 50)
    pen.write('SUDOKU', font = ('Arial', 75, 'normal'))
    pen.goto(-95, -0)
    rect(pen, 200, 75)
    pen.goto(-95, -100)
    rect(pen, 200, 75)
    pen.goto(-50, -65)
    pen.write('PLAY', font = ('Arial', 35, 'normal'))
    pen.goto(-50, -165)
    pen.write('QUIT', font = ('Arial', 35, 'normal'))
    while True:
        screen.onclick(welcome_screen_check)
        if is_welcome_screen_over:
            return
        screen.update()
        time.sleep(0.01)


def grid_size_check(x, y):
    global is_grid_size_over, n, srn
    if -95 < x < 105:
        if -50 < y < 0:
            is_grid_size_over = True
            n = 4
        elif -125 < y < -75:
            is_grid_size_over = True
            n = 9
        elif -200 < y < -150:
            is_grid_size_over = True
            n = 16
        srn = int(math.sqrt(n))


def grid_size_screen():
    pen.clear()
    pen2.clear()
    screen.setup(600, 600)
    pen.goto(-50, 130)
    pen.write('SELECT', font = ('Arial', 20, 'normal'))
    pen.goto(-110, 50)
    pen.write('VARIANT', font = ('Arial', 40, 'normal'))
    pen.goto(-95, -0)
    rect(pen, 200, 50)
    pen.goto(-95, -75)
    rect(pen, 200, 50)
    pen.goto(-95, -150)
    rect(pen, 200, 50)
    pen.goto(-40, -50)
    pen.write('4 X 4', font = ('Arial', 30, 'normal'))
    pen.goto(-40, -125)
    pen.write('9 X 9', font = ('Arial', 30, 'normal'))
    pen.goto(-60, -200)
    pen.write('16 X 16', font = ('Arial', 30, 'normal'))
    while True:
        screen.onclick(grid_size_check)
        if is_grid_size_over:
            return
        screen.update()
        time.sleep(0.01)


def mode_selection_screen_check(x, y):
    global is_mode_selection, mode
    if -150 < x < 150:
        if -50 < y < 0:
            is_mode_selection = True
            mode = 'human'
    if -150 < x < 220:
        if -125 < y < -75:
            is_mode_selection = True
            mode = 'machine'


def mode_selection_screen():
    pen.clear()
    pen2.clear()
    screen.setup(600, 600)
    pen.goto(-180, 75)
    pen.write('Who shall solve the puzzle?', font = ('Arial', 25, 'normal'))
    pen.goto(-150, 0)
    rect(pen, 100, 50)
    pen.goto(-50, 0)
    rect(pen, 200, 50)
    pen.goto(-136, -47)
    pen.write('You', font = ('Arial', 30, 'normal'))
    pen.goto(-150, -75)
    rect(pen, 170, 50)
    pen.goto(20, -75)
    rect(pen, 200, 50)
    pen.goto(-136, -125)
    pen.write('Machine', font = ('Arial', 30, 'normal'))
    pen.goto(-40, -22)
    pen.write('Solve a computer-generated', font = ('Arial', 10, 'normal'))
    pen.goto(-40, -42)
    pen.write('puzzle', font = ('Arial', 10, 'normal'))
    pen.goto(30, -98)
    pen.write('Find a solution to a puzzle', font = ('Arial', 10, 'normal'))
    pen.goto(30, -118)
    pen.write('using the machine', font = ('Arial', 10, 'normal'))
    while True:
        screen.onclick(mode_selection_screen_check)
        if is_mode_selection:
            return
        screen.update()
        time.sleep(0.01)


is_difficulty = False


def difficulty_check(x, y):
    global is_difficulty, difficulty
    if -95 < x < 105:
        if -50 < y < 0:
            is_difficulty = True
            difficulty = 'easy'
        elif -125 < y < -75:
            is_difficulty = True
            difficulty = 'medium'
        elif -200 < y < -150:
            is_difficulty = True
            difficulty = 'hard'


def difficulty_screen():
    pen.clear()
    pen2.clear()
    screen.setup(600, 600)
    pen.goto(-50, 130)
    pen.write('SELECT', font = ('Arial', 20, 'normal'))
    pen.goto(-150, 50)
    pen.write('DIFFICULTY', font = ('Arial', 40, 'normal'))
    pen.goto(-95, -0)
    rect(pen, 200, 50)
    pen.goto(-95, -75)
    rect(pen, 200, 50)
    pen.goto(-95, -150)
    rect(pen, 200, 50)
    pen.goto(-45, -50)
    pen.write('EASY', font = ('Arial', 30, 'normal'))
    pen.goto(-75, -125)
    pen.write('MEDIUM', font = ('Arial', 30, 'normal'))
    pen.goto(-45, -200)
    pen.write('HARD', font = ('Arial', 30, 'normal'))
    while True:
        screen.onclick(difficulty_check)
        if is_difficulty:
            return
        screen.update()
        time.sleep(0.01)


n = 9
mode = 'human'
difficulty = 'easy'


def play_game():
    global n, mode, difficulty, s
    m = 0
    screen.setup(900, 600)
    pen.clear()
    pen2.clear()
    if mode == 'human':
        if difficulty == 'easy':
            if n == 4:
                m = 5
            else:
                m = n * 3
        elif difficulty == 'medium':
            if n == 4:
                m = 8
            else:
                m = n * 5
        elif difficulty == 'hard':
            if n == 4:
                m = 10
            else:
                m = n * 7
        pen.goto(150, -200)
        pen.clear()
        pen.write('Generating Board...', font = ('Arial', 15, 'normal'))
        s = Sudoku(n, m, False)
        s.board_generate()
        # draw_board(n)
        # draw_buttons(n)
        # draw_numbers_on_grid()
        update_unmodifiable_cells()
        pen.clear()
        pen2.clear()
    else:
        s = Sudoku(n, 0, False)
        update_unmodifiable_cells()
    if mode == 'machine':
        pen.pensize(4)
        pen.goto(150, -100)
        rect(pen, 200, 50)
        pen.goto(200, -150)
        pen.write('Solve', font = ('Arial', 30, 'normal'))
    pen.pensize(4)
    pen.goto(150, -175)
    rect(pen, 200, 50)
    pen.goto(175, -220)
    pen.write('Main Menu', font = ('Arial', 25, 'normal'))
    draw_board(n)
    draw_buttons(n)
    draw_numbers_on_grid()
    # screen.onclick(check_buttons)
    # screen.mainloop()
    while True:
        screen.onclick(check_buttons)
        if is_game_over:
            return
        screen.update()
        time.sleep(0.01)


while True:
    unmodifiable_cells = []
    for button in buttons:
        button.is_selected = False
        button.is_active = False
    n = 9
    srn = 3
    is_game_over = False
    pen.clear()
    pen2.clear()
    is_welcome_screen_over = False
    is_grid_size_over = False
    is_mode_selection = False
    is_difficulty = False
    welcome_screen()
    grid_size_screen()
    mode_selection_screen()
    if mode == 'human':
        difficulty_screen()
    play_game()
    time.sleep(0.01)
# screen.exitonclick()
