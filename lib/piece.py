# -*- encoding: utf-8 -*-
import pygame
import utils
import os
from config import LEFT_CORNER, TOP_CORNER
import random


#"Constantes"
#PIECE_I, PIECE_J, PIECE_L, PIECE_O, PIECE_S, PIECE_T, PIECE_Z = range(7)

class PieceStatic(pygame.sprite.Sprite):

    def __init__(self, letter=None):
        pygame.sprite.Sprite.__init__(self)
        
        if None == letter:
            self.letter = random.randrange(7)
        else:
            self.letter = letter

        self.load_images("pieces/p" + str(self.letter) + ".png")
        self.load_matrix()
        self.set_frame(0)
        self.set_position_rect(0, 0)

    def load_matrix(self):
        """Carga todos los mapas de colision para la pieza.

        Inicialmente las piezas tienen asignado un archivo de texto
        que se almacena en el directorio 'mask'. El contenido
        de este archivo se convierte en una lista de matrices
        dentro de esta función.
        """
        dirname = os.path.dirname(os.path.abspath(__file__))
        filename = "p" + str(self.letter) + ".txt"
        handler = file(os.path.join(dirname, "../mask/", filename), "rt")
        content = handler.readlines()

        self.matrix_list = [
                self.create_mask(content[0:4]),
                self.create_mask(content[5:9]),
                self.create_mask(content[10:14]),
                self.create_mask(content[15:19]),
                ]

        handler.close()

    def create_mask(self, initial_mask):
        """Convierte una matriz de texto en una matriz numérica.

        Esta conversión realiza algo similar a lo siguiente::

            '..x.\n'          [0, 0, 1, 0]
            'xxx.\n'     -->  [1, 1, 1, 0]
            '....\n'     -->  [0, 0, 0, 0]
            '....\n'          [0, 0, 0, 0]

        La matriz de texto de la izquierda es útil para manipular
        desde un archivo de texto, pero la segunda es mas fácil
        de utilizar desde el código para hacer verificaciones.

        Esta función permite que los desarrolladores puedan definir
        las formas de fichas de manera sencilla desde un editor (estructura
        de la izquierda) y luego puedan convertirlas a datos mas
        fáciles de manipular dentro del código (estructura de la derecha).
        """

        matrix = []

        for line in initial_mask:
            new_line = []

            for c in line.strip():
                if c in ['x', 'X']:
                    new_line.append(1)
                else:
                    new_line.append(0)

            matrix.append(new_line)

        return matrix

    def load_images(self, path):
        image, rect = utils.load_images(path, True)
        w = rect.w / 4
        h = rect.h
        self.frames = [image.subsurface(x * w, 0, w, h) for x in range(0, 4)]

    def set_frame(self, index):
        self.image = self.frames[index]
        self.frame_index = index
        self.matrix = self.matrix_list[index]

    def _print_matrix(self, matrix):
        "Imprime una matriz a modo de depuración."
        for line in matrix:
            print line

    def set_position_rect(self, x, y):
        w = 80
        h = 80

        self.rect = pygame.Rect(x, y, w, h)

class Piece(PieceStatic):
    """Representa una pieza del tetris"""

    def __init__(self, board, speed, letter=None):
        PieceStatic.__init__(self, letter)

        self.board = board

        self.position_row = 1
        self.position_col = 5
        self.update_position_rect()
        self.speed = speed
        self.timer = 0

    def update(self):
        self.timer += 1

        if self.timer > 40 - self.speed * 5:
            self.timer = 0
            self.move(0, 1)

    def move(self, dx, dy):
        if dy > 0:
            self.timer = 0

        if self.can_move(dx, dy):
            self.position_col += dx
            self.position_row += dy
            self.update_position_rect()
        else:
            if dy > 0:
                print "Ha llegado al suelo."
                self.board.put_one_piece_here(self.position_row, 
                        self.position_col, self.image, self.matrix)
                self.board.go_to_next_piece()

    def can_move(self, dx, dy):
        """Informa si puede mover relativamente una pieza."""
        row = self.position_row + dy
        col = self.position_col + dx

        return self.board.can_put_this_piece_here(row, col, self.matrix)

    def update_position_rect(self):
        x = (self.position_col - 1) * 20
        y = (self.position_row - 1) * 20
        
        self.set_position_rect(LEFT_CORNER + x, TOP_CORNER + y)

    def rotate_to_left(self):
        self.rotate(-1)

    def rotate_to_right(self):
        self.rotate(1)

    def rotate(self, delta):
        posible_next_matrix = self.get_matrix_for_rotation(delta)
        row = self.position_row
        col = self.position_col

        if self.board.can_put_this_piece_here(row, col, posible_next_matrix):
            self.frame_index = (self.frame_index + delta) % 4
            self.set_frame(self.frame_index)
        else:
            print "Evitando rotar, la pieza no tiene espacio para girar."

    def get_matrix_for_rotation(self, delta):
        next_rotation_index = (self.frame_index + delta) % 4
        return self.matrix_list[next_rotation_index]
        
    def on_key_down_event(self, event):
        """Gestiona la pulsación de teclas para controlar la pieza."""

        if event.key == pygame.K_LEFT:
            self.move(-1, 0)
        elif event.key == pygame.K_RIGHT:
            self.move(1, 0)


        if event.key == pygame.K_UP:
            self.rotate_to_left()

        if event.key == pygame.K_z:
            self.rotate_to_left()
        elif event.key == pygame.K_x:
            self.rotate_to_right()

        if event.key == pygame.K_DOWN:
            self.move(0, 1)

        if event.key == pygame.K_SPACE:
            self.inmediate_fall()

    def inmediate_fall(self):
        "Hace caer la ficha inmediatamente."

        while self.can_move(0, 1):
            self.move(0, 1)

        self.move(0, 1)
