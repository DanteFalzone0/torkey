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
import random
import sys
import os
from pygame.locals import *
from apple import Apple
fps_clock = pygame.time.Clock()
turkey_x_pos = 20
surface = pygame.display.set_mode((600, 600))
black = (0, 0, 0)
ground_y_pos = 540


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
        self._apples_eaten = 0


    def render(self, pygame_surface):
        if self._which_frame == 0:
            pygame_surface.blit(
                self._frame_0,
                (turkey_x_pos, self._y_pos)
            )

        elif self._which_frame == 1:
            pygame_surface.blit(
                self._frame_1,
                (turkey_x_pos, self._y_pos)
            )

        height = self._frame_0.get_size()[1]
        if self._y_pos < ground_y_pos - height:
            pygame_surface.blit(
                self._wing,
                (turkey_x_pos + 50, self._y_pos + 60)
            )


    def gobble(self):
        os.system("spd-say \"gobble gobble\" -t female3")


    def update_y_pos(self):
        height = self._frame_0.get_size()[1]
        if self._y_pos + height >= ground_y_pos:
            self._y_pos = ground_y_pos - height
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


    def get_width(self):
        return self._frame_0.get_size()[0]


    def get_height(self):
        return self._frame_0.get_size()[1]


    def get_y_pos(self):
        return self._y_pos


    def eat(self, apple):
        os.system("spd-say \"cronch\" -t female3 -w -i100")
        self._apples_eaten += 1
        apple.reset_y_pos(random.randint(0, 500))


turkey = Turkey(
    20,
    "assets/turkey0.png",
    "assets/turkey1.png",
    "assets/wing.png"
)

ground = pygame.image.load("assets/ground_foreground.png")

apple = Apple(300, "assets/apple.png")

def update_game_state(ticks):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

    surface.fill(black)
    surface.blit(ground, (0, ground_y_pos))

    if apple.update(turkey_x_pos) == 1:
        apple.reset_y_pos(random.randint(0, 500))
    apple.render(surface)

    turkey.update_y_pos()
    turkey.render(surface)

    if apple.get_x_pos() <= turkey_x_pos + turkey.get_width():
        turkey_min = turkey.get_y_pos()
        turkey_max = turkey_min + turkey.get_height()
        turkey_range = range(turkey_min, turkey_max)
        if apple.get_y_pos() in turkey_range:
            turkey.eat(apple)


    if ticks % 6 == 0:
        turkey.switch_frame()

    keys = pygame.key.get_pressed()
    if keys[K_SPACE]:
        turkey.gobble()
        turkey.jump()

    pygame.display.update()
    fps_clock.tick(30)

    if ticks == 59:
        return 0
    else:
        return ticks + 1


TICKS = 0
while True:
    TICKS = update_game_state(TICKS)
