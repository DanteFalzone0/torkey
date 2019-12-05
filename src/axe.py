import pygame

class Axe:
    def __init__(
        self,
        y_pos,
        image_paths_array
    ):
        self._x_pos = 600 # rightmost edge of the screen
        self._y_pos = y_pos
        self._image_frames = []
        for image_filename in image_paths_array:
            self._image_frames.append(
                pygame.image.load(
                    image_filename
                )
            )
        self._which_frame = 0


    def update(self, ticks):
        if (ticks + 1) % 5 == 0:
            if self._which_frame + 1 == len(self._image_frames):
                self._which_frame = 0
            else:
                self._which_frame += 1
        if self._x_pos <= 0:
            return 1
        else:
            self._x_pos -= 1
            return 0


    def render(self, pygame_surface):
        pygame_surface.blit(
            self._image_frames[self._which_frame],
            (self._x_pos, self._y_pos)
        )


    def reset_y_pos(self, value):
        self._x_pos = 600
        self._y_pos = value


    def get_y_pos(self):
        return self._y_pos


    def get_x_pos(self):
        return self._x_pos
