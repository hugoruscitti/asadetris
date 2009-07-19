# -*- encoding: utf-8 -*-
import scene
import utils
import pygame

class PresentsScene(scene.Scene):
    """Representa la escena de introducción al juego donde se muestra el logo.

    Esta escena es la primera que se ve al iniciar el juego."""

    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.title, self.rect = utils.load_images("mainmenu/title.png")
        self.font = utils.load_font("Dejavu.ttf", 30)
        msg = "Pulse una tecla para salir"
        self.text, self.text_size = utils.render_text(msg, self.font)

    def on_update(self):
        pass

    def on_draw(self, screen):
        screen.blit(self.title, (180, 20))
        screen.blit(self.text, (180, 190))
        
    def on_event(self, event):

        if event.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
            self.director.quit()
