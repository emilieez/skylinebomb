import pygame

from constants import *


class Plane:
    curr_direction = False

    def __init__(self, screen, width, height, initial_x, initial_y):
        self.height = height
        self.width = width
        self.x_pos = initial_x
        self.y_pos = initial_y
        self.screen = screen

        self.block = pygame.Surface((width, height))
        self.block.fill(GREEN)
        self.whiteblock = pygame.Surface((width, height))
        self.whiteblock.fill(WHITE)

    def erase(self):
        self.screen.blit(self.whiteblock, (self.x_pos, self.y_pos))

    def draw(self):
        self.screen.blit(self.block, (self.x_pos, self.y_pos))

    # TODO: refactor continous move
    def move(self, distance):
        self.erase()
        if self.x_pos != 0 and self.x_pos != SCREEN_HEIGHT:
            if not Plane.curr_direction:
                self.x_pos -= distance
            else:
                self.x_pos += distance
        else:
            Plane.curr_direction = not Plane.curr_direction
            if Plane.curr_direction:
                self.x_pos += distance
            else:
                self.x_pos -= distance

        self.draw()

        # self.erase()
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_h]:
        #     self.x_pos -= distance
        # if keys[pygame.K_j]:
        #     self.y_pos += distance
        # if keys[pygame.K_l]:
        #     self.x_pos += distance
        # if keys[pygame.K_k]:
        #     self.y_pos -= distance
        # self.draw()