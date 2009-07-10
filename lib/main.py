# -*- coding: utf-8 -*-
import pygame


def run():
    "Función principal del programa."

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Asadetris - 0.1")
    quit = False

    while not quit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True

        pygame.time.delay(10)


if __name__ == '__main__':
    run()
