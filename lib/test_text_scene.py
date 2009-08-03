# -*- encoding: utf-8 -*-
import director
import utils
import scene
import utils
import pygame


class TestTextScene(scene.Scene):
    """Un escena de prueba para el modulo de fuentes."""

    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.font = utils.load_font("FreeSans.ttf", 30)
        self.message, rect = utils.render_text("Una linea\nDos\nTres", self.font)

    def on_update(self):
        pass

    def on_draw(self, screen):
        screen.blit(self.message, (200, 200))
        pass
        
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.director.quit()
        elif event.type == pygame.KEYDOWN:
            self.director.quit()

if __name__ == '__main__':
    dir = director.Director()
    scene = TestTextScene(dir)
    dir.change_scene(scene)
    dir.loop()
