# -*- coding: utf-8 -*-
import pygame
import utils


def run():
    "Función principal del programa."

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Asadetris - 0.1")
    quit = False

    title, rect = utils.load_images("mainmenu/title.png")

    while not quit:
        screen.fill((200, 200, 200))
        screen.blit(title, (180, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True

        pygame.display.flip()
        pygame.time.delay(10)


if __name__ == '__main__':
    run()
