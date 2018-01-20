import pygame

from constants import *


class Bomb:
    drop = False

    def __init__(self, surface, color, pos, radius, width=0):
        self.surface = surface
        self.color = color
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.radius = radius
        self.width = width

        self.bomb = pygame.Surface((radius, width))
        self.bomb.fill(PLANE_COLOUR)

    def draw(self, x_pos, y_pos):
        pygame.draw.circle(self.surface, self.color, (x_pos, y_pos), self.radius, 0)

    def erase(self, x_pos, y_pos):
        curr_eraser_radius = self.radius
        if curr_eraser_radius < 155 and y_pos == SCREEN_HEIGHT - self.radius:
            curr_eraser_radius += 155
        pygame.draw.circle(self.surface, BLACK, (x_pos, y_pos), curr_eraser_radius, 0)

    def drop_bomb(self):
        if self.y_pos <= SCREEN_HEIGHT + self.radius and Bomb.drop:
            self.erase(self.x_pos, self.y_pos)
            self.y_pos += 1
            self.draw(self.x_pos, self.y_pos)
