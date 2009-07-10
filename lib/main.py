import pygame


def run():

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Asadetris")
    quit = False

    while not quit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True


        pygame.time.delay(10)
