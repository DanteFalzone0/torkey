import pygame

class Apple:
    def __init__(self, y_pos, image_path):
        self._x_pos = 600 # rightmost edge of the screen
        self._y_pos = y_pos
        self.image = pygame.image.load(image_path)


    def update(self, turkey_x_pos):
        if self._x_pos <= 0:
            return 1
        else:
            self._x_pos -= 5
            return 0


    def render(self, pygame_surface):
        pygame_surface.blit(self.image, (self._x_pos, self._y_pos))


    def reset_y_pos(self, value):
        self._x_pos = 600
        self._y_pos = value


    def get_y_pos(self):
        return self._y_pos


    def get_x_pos(self):
        return self._x_pos
