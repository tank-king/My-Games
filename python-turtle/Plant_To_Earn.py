import pygame
import time
import os

pygame.init()


class Spritesheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename)

    def get_image_at_pos(self, x, y, width, height):
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), (x, y, width, height))

        return image

    def get_images(self, row, column, width, height):
        image_list = []
        for i in range(row * column):
            # print(i, (0 + (i % column) * width, 0 + i // column * height))
            sprite = self.get_image_at_pos(0 + (i % column) * width, 0 + i // column * height,
                                           width, height)
            image_list.append(sprite)
            # print(sprite.get_rect())

        return image_list


class BasicObject:
    def __init__(self, img_txt = None):
        self.x = 0
        self.y = 0
        try:
            self.image = pygame.image.load(img_txt)
        except pygame.error:
            print('warning : no image defined for this object')


class Platformer:
    def __init__(self, color = None):
        self.x = 0
        self.y = 0
        self.color = color
        self.maze = []  # if any maze is used


class Button:
    def __init__(self, text, ac, ic, tc):
        self.msg = text
        self.ac = ac
        self.ic = ic
        self.tc = tc

    def draw_button(self, surface):
        pass


class Game:
    def check_events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    pass
                if e.key == pygame.K_RIGHT:
                    pass
                if e.key == pygame.K_UP:
                    pass
                if e.key == pygame.K_DOWN:
                    pass
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_LEFT:
                    pass
                if e.key == pygame.K_RIGHT:
                    pass
                if e.key == pygame.K_UP:
                    pass
                if e.key == pygame.K_DOWN:
                    pass


field = Platformer((255, 255, 255))
field.maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 1, 1, 1, 1, 1, 0],
              [0, 1, 0, 0, 0, 0, 0, 1, 0],
              [0, 1, 0, 0, 0, 0, 0, 1, 0],
              [0, 1, 0, 0, 0, 0, 0, 1, 0],
              [0, 1, 0, 0, 0, 0, 0, 1, 0],
              [0, 1, 1, 1, 1, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              ]

ground_tile = pygame.image.load('ground_tile2.gif')
ground_tile = pygame.transform.scale(ground_tile, (70, 70))
field_tile = pygame.image.load('field_tile_1.gif')

screen = pygame.display.set_mode((9 * 70, 8 * 70))
pygame.display.set_caption('Plant To Earn')

score = 0


def field_set():
    for i in range(len(field.maze)):
        for j in range(len(field.maze[i])):
            if field.maze[i][j] == 1:
                # screen.blit(field_tile, (j * 70, i * 70))
                pygame.draw.rect(screen, (37, 16, 10), (j * 70, i * 70, 70, 70))
            elif field.maze[i][j] == 0:
                screen.blit(ground_tile, (j * 70, i * 70))
                # pygame.draw.rect(screen, (218, 165, 32), (j * 70, i * 70, 70, 70))


field_set()
pygame.display.update()


class Player:
    def __init__(self):
        self.x = 15
        self.y = 0
        self.direction = 'left'
        self.dx = 0
        self.dy = 0
        self.velocity = 5


player = Player()

walk = Spritesheet('boy_walking1.gif')
walk_images = walk.get_images(4, 4, 40, 60)

plant1 = pygame.image.load('plant1.gif')
plant1 = pygame.transform.scale(plant1, (70, 70))
plant2 = pygame.image.load('plant2.gif')
plant2 = pygame.transform.scale(plant2, (70, 70))
turnip = pygame.image.load('turnip1.gif')  # ('plant3.gif')
turnip = pygame.transform.scale(turnip, (70, 70))
carrot = pygame.image.load('carrot1.gif')  # ('plant3.gif')
carrot = pygame.transform.scale(carrot, (70, 70))

turnip_sell_price = 20
carrot_sell_price = 20
manure_price = 10

turnip_no = 0
carrot_no = 0
manure_no = 2

coins = 10

plant1_list = []
plant2_list = []
plant3_list = []

seed = pygame.image.load('seed1.gif')
seed = pygame.transform.scale(seed, (80, 80))

jug = pygame.image.load('jug1.png')
jug = pygame.transform.scale(jug, (100, 100))

sack = pygame.image.load('sack.gif')
sack = pygame.transform.scale(sack, (70, 70))

screen.blit(walk_images[15], (100, 100))

pos = (0, 0)  # for mouse
grid_pos = [0, 0]  # for maze

current_icon = 'none'
plantation_list = []
for i in range(len(field.maze)):
    for j in range(len(field.maze[i])):
        if field.maze[i][j] == 1:
            plantation_list.append([j, i])

plantation_status = []
for i in range(len(plantation_list)):
    plantation_status.append(False)


def plant_menu():
    s = pygame.Surface((200, 300))
    del s
    '''s.set_alpha(128)
    s.fill((255,255,255))
    screen.blit(s,(0,0))'''
    s2 = pygame.image.load('scroll1.gif')
    screen.blit(s2, (140, 70))


is_shop = False


def check_events():
    global player, pos, is_shop
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_v:
                is_shop = True
                # shop_screen()
            if e.key == pygame.K_g:
                Level.levels[Level.level].show_goals()
            '''if e.key == pygame.K_LEFT:
                player.direction = 'left'
                player.dx = -player.velocity
            if e.key == pygame.K_RIGHT:
                player.direction = 'right'
                player.dx = player.velocity
            if e.key == pygame.K_UP:
                player.direction = 'up'
                player.dy = -player.velocity
            if e.key == pygame.K_DOWN:
                player.direction = 'down'
                player.dy = player.velocity'''
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                player.dx = 0
            if e.key == pygame.K_RIGHT:
                player.dx = 0
            if e.key == pygame.K_UP:
                player.dy = 0
            if e.key == pygame.K_DOWN:
                player.dy = 0
        if e.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            grid_pos = get_target_grid()


class Plant:
    def __init__(self, type):
        self.x = 0
        self.y = 0
        self.stage = 'plant1'
        self.status_complete = 0
        self.rate = 5
        self.pic = plant1
        self.type = type
        self.timer = time.time()
        self.rate_timer = time.time()

    def stage_update(self):
        if time.time() - self.rate_timer >= 3:
            if self.rate >= -3:
                self.rate -= 1
            if self.rate < 0:
                if self.status_complete < 20:
                    self.rate = 0
                if self.status_complete >= 50 and self.status_complete <= 55:
                    self.rate = 0
            self.rate_timer = time.time()

        if time.time() - self.timer >= 1:
            self.timer = time.time()
            if self.status_complete < 100:
                self.status_complete += self.rate
                if self.status_complete > 100:
                    self.status_complete = 100
            if self.status_complete >= 50 and self.status_complete < 100:
                self.pic = plant2
            if self.status_complete >= 100:
                if self.type == 'turnip':
                    self.pic = turnip
                else:
                    self.pic = carrot

    def draw_status_bar(self):
        if self.status_complete < 100:
            pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 50, 10))
            pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.status_complete // 2, 10))

    def collect_plant(self):
        global plant_list, carrot_no, turnip_no
        if self.type == 'carrot':
            carrot_no += 1
        elif self.type == 'turnip':
            turnip_no += 1
        plant_list.remove(self)
        del self


plant_list = []


def message_box(message):
    text = pygame.font.SysFont('Comic Sans Ms', 15, True)
    pos = pygame.mouse.get_pos()
    message = 'No manure!'
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            if e.type == pygame.MOUSEBUTTONUP:
                pos2 = pygame.mouse.get_pos()
                if pos2[0] > pos[0] // 70 * 70 and pos2[0] < pos[0] // 70 * 70 + 100:
                    if pos2[1] > pos[1] // 70 * 70 + 20 and pos2[1] < pos[1] // 70 * 70 + 40:
                        return

        field_set()
        pygame.draw.rect(screen, (119, 63, 10), (70 * 2, 70 * 2, 70 * 5, 70 * 4))
        screen.blit(walk_images[0], (player.x, player.y))
        for i in plant_list:
            screen.blit(i.pic, (i.x, i.y))
            i.stage_update()
            i.draw_status_bar()

        pos2 = pygame.mouse.get_pos()
        if pos2[1] > 280 and pos2[1] < 350:
            if pos2[0] > 210 and pos2[0] < 280:
                pygame.draw.rect(screen, (255, 255, 255), (210, 280, 70, 70))
                pygame.draw.rect(screen, (119, 63, 10), (215, 285, 60, 60))
            if pos2[0] > 280 and pos2[0] < 350:
                pygame.draw.rect(screen, (255, 255, 255), (280, 280, 70, 70))
                pygame.draw.rect(screen, (119, 63, 10), (285, 285, 60, 60))
            if pos2[0] > 350 and pos2[0] < 420:
                pygame.draw.rect(screen, (255, 255, 255), (350, 280, 70, 70))
                pygame.draw.rect(screen, (119, 63, 10), (355, 285, 60, 60))

        if current_icon != 'none':
            if current_icon == 'seed':
                pygame.draw.rect(screen, (255, 255, 255), (210, 280, 70, 70))
                pygame.draw.rect(screen, (119, 63, 10), (215, 285, 60, 60))
            if current_icon == 'jug':
                pygame.draw.rect(screen, (255, 255, 255), (280, 280, 70, 70))
                pygame.draw.rect(screen, (119, 63, 10), (285, 285, 60, 60))
            if current_icon == 'sack':
                pygame.draw.rect(screen, (255, 255, 255), (350, 280, 70, 70))
                pygame.draw.rect(screen, (119, 63, 10), (355, 285, 60, 60))

        screen.blit(seed, (70 * 3 - 5, 70 * 4 - 5))
        screen.blit(jug, (70 * 4 - 15, 70 * 4 - 15))
        screen.blit(sack, (70 * 5, 70 * 4))

        Level.levels[-1].show_time()

        pygame.draw.rect(screen, (255, 255, 255), (pos[0] // 70 * 70, pos[1] // 70 * 70, 100, 40))
        screen.blit(text.render(message, True, (0, 0, 0)), (pos[0] // 70 * 70 + 5, pos[1] // 70 *
                                                            70))
        pygame.draw.rect(screen, (154, 123, 79),
                         (pos[0] // 70 * 70, pos[1] // 70 * 70 + 20, 100, 20))
        screen.blit(text.render('Ok', True, (0, 0, 0)), (pos[0] // 70 * 70 + 35, pos[1] // 70 *
                                                         70 + 17))
        pygame.display.update()


def get_target_grid():
    global field, pos, player, current_icon, plant1_list, plant2_list, plant3_list, manure_no
    xcor = pos[0]
    ycor = pos[1]
    x1 = xcor // 70
    y1 = ycor // 70
    x2 = player.x // 70
    y2 = player.y // 70

    if y1 == 4:
        if x1 == 3:
            if current_icon != 'seed':
                current_icon = 'seed'
            else:
                current_icon = 'none'
        elif x1 == 4:
            if current_icon != 'jug':
                current_icon = 'jug'
            else:
                current_icon = 'none'
        elif x1 == 5:
            if current_icon != 'sack':
                current_icon = 'sack'
            else:
                current_icon = 'none'

    if field.maze[y1][x1] == 1:
        if y1 == 1:
            x2 = x1 * 70 + 15
            y2 = (y1 - 1) * 70
        elif y1 == 6:
            x2 = x1 * 70 + 15
            y2 = (y1 + 1) * 70
        else:
            if x1 == 1:
                x2 = (x1 - 1) * 70 + 15
                y2 = y1 * 70
            elif x1 == 7:
                x2 = (x1 + 1) * 70 + 15
                y2 = y1 * 70
        player.x = x2
        player.y = y2

        for i in range(len(plantation_list)):
            if plantation_list[i] == [x1, y1]:
                if current_icon == 'seed':
                    if plantation_status[i] is False:
                        plantation_status[i] = True
                        seed_type = seed_type_menu(x1 * 70, y1 * 70)
                        temp = Plant(seed_type)
                        temp.x = x1 * 70
                        temp.y = y1 * 70
                        plant_list.append(temp)
                        # current_icon = 'none'
                else:
                    if plantation_status[i]:
                        for j in range(len(plant_list)):
                            if plant_list[j].x == x1 * 70 and plant_list[j].y == y1 * 70:
                                if current_icon == 'sack':
                                    manure_no -= 1
                                    if manure_no < 0:
                                        manure_no = 0
                                        message_box('hihihhi')
                                    else:
                                        plant_list[j].rate = 5
                                    # current_icon = 'none'
                                elif current_icon == 'jug':
                                    # current_icon = 'none'
                                    plant_list[j].rate += 2
                                    if plant_list[j].rate > 5:
                                        plant_list[j].rate = 5

                                if plant_list[j].status_complete >= 100:
                                    plant_list[j].collect_plant()
                                    plantation_status[i] = False
                                break


player_time = time.time()

# welcome_screen()

# shopping materials
sack_count = 5
seed_count = 5


def shop_screen():
    global manure_no, carrot_no, turnip_no, coins, is_shop
    message = '      ' + 'Coins : ' + str(coins)
    s2 = pygame.image.load('scroll1.gif')
    text = pygame.font.SysFont('Comic Sans Ms', 30, True, True)
    text1 = text.render('Shop', True, (0, 0, 0))
    text = pygame.font.SysFont('Comic Sans Ms', 25, True)
    text2 = text.render('Manure', True, (0, 0, 0))
    msg = pygame.font.SysFont('Comic Sans Ms', 20, True)
    msg_txt = msg.render(message, True, (0, 0, 0))
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_v:
                    is_shop = False
                    return
            if e.type == pygame.MOUSEBUTTONUP:
                message = '      ' + 'Coins : ' + str(coins)
                pos = pygame.mouse.get_pos()
                if pos[0] > 370 and pos[0] < 420:
                    if pos[1] > 200 and pos[1] < 250:
                        manure_no += 1
                        coins -= manure_price
                        message = '      ' + 'Coins : ' + str(coins)
                        if coins < 0:
                            coins += manure_price
                            manure_no -= 1
                            message = ' ' + 'Not enough Coins!'
                    elif pos[1] > 310 and pos[1] < 340:
                        carrot_no -= 1
                        coins += carrot_sell_price
                        message = '      ' + 'Coins : ' + str(coins)
                        if carrot_no < 0:
                            carrot_no = 0
                            message = 'No more Carrots left!'
                            coins -= carrot_sell_price
                    elif pos[1] > 350 and pos[1] < 380:
                        turnip_no -= 1
                        coins += turnip_sell_price
                        message = '      ' + 'Coins : ' + str(coins)
                        if turnip_no < 0:
                            turnip_no = 0
                            message = 'No more Turnips left!'
                            coins -= turnip_sell_price

        field_set()
        pygame.draw.rect(screen, (119, 63, 10), (70 * 2, 70 * 2, 70 * 5, 70 * 4))
        screen.blit(walk_images[0], (player.x, player.y))
        for i in plant_list:
            screen.blit(i.pic, (i.x, i.y))
            i.stage_update()
            i.draw_status_bar()

        screen.blit(s2, (140, 70))
        pos = pygame.mouse.get_pos()
        if pos[0] > 370 and pos[0] < 420:
            if pos[1] > 200 and pos[1] < 250:
                pygame.draw.rect(screen, (0, 75, 0), (370, 200, 50, 40))
            elif pos[1] > 310 and pos[1] < 340:
                pygame.draw.rect(screen, (0, 75, 0), (370, 310, 50, 35))
            elif pos[1] > 350 and pos[1] < 380:
                pygame.draw.rect(screen, (0, 75, 0), (370, 350, 50, 35))
        screen.blit(text1, (290, 90))
        screen.blit(text1, (290, 90))
        text2 = text.render('Buy : ', True, (0, 0, 0))
        screen.blit(text2, (200, 150))
        text2 = text.render('Manure', True, (0, 0, 0))
        screen.blit(text2, (220, 200))
        text2 = text.render('Sell : ', True, (0, 0, 0))
        screen.blit(text2, (200, 260))
        text2 = text.render('Carrot', True, (0, 0, 0))
        screen.blit(text2, (220, 310))
        text2 = text.render('Turnip', True, (0, 0, 0))
        screen.blit(text2, (220, 350))
        msg_txt = msg.render(message, True, (0, 0, 0))
        screen.blit(msg_txt, (210, 425))

        text2 = text.render('Qty', True, (0, 0, 0))
        screen.blit(text2, (315, 150))
        text2 = text.render(str(manure_no), True, (0, 0, 0))
        screen.blit(text2, (330, 200))
        text2 = text.render(str(carrot_no), True, (0, 0, 0))
        screen.blit(text2, (330, 310))
        text2 = text.render(str(turnip_no), True, (0, 0, 0))
        screen.blit(text2, (330, 350))

        text2 = text.render('Rate', True, (0, 0, 0))
        screen.blit(text2, (370, 150))
        text2 = text.render(str(manure_price), True, (0, 0, 0))
        screen.blit(text2, (380, 200))
        text2 = text.render(str(carrot_sell_price), True, (0, 0, 0))
        screen.blit(text2, (380, 310))
        text2 = text.render(str(turnip_sell_price), True, (0, 0, 0))
        screen.blit(text2, (380, 350))

        pygame.display.update()


def seed_type_menu(x, y):
    text = pygame.font.SysFont('comic sans ms', 20)
    text1 = text.render('Carrot', True, (0, 0, 0))
    text2 = text.render('Turnip', True, (0, 0, 0))
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            if e.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] > x and mouse_pos[0] < x + 100:
                    if mouse_pos[1] > y and mouse_pos[1] < y + 25:
                        return 'carrot'
                    elif mouse_pos[1] > y + 25 and mouse_pos[1] < y + 50:
                        return 'turnip'

        field_set()
        pygame.draw.rect(screen, (119, 63, 10), (70 * 2, 70 * 2, 70 * 5, 70 * 4))
        screen.blit(walk_images[0], (player.x, player.y))
        for i in plant_list:
            screen.blit(i.pic, (i.x, i.y))
            i.stage_update()
            i.draw_status_bar()
        pos = pygame.mouse.get_pos()
        if pos[1] > 280 and pos[1] < 350:
            if pos[0] > 210 and pos[0] < 280:
                pygame.draw.rect(screen, (255, 255, 255), (210, 280, 70, 70))
                pygame.draw.rect(screen, (119, 63, 10), (215, 285, 60, 60))
            if pos[0] > 280 and pos[0] < 350:
                pygame.draw.rect(screen, (255, 255, 255), (280, 280, 70, 70))
                pygame.draw.rect(screen, (119, 63, 10), (285, 285, 60, 60))
            if pos[0] > 350 and pos[0] < 420:
                pygame.draw.rect(screen, (255, 255, 255), (350, 280, 70, 70))
                pygame.draw.rect(screen, (119, 63, 10), (355, 285, 60, 60))

        if current_icon != 'none':
            if current_icon == 'seed':
                pygame.draw.rect(screen, (255, 255, 255), (210, 280, 70, 70))
                pygame.draw.rect(screen, (119, 63, 10), (215, 285, 60, 60))
            if current_icon == 'jug':
                pygame.draw.rect(screen, (255, 255, 255), (280, 280, 70, 70))
                pygame.draw.rect(screen, (119, 63, 10), (285, 285, 60, 60))
            if current_icon == 'sack':
                pygame.draw.rect(screen, (255, 255, 255), (350, 280, 70, 70))
                pygame.draw.rect(screen, (119, 63, 10), (355, 285, 60, 60))
        screen.blit(seed, (70 * 3 - 5, 70 * 4 - 5))
        screen.blit(jug, (70 * 4 - 15, 70 * 4 - 15))
        screen.blit(sack, (70 * 5, 70 * 4))

        Level.levels[-1].show_time()

        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.rect(screen, (255, 255, 255), (x, y, 100, 50))
        if mouse_pos[0] > x and mouse_pos[0] < x + 100:
            if mouse_pos[1] > y and mouse_pos[1] < y + 25:
                pygame.draw.rect(screen, (154, 123, 79), (x, y, 100, 25))
            elif mouse_pos[1] > y + 25 and mouse_pos[1] < y + 50:
                pygame.draw.rect(screen, (154, 123, 79), (x, y + 25, 100, 25))
            else:
                pygame.draw.rect(screen, (154, 123, 79), (x, y, 100, 25))
        else:
            pygame.draw.rect(screen, (154, 123, 79), (x, y, 100, 25))
        screen.blit(text1, (x + 3, y - 3))
        screen.blit(text2, (x + 3, y + 20))
        pygame.display.update()


class Level:
    level = 0
    levels = []

    def __init__(self, carrots = 0, turnip = 0, coins = 0, duration = 30):
        Level.level += 1
        Level.levels.append(self)
        self.start_time = time.time()
        self.goals = [carrots, turnip, coins, duration]

    def level_reset(self):
        global carrot_no, turnip_no, coins
        carrot_no = turnip_no = 0
        coins = 10
        self.start_time = time.time()
        for i in plant_list:
            plant_list.remove(i)
            del i

    def show_goals(self):
        s2 = pygame.image.load('scroll1.gif')
        text = pygame.font.SysFont('Comic Sans Ms', 30, True, True)
        t2 = text.render('Goals', True, (0, 0, 0))
        text = pygame.font.SysFont('Comic Sans Ms', 25, True)
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    quit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_g:
                        return

            field_set()
            pygame.draw.rect(screen, (119, 63, 10), (70 * 2, 70 * 2, 70 * 5, 70 * 4))
            screen.blit(walk_images[0], (player.x, player.y))
            for i in plant_list:
                screen.blit(i.pic, (i.x, i.y))
                i.stage_update()
                i.draw_status_bar()

            screen.blit(s2, (140, 70))
            screen.blit(t2, (290, 90))
            screen.blit(text.render('Level ' + str(Level.level), True, (0, 0, 0)), (270, 150))
            screen.blit(text.render('Carrots : ' + str(self.goals[0]), True, (0, 0, 0)), (220, 200))
            screen.blit(text.render('Turnips : ' + str(self.goals[1]), True, (0, 0, 0)), (220, 250))
            screen.blit(text.render('Coins : ' + str(self.goals[2]), True, (0, 0, 0)), (220, 300))
            screen.blit(text.render('Time : ', True, (0, 0, 0)), (240, 350))
            screen.blit(text.render(str(self.goals[3] // 60) + ':' + str(self.goals[3] % 60), True,
                                    (0, 0, 0)), (340, 350))
            pygame.display.update()

    def end_screen(self, status):
        global score
        s2 = pygame.image.load('scroll1.gif')
        text = pygame.font.SysFont('Comic Sans Ms', 30, True, True)
        if status:
            msg = ' ' + 'You Won!'
            message = 'Press G to proceed'
        else:
            msg = 'You Lost!'
            message = 'Press G to replay'
        t2 = text.render(msg, True, (0, 0, 0))
        text = pygame.font.SysFont('Comic Sans Ms', 25, True)
        text2 = pygame.font.SysFont('Comic Sans Ms', 20, True, True)
        if status:
            bonus = int((time.time() - self.start_time) * 1)
            lvl_score = int(Level.level * 10)
            tot_score = bonus + lvl_score
        else:
            bonus = 0
            lvl_score = 0
            tot_score = 0
        score += tot_score // 100
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    quit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_g:
                        return
            field_set()
            pygame.draw.rect(screen, (119, 63, 10), (70 * 2, 70 * 2, 70 * 5, 70 * 4))
            screen.blit(s2, (140, 70))
            screen.blit(t2, (250, 90))
            screen.blit(text.render('Level Score : ' + str(lvl_score), True, (0, 0, 0)), (200, 180))
            screen.blit(text.render('Bonus Score : ' + str(bonus), True, (0, 0, 0)), (200, 240))
            screen.blit(text.render('Total Score : ' + str(tot_score), True, (0, 0, 0)), (200, 300))
            screen.blit(text2.render(message, True, (0, 0, 0)), (230, 360))
            pygame.display.update()

    def show_time(self):
        m = int(self.goals[3] - (time.time() - self.start_time)) // 60
        s = int(self.goals[3] - (time.time() - self.start_time)) % 60
        if m < 10:
            m2 = '0' + str(m)
        else:
            m2 = str(m)
        if s < 10:
            s2 = '0' + str(s)
        else:
            s2 = str(s)

        if m * 60 + s < self.goals[3]:
            pass

        text = pygame.font.SysFont('Comic Sans Ms', 50)
        screen.blit(text.render(m2, True, (255, 255, 255)), (70 * 3.5, 70 * 3))
        screen.blit(text.render(':', True, (255, 255, 255)), (70 * 4.4, 70 * 3))
        screen.blit(text.render(s2, True, (255, 255, 255)), (70 * 4.6, 70 * 3))

    def start_level(self):
        is_carrots = is_turnips = is_coins = False
        self.start_time = time.time()
        while True:
            # shop_screen()
            field_set()
            pygame.draw.rect(screen, (119, 63, 10), (70 * 2, 70 * 2, 70 * 5, 70 * 4))
            screen.blit(walk_images[0], (player.x, player.y))
            for i in plant_list:
                screen.blit(i.pic, (i.x, i.y))
                i.stage_update()
                i.draw_status_bar()
            player.x += player.dx
            player.y += player.dy
            pos = pygame.mouse.get_pos()
            if pos[1] > 280 and pos[1] < 350:
                if pos[0] > 210 and pos[0] < 280:
                    pygame.draw.rect(screen, (255, 255, 255), (210, 280, 70, 70))
                    pygame.draw.rect(screen, (119, 63, 10), (215, 285, 60, 60))
                if pos[0] > 280 and pos[0] < 350:
                    pygame.draw.rect(screen, (255, 255, 255), (280, 280, 70, 70))
                    pygame.draw.rect(screen, (119, 63, 10), (285, 285, 60, 60))
                if pos[0] > 350 and pos[0] < 420:
                    pygame.draw.rect(screen, (255, 255, 255), (350, 280, 70, 70))
                    pygame.draw.rect(screen, (119, 63, 10), (355, 285, 60, 60))

            if current_icon != 'none':
                if current_icon == 'seed':
                    pygame.draw.rect(screen, (255, 255, 255), (210, 280, 70, 70))
                    pygame.draw.rect(screen, (119, 63, 10), (215, 285, 60, 60))
                if current_icon == 'jug':
                    pygame.draw.rect(screen, (255, 255, 255), (280, 280, 70, 70))
                    pygame.draw.rect(screen, (119, 63, 10), (285, 285, 60, 60))
                if current_icon == 'sack':
                    pygame.draw.rect(screen, (255, 255, 255), (350, 280, 70, 70))
                    pygame.draw.rect(screen, (119, 63, 10), (355, 285, 60, 60))

            screen.blit(seed, (70 * 3 - 5, 70 * 4 - 5))
            screen.blit(jug, (70 * 4 - 15, 70 * 4 - 15))
            screen.blit(sack, (70 * 5, 70 * 4))

            self.show_time()

            if is_shop:
                shop_screen()

            check_events()

            # plant_menu()
            # exit condition
            if time.time() - self.start_time >= self.goals[3]:
                self.end_screen(False)
                self.show_goals()
                self.level_reset()
            '''if carrot_no >= self.goals[0]:
                if turnip_no >= self.goals[1]:
                    if coins >= self.goals[2]:
                        if time.time() - self.start_time < self.goals[3]:
                            self.end_screen(True)
                            self.level_reset()
                            return'''
            if carrot_no >= self.goals[0]:
                is_carrots = True
            if turnip_no >= self.goals[1]:
                is_turnips = True
            if coins >= self.goals[2]:
                is_coins = True
            if is_carrots and is_turnips and is_coins:
                if time.time() - self.start_time < self.goals[3]:
                    self.end_screen(True)
                    self.level_reset()
                    return
            pygame.display.update()
            pygame.time.Clock().tick(60)


def home_page():
    text = pygame.font.SysFont('Comic Sans Ms', 70)
    text2 = pygame.font.SysFont('Comic Sans Ms', 20)
    heading = text.render('Plant to Earn', True, (255, 255, 255))
    text = pygame.font.SysFont('Comic Sans Ms', 45)
    show_score = False
    try:
        f = open('Farm_game_score_file.txt', 'r')
        high_score = int(f.read())
        f.close()
    except FileNotFoundError:
        f = open('Farm_game_score_file.txt', 'w')
        f.write(str(0))
        high_score = 0
        f.close()
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[1] > 350 and pos[1] < 420:
                    if pos[0] > 140 and pos[0] < 245:
                        return
                    if pos[0] > 245 and pos[0] < 390:
                        show_score = not show_score
                    if pos[0] > 390 and pos[0] < 500:
                        quit()
        pos = pygame.mouse.get_pos()
        field_set()
        # pygame.draw.rect(screen, (119, 63, 10), (70 * 2, 70 * 2, 70 * 5, 70 * 4))
        pygame.draw.rect(screen, (37, 16, 10), (70 * 2, 70 * 2, 70 * 5, 70 * 4))
        if pos[1] > 350 and pos[1] < 420:
            if pos[0] > 140 and pos[0] < 245:
                pygame.draw.rect(screen, (255, 255, 255), (140, 350, 100, 70))
                pygame.draw.rect(screen, (37, 16, 10), (145, 355, 90, 60))
            if pos[0] > 245 and pos[0] < 390:
                pygame.draw.rect(screen, (255, 255, 255), (240, 350, 140, 70))
                pygame.draw.rect(screen, (37, 16, 10), (245, 355, 130, 60))
            if pos[0] > 390 and pos[0] < 500:
                pygame.draw.rect(screen, (255, 255, 255), (380, 350, 115, 70))
                pygame.draw.rect(screen, (37, 16, 10), (385, 355, 105, 60))
        screen.blit(heading, (105, 90))
        screen.blit(text.render('Play', True, (255, 255, 255)), (150, 350))
        screen.blit(text.render('Score', True, (255, 255, 255)), (245, 350))
        screen.blit(text.render('Quit', True, (255, 255, 255)), (390, 350))
        if show_score:
            # pygame.draw.rect(screen, (255, 255, 255), (150, 200, 300, 70))
            screen.blit(text.render('High Score : ' + str(high_score), True, (255, 255, 255)),
                        (165, 230))
        pygame.display.update()


os.system('CLS')
home_page()


def score_file_update():
    global score
    try:
        f = open('Farm_game_score_file.txt', 'r+')
        high_score = int(f.read())
        if score > high_score:
            f.write(str(score))
        f.close()
    except FileNotFoundError:
        f = open('Farm_game_score_file.txt', 'w')
        f.write(str(0))
        high_score = 0
        if score > high_score:
            f.write(str(score))
        f.close()


def main_game():
    level_goals = [[1, 1, 20, 100],
                   [3, 3, 40, 180],
                   [4, 4, 60, 210],
                   [1, 1, 20, 100],
                   [1, 1, 20, 100]
                   ]
    '''carrots = 1
    turnips = 1
    money = 0
    duration = 100'''
    while True:
        goals = level_goals[Level.level]
        # curr_level = Level(carrots, turnips, money, duration)
        curr_level = Level(goals[0], goals[1], goals[2], goals[3])
        Level.levels.append(curr_level)
        curr_level.show_goals()
        curr_level.start_level()
        score_file_update()
        Level.levels.remove(curr_level)
        del curr_level


main_game()
