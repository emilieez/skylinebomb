import pygame

import environment

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Blocker")
    environment.draw_buildings()

    while True:
        for event in pygame.event.get():
            environment.event_resolver(event)

        environment.plane.move()
        environment.bomb.drop_bomb()
        pygame.display.update()
