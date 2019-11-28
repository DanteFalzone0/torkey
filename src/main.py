#          main.py file of torkey
#    Copyright (C) 2019  Dante Falzone
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import pygame
import sys
import os
from pygame.locals import *
FPS_CLOCK = pygame.time.Clock()
TURKEY_X_POS = 20
SURFACE = pygame.display.set_mode((600, 600))
BLACK = (0, 0, 0)
GROUND_Y_POS = 540


class Turkey:
    def __init__(
        self,
        starting_y_pos,
        frame_0_path,
        frame_1_path,
        wing_path
    ):

        self._frame_0 = pygame.image.load(frame_0_path)
        self._frame_1 = pygame.image.load(frame_1_path)
        self._wing = pygame.image.load(wing_path)
        self._y_pos = starting_y_pos
        self._downwards_momentum = 0.0
        self._which_frame = 0 # determines which frame we show


    def render(self, pygame_surface):
        if self._which_frame == 0:
            pygame_surface.blit(
                self._frame_0,
                (TURKEY_X_POS, self._y_pos)
            )

        elif self._which_frame == 1:
            pygame_surface.blit(
                self._frame_1,
                (TURKEY_X_POS, self._y_pos)
            )

        height = self._frame_0.get_size()[1]
        if self._y_pos < GROUND_Y_POS - height:
            pygame_surface.blit(
                self._wing,
                (TURKEY_X_POS + 50, self._y_pos + 60)
            )


    def gobble(self):
        os.system("spd-say \"gobble gobble\" -t female3")


    def update_y_pos(self):
        height = self._frame_0.get_size()[1]
        if self._y_pos + height >= GROUND_Y_POS:
            self._y_pos = GROUND_Y_POS - height
            if self._downwards_momentum > 0:
                self._downwards_momentum = 0.0
        else:
            self._downwards_momentum += 1.0
        self._y_pos += int(self._downwards_momentum)


    def jump(self):
        self._downwards_momentum = -10.0

    def switch_frame(self):
        if self._which_frame == 0:
            self._which_frame = 1
        elif self._which_frame == 1:
            self._which_frame = 0


TURKEY = Turkey(
    20,
    "assets/turkey0.png",
    "assets/turkey1.png",
    "assets/wing.png"
)

GROUND = pygame.image.load("assets/ground_foreground.png")

def update_game_state(ticks):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

    SURFACE.fill(BLACK)

    SURFACE.blit(GROUND, (0, GROUND_Y_POS))

    TURKEY.update_y_pos()

    TURKEY.render(SURFACE)

    if ticks % 6 == 0:
        TURKEY.switch_frame()

    keys = pygame.key.get_pressed()
    if keys[K_SPACE]:
        TURKEY.gobble()
        TURKEY.jump()

    pygame.display.update()
    FPS_CLOCK.tick(30)

    if ticks == 59:
        return 0
    else:
        return ticks + 1


TICKS = 0
while True:
    TICKS = update_game_state(TICKS)
