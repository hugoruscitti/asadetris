# -*- encoding: utf-8 -*-
import pygame
import scene
import utils
import board
import piece


class GameScene(scene.Scene):
    """Representa la escena de juego.

    Esta escena es en la que el usuario interacciona con las piezas."""

    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.board = board.Board()
        self.background, tmp = utils.load_images("gamescene/background.png")
        self.pieces = pygame.sprite.RenderUpdates()
        self.pieces.add(piece.Piece())

    def on_update(self):
        self.board.update()

    def on_draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.pieces.draw(screen)
        #self.board.draw(screen)

    def on_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._return_to_main_menu()

    def _return_to_main_menu(self):
        import presents_scene

        scene = presents_scene.PresentsScene(self.director)
        self.director.change_scene(scene)
