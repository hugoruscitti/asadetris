# -*- encoding: utf-8 -*-
import scene
import utils
import pygame
import presents_scene
import engine
class GameScene(scene.Scene):
    """Representa la escena de juego.

    Esta escena es en la que el usuario interacciona con las piezas."""

    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.font = utils.load_font("FreeSans.ttf", 20)
        msg = "Pantalla de juego"
        self.text, self.text_size = utils.render_text(msg, self.font)
        self.board = engine.Board()

    def on_update(self):
        self.board.update()

    def on_draw(self, screen):
        screen.fill((150, 150, 150))
        screen.blit(self.text, (10, 190))
        self.board.draw(screen)


    def on_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                scene = presents_scene.PresentsScene(self.director)
                self.director.change_scene(scene)
