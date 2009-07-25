# -*- encoding: utf-8 -*-
import pygame
import utils


class Board:
    "Representa el tablero donde se muestran las fichas"

    def __init__(self):
        self.pieces = []
        self.matrix = self.init_matrix(10, 18)

    def update(self):
        pass

    def draw(self, screen):
        pass

    def init_matrix(self, cells_width, cells_height):
        board = []

        for y in range(cells_height):
            line = []

            for x in range(cells_width):
                line.append(0)

            board.append(line)

        return board

    def can_put_this_piece_here(self, row, col, mask):
        """Informa si una pieza se puede colocar en una determinada posición.

        Este método evalua las colisiones de una pieza ante un posible
        movimiento."""

        for delta_row in range(0, 4):
            for delta_column in range(0, 4):

                if mask[delta_row][delta_column]:
                    dst_col = col - delta_column - 1

        # compara la máscara de la pieza con la matriz del tablero.


        return True
