# -*- encoding: utf-8 -*-
import pygame
import utils

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
        self.quit_flag = False

    def loop(self):
        "Pone en funcionamiento el juego."


        while not self.quit_flag:

            # propaga eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                else:
                    self.scene.on_event(event)

            # actualiza la escena
            self.scene.on_update()
            pygame.time.delay(10)
        
            # dibuja la pantalla
            self.screen.fill((200, 200, 200))
            self.scene.on_draw(self.screen)
            pygame.display.flip()


    def change_scene(self, scene):
        "Altera la escena actual."
        self.scene = scene

    def quit(self):
        self.quit_flag = True
