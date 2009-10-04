# -*- encoding: utf-8 -*-
import pygame
import utils
import sys

class Director:
    """Representa el objeto principal del juego.

    El objeto Director mantiene en funcionamiento el juego, se
    encarga de actualizar, dibuja y propagar eventos.

    Tiene que utilizar este objeto en conjunto con objetos
    derivados de Scene."""

    def __init__(self):
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Asadetris - 0.1")
        self.scene = None
        self.fullscreen = False
        self.quit_flag = False

        pygame.key.set_repeat(100, 100)

    def loop(self):
        "Pone en funcionamiento el juego."

        while not self.quit_flag:

            # propaga eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key in [pygame.K_F3, pygame.K_f]:
                            self.alternate_fullscreen()
                        elif event.key == pygame.K_q:
                            sys.exit(0)

                        self.scene.on_event(event)

            # actualiza la escena
            self.scene.on_update()
            pygame.time.delay(10)
        
            # dibuja la pantalla
            self.screen.fill((200, 200, 200))
            self.scene.on_draw(self.screen)
            pygame.display.flip()

    def alternate_fullscreen(self):
        self.set_fullscreen(not self.fullscreen)

    def set_fullscreen(self, mode):
        #TODO: utilizar el parametro mode
        pygame.display.toggle_fullscreen()

    def change_scene(self, scene):
        "Altera la escena actual."
        self.scene = scene

    def quit(self):
        self.quit_flag = True
