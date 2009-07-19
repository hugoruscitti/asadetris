# -*- encoding: utf-8 -*-
import scene
import utils
import pygame
import presents_scene

class GameScene(scene.Scene):
    """Representa la escena de juego.

    Esta escena es en la que el usuario interacciona con las piezas."""

    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.font = utils.load_font("FreeSans.ttf", 30)
        msg = "Pantalla de juego"
        self.text, self.text_size = utils.render_text(msg, self.font)

    def on_update(self):
        pass

    def on_draw(self, screen):
        screen.blit(self.text, (180, 190))
        
    def on_event(self, event):

        if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				scene = presents_scene.PresentsScene(self.director)
				self.director.change_scene(scene)
