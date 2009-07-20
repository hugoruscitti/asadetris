# -*- encoding: utf-8 -*-
import scene
import utils
import pygame
import presents_scene
import board


class GameScene(scene.Scene):
    """Representa la escena de juego.

    Esta escena es en la que el usuario interacciona con las piezas."""

    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.font = utils.load_font("FreeSans.ttf", 20)
        self.board = board.Board()
        self.background, tmp = utils.load_images("gamescene/background.png")

    def on_update(self):
        self.board.update()

    def on_draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.board.draw(screen)

    def on_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                scene = presents_scene.PresentsScene(self.director)
                self.director.change_scene(scene)
