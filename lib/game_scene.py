# -*- encoding: utf-8 -*-
import pygame
import scene
import utils
import pytweener
import board
import piece
import display
import game_scene_messages
from config import LEFT_CORNER, TOP_CORNER
DELAY_LINE_COMPLE_EFFECT = 30


class LineAnimation:

    def __init__(self, lines):
        self.lines = lines
        self.count = 0

    def draw(self, screen):
        self.count += 1

        for line in self.lines:
            self.blit_rect(screen, line)

    def blit_rect(self, screen, line):
        rect = pygame.Rect((LEFT_CORNER, TOP_CORNER + line * 20, 20 * 10, 20))

        if self.count % 10 <= 5:
            color = (255, 255, 255)
        else:
            color = (100, 100, 100)

        screen.fill(color, rect)


class GameScene(scene.Scene):
    """Representa la escena de juego.

    Esta escena es en la que el usuario interacciona con las piezas."""

    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.graphic_message = None
        self.running = True
        self.delay_showing_line_animation = 0
        self.current_message = None
        self.current_message_rect = None
        self.board = board.Board(self)
        self.display = display.Display()
        self.background, tmp = utils.load_images("gamescene/background.png")
        self.pieces = piece.Group()
        self.game_speed = 0
        self.create_return_message()
        self.show_graphic_message(game_scene_messages.AreYouReadyMessage(self))
        self.line_animation = None
        self.delay_showing_line_animation = 0

    def unpause_and_start_to_play(self):
        self.running = True
        self.go_to_next_piece()

    def create_return_message(self):
        font = utils.load_font("FreeSans.ttf", 14)
        text = "Pulse ESC para regresar al menu"
        self.return_message, rect = utils.render_text(text, font)

    def on_update(self):

        if self.delay_showing_line_animation:
            self.delay_showing_line_animation -= 1
        else:
            if self.running:
                self.board.update()
                self.pieces.update()

        if self.graphic_message:
            self.graphic_message.on_update()

    def on_draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.display.draw(screen)
        self.pieces.draw(screen)
        self.board.draw(screen)
        screen.blit(self.return_message, (8, 460))

        # muestra la animacion de las lineas que se han
        # eliminando.
        if self.delay_showing_line_animation:
            self.line_animation.draw(screen)

            if self.delay_showing_line_animation == 1:
                self.board.remove_complete_lines()

        if self.graphic_message:
            self.graphic_message.on_draw(screen)
        
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
	        if self.running:
                    self._return_to_main_menu()
                else:
		    self.graphic_message = None
		    self.running = True
            elif event.key == pygame.K_p:
	        if self.running:
        	    self.on_game_pause()
		else:
		    self.graphic_message = None
		    self.running = True
            else:
                self.emit_on_key_down_event_to_pieces(event)
        elif event.type == pygame.JOYBUTTONDOWN:
            self.emit_joybutton_event_to_pieces(event)
        elif event.type == pygame.JOYHATMOTION:
            self.emit_joyhatmotion_event_to_pieces(event)

    def emit_on_key_down_event_to_pieces(self, event):
        if self.running:
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

        scene = presents_scene.PresentsScene(self.director, 0)
        self.director.change_scene(scene)

    def go_to_next_piece(self):
        if self.running:
            nextp = piece.Piece(self.board, self.game_speed, 
                    self.display.get_next_piece_letter())
            self.pieces.add(nextp)
            self.display.set_next_piece()

    def on_line_complete(self, lines):
        self.line_animation = LineAnimation(lines)
        for line in lines:
            self.display.on_line_complete()

        # aumenta la velocidad del juego
        self.game_speed = (self.display.level * 2)
	print self.game_speed
        self.delay_showing_line_animation = DELAY_LINE_COMPLE_EFFECT

    def pause(self):
        self.running = False
        self.pieces.empty()

    def show_message(self, text):
        font = utils.load_font("FreeSans.ttf", 14)
        self.current_message, self.current_message_rect = utils.render_text(text, font)

    def show_graphic_message(self, message_object):
        """Muestra un mensaje a partir de una imagen.

        Detiene el juego hasta que el mensaje desaparece de la escena."""
        self.graphic_message = message_object

    def on_game_over(self):
        self.show_graphic_message(game_scene_messages.GameOverMessage(self))
	
    def on_game_pause(self):
        self.running = False
        self.show_graphic_message(game_scene_messages.PauseMessage(self))
