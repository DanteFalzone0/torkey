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
from pygame.locals import *
fps_clock = pygame.time.Clock()
TURKEY_X_POS = 20
SURFACE = pygame.display.set_mode((600, 600))
BLACK = (0, 0, 0)

class Turkey:
    def __init__(self, starting_y_pos, frame_0_path, frame_1_path):
        self._frame_0 = pygame.image.load(frame_0_path)
        self._frame_1 = pygame.image.load(frame_1_path)
        self._y_pos = starting_y_pos
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


    def update_y_pos(self, amount):
        self._y_pos += amount


    def switch_frame(self):
        if self._which_frame == 0:
            self._which_frame = 1
        elif self._which_frame == 1:
            self._which_frame = 0


turkey = Turkey(
    20,
    "../assets/turkey0.png",
    "../assets/turkey1.png"
)

def update_game_state(ticks):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

    SURFACE.fill(BLACK)

    turkey.render(SURFACE)

    if ticks % 6 == 0:
        turkey.switch_frame()

    pygame.display.update()
    fps_clock.tick(30)

    if ticks == 59:
        return 0
    else:
        return ticks + 1


TICKS = 0
while True:
    TICKS = update_game_state(TICKS)
