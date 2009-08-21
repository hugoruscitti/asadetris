# -*- encoding: utf-8 -*-
import pygame
import utils
from config import LEFT_CORNER, TOP_CORNER


class Board:
    "Representa el tablero donde se muestran las fichas"

    def __init__(self, gamescene):
        self.pieces = []
        self.visual_matrix = pygame.Surface((10 * 20, 18 * 20), pygame.SRCALPHA, 32)
        self.matrix = self.init_matrix(10, 18)
        self.gamescene = gamescene

    def update(self):
        pass

    #def draw_block(self, row, col):
    #    color = (200, 200, 0)
    #    self.visual_matrix.fill(color, (col * 20, row * 20, 20, 20))

    def draw(self, screen):
        screen.blit(self.visual_matrix, (LEFT_CORNER, TOP_CORNER))

    def init_matrix(self, cells_width, cells_height):
        "Inicializa la matriz de colisiones invisible al usuario."
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
                    dst_col = col - 1 + delta_column
                    dst_row = row - 1 + delta_row

                    if dst_col < 0:
                        return False

                    try:
                        if self.matrix[dst_row][dst_col]:
                            return False
                    except IndexError:
                        return False

        return True

    def _update_matrix_putting_a_new_piece(self, row, col, mask):
        # define como colisionables los bloques que ocupará la pieza.
        for delta_row in range(0, 4):
            for delta_column in range(0, 4):

                if mask[delta_row][delta_column]:
                    dst_col = col - 1 + delta_column
                    dst_row = row - 1 + delta_row

                    self.matrix[dst_row][dst_col] = mask[delta_row][delta_column]
                    #self.draw_block(dst_row, dst_col)

    def put_one_piece_here(self, row, col, image, mask):
        """Suelta una pieza en determinada parte del escenario."""

        self._update_matrix_putting_a_new_piece(row, col, mask)
        # dibuja la pieza en donde cae.
        self.visual_matrix.blit(image, ((col - 1)  * 20, (row -1) * 20))

        print "Asi queda la matriz luego de colocar la pieza."
        import pprint
        pprint.pprint(self.matrix)

        self.check_lines()

    def go_to_next_piece(self):
        self.gamescene.go_to_next_scene()

    def check_lines(self):
        for row in range(len(self.matrix)):
            width = len(self.matrix[row])
            cwidth = 0

            for col in range(width):
                if self.matrix[row][col] == 1:
                    cwidth += 1

            if cwidth == width:
                print "LINE at ROW %d" % (row)
