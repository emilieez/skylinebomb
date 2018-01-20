import pygame

import setup

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Blocker")

    screen = setup.get_screen()
    setup.draw_buildings(screen)
    plane = setup.get_plane(screen)
    bomb = setup.get_bomb(screen)

    while True:
        for event in pygame.event.get():
            setup.event_resolver(event, plane, bomb)

        plane.move()
        bomb.drop_bomb()
        pygame.display.update()
