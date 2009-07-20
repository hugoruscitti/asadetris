# -*- encoding: utf-8 -*-
import pygame
import utils

"Constantes"
PIECE_L, PIECE_O, PIECE_T, PIECE_S, PIECE_Z, PIECE_J, PIECE_I = range(7)

class Board:
    "Representa el tablero donde se muestran las fichas"
    def __init__(self):
        self.pieces = []
        self.active_piece = Piece((240,0))
        self.game_rect = pygame.Rect(220, 80, 200, 380)
        self.board = self.init_board(10,19)

    def update(self):
        self.active_piece.update()

        if self.active_piece.on_ground():
            self.pieces.append(self.active_piece)
            self.active_piece = Piece((240,0))


    def draw(self, screen):
        screen.fill((0,0,0), self.game_rect)
        self.active_piece.draw(screen)
        for piece in self.pieces:
            piece.draw(screen)

    def init_board(self, cells_width, cells_height):
        board = []
        for y in range(cells_height):
            line = []
            for x in range(cells_width):
                line.append(' ')
            board.append(line)

        return board


class Piece():
    """Representa una pieza del tetris"""

    def __init__(self, letter = PIECE_L, pos = (220,0)):
        self.letter = letter
        self.image, self.rect = utils.load_images("brick.jpg", True)
        self.rect.x = pos [0]
        self.rect.y = pos [1]
        self.ground = False

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def on_ground(self):
        """self.ground = True en caso de que haya llegado al final
         o haya chocado"""
        return self.ground
