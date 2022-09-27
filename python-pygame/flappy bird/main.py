"""

Flappy Bird demo for kengi template
Intended resolution -> 960 X 540
TARGET FPS -> 60 FPS
Delta Time -> Enabled
Code Readability Level -> Beginners / Intermediate

"""
import sys

from objects import *
from menu import *

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((W, H))


def main_game():
    dt = 1  # assuming ratio is 1 initially

    menu_manager = MenuManager()

    while True:
        # global event checking
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    return

        # general display blits
        screen.fill('black')

        menu_manager.update(events, dt)
        menu_manager.draw(screen)

        # display update and dt update
        pygame.display.update()
        dt = TARGET_FPS * clock.tick(FPS) / 1000  # ratio of target to current FPS
        # dt = round(dt, 6)
        print(clock.get_fps())
        # dt = 1
        if dt == 0:
            dt = 1


if __name__ == '__main__':
    main_game()
    pygame.quit()
    sys.exit(0)
