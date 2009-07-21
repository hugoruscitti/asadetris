# -*- encoding: utf-8 -*-
import pygame
import utils


class Board:
    "Representa el tablero donde se muestran las fichas"

    def __init__(self):
        self.pieces = []
        #self.active_piece = Piece((240,0))
        self.game_rect = pygame.Rect(220, 80, 200, 380)
        self.board = self.init_board(10,19)

    def update(self):
        pass
        #self.active_piece.update()

        #if self.active_piece.on_ground():
        #    self.pieces.append(self.active_piece)
        #    self.active_piece = Piece((240,0))


    def draw(self, screen):
        pass
        #screen.fill((0,0,0), self.game_rect)

        #self.active_piece.draw(screen)

        #for piece in self.pieces:
        #    piece.draw(screen)

    def init_board(self, cells_width, cells_height):
        board = []

        for y in range(cells_height):
            line = []
            for x in range(cells_width):
                line.append(' ')
            board.append(line)

        return board
