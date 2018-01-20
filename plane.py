import pygame

from constants import *


class Plane:
    curr_direction = False
    curr_displacement = INITIAL_DISTANCE
    stopped = False

    def __init__(self, screen, width, height, initial_x, initial_y):
        self.height = height
        self.width = width
        self.x_pos = initial_x
        self.y_pos = initial_y
        self.screen = screen

        self.block = pygame.Surface((width, height))
        self.block.fill(PLANE_COLOUR)
        self.whiteblock = pygame.Surface((width, height))
        self.whiteblock.fill(WHITE)

    def erase(self):
        self.screen.blit(self.whiteblock, (self.x_pos, self.y_pos))

    def draw(self):
        self.screen.blit(self.block, (self.x_pos, self.y_pos))

    def perform_key_events(self, evkey):
        # left and right arrow to change speed
        if evkey == pygame.K_LEFT:
            Plane.curr_displacement = Plane.curr_displacement / 2
            self.x_pos -= Plane.curr_displacement
        if evkey == pygame.K_RIGHT:
            Plane.curr_displacement = Plane.curr_displacement * 2
            self.x_pos += Plane.curr_displacement
        # space to stop the plane
        if evkey == pygame.K_SPACE:
            Plane.stopped = not Plane.stopped

    # TODO: refactor continuous move (SCREEN_WIDTH - CURR_DISPLACEMENT + 10) % 10
    def move(self):
        self.erase()
        if not Plane.stopped:
            if 0 <= self.x_pos <= SCREEN_WIDTH - self.width / 2:
                if not Plane.curr_direction:
                    self.x_pos -= Plane.curr_displacement
                else:
                    self.x_pos += Plane.curr_displacement
            else:
                Plane.curr_direction = not Plane.curr_direction
                if Plane.curr_direction:
                    self.x_pos += Plane.curr_displacement
                else:
                    self.x_pos -= Plane.curr_displacement
        self.draw()
