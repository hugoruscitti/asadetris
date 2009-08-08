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
        self.board = board.Board(self)
        self.background, tmp = utils.load_images("gamescene/background.png")
        self.pieces = pygame.sprite.GroupSingle()
        self.pieces.add(piece.Piece(self.board))
        self.create_return_message()

    def create_return_message(self):
        font = utils.load_font("FreeSans.ttf", 14)
        text = "Pulse ESC para regresar al menu"
        self.return_message, rect = utils.render_text(text, font)

    def on_update(self):
        self.board.update()
        self.pieces.update()

    def on_draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.pieces.draw(screen)
        self.board.draw(screen)
        screen.blit(self.return_message, (8, 460))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.director.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._return_to_main_menu()
            else:
                self.emit_on_key_down_event_to_pieces(event)

    def emit_on_key_down_event_to_pieces(self, event):
        for piece in self.pieces.sprites():
            piece.on_key_down_event(event)

    def _return_to_main_menu(self):
        import presents_scene

        scene = presents_scene.PresentsScene(self.director)
        self.director.change_scene(scene)

    def go_to_next_scene(self):
        self.pieces.add(piece.Piece(self.board))
