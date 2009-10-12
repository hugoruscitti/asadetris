# -*- encoding: utf-8 -*-
import pygame
import scene
import utils
import board
import piece
import display


class GameScene(scene.Scene):
    """Representa la escena de juego.

    Esta escena es en la que el usuario interacciona con las piezas."""

    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.running = True
        self.current_message = None
        self.current_message_rect = None
        self.board = board.Board(self)
        self.display = display.Display()
        self.background, tmp = utils.load_images("gamescene/background.png")
        self.pieces = piece.Group()
        self.game_speed = 0
        self.go_to_next_piece()
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
        self.display.draw(screen)
        self.pieces.draw(screen)
        self.board.draw(screen)
        screen.blit(self.return_message, (8, 460))
        
        if self.current_message:
            x = ( 640 - self.current_message_rect.w ) / 2
            y = ( 480 - self.current_message_rect.h ) / 2
            
            # screen.set_alpha(150)
            screen.blit(self.current_message, (x, y))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.director.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._return_to_main_menu()
            else:
                self.emit_on_key_down_event_to_pieces(event)
        elif event.type == pygame.JOYBUTTONDOWN:
            self.emit_joybutton_event_to_pieces(event)
        elif event.type == pygame.JOYHATMOTION:
            self.emit_joyhatmotion_event_to_pieces(event)

    def emit_on_key_down_event_to_pieces(self, event):
        for piece in self.pieces.sprites():
            piece.on_key_down_event(event)

    def emit_joyhatmotion_event_to_pieces(self, event):
        for piece in self.pieces.sprites():
            piece.on_joyhatmotion_event(event)

    def emit_joybutton_event_to_pieces(self, event):
        for piece in self.pieces.sprites():
            piece.on_joybutton_event(event)

    def _return_to_main_menu(self):
        import presents_scene

        scene = presents_scene.PresentsScene(self.director)
        self.director.change_scene(scene)

    def go_to_next_piece(self):
        if self.running:
            nextp = piece.Piece(self.board, self.game_speed, 
                    self.display.get_next_piece_letter())
            self.pieces.add(nextp)
            self.display.set_next_piece()

    def on_line_complete(self):
        self.display.on_line_complete()
        self.game_speed = self.display.level * 2

    def pause(self):
        self.running = False
        self.pieces.empty()

    def show_message(self, text):
        font = utils.load_font("FreeSans.ttf", 14)
        self.current_message, self.current_message_rect = utils.render_text(text, font)
