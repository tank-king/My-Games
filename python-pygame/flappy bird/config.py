"""
Entry point for all imports
Here we will need to alias pygame from kengi.pygame
"""

import os
import pygame

W, H = 960, 540

FPS = 60
TARGET_FPS = 60

ASSETS = 'assets'
IMAGES = os.path.join(ASSETS, 'images')
SOUNDS = os.path.join(ASSETS, 'sounds')

SPEED = 2


# below are some utility functions

def load_image(path, alpha=False, scale=1.0, color_key=None):
    img = pygame.image.load(path)
    if alpha:
        img = img.convert_alpha()
    else:
        img = img.convert()
    if scale != 1.0:
        img = pygame.transform.scale_by(img, scale)
    if color_key:
        img.set_colorkey(color_key)
    return img


def clamp(value, mini, maxi):
    if value < mini:
        return mini
    if value > maxi:
        return maxi
    return value
