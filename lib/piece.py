# -*- encoding: utf-8 -*-
import pygame
import utils
import os
from config import LEFT_CORNER, TOP_CORNER
import random


class Group(pygame.sprite.GroupSingle):

    def __init__(self):
        pygame.sprite.GroupSingle.__init__(self)

    def draw(self, screen):
        for s in self.sprites():
            s.draw(screen)



class PieceStatic(pygame.sprite.Sprite):

    def __init__(self, letter=None):
        pygame.sprite.Sprite.__init__(self)
        self.current_angle = 0
        self.frame_index = 0
        
        if None == letter:
            self.letter = random.randrange(7)
        else:
            self.letter = letter

        self.load_images(self.letter)
        self.load_matrix()
        self.set_animation_frame(0)
        self.set_frame(0)
        self.set_position_rect(0, 0)

    def draw(self, screen):
        rect = pygame.Rect(self.rect)
        image_rect = self.image.get_rect()

        center = rect.center
        image_rect.center =center
        screen.blit(self.image, image_rect)


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

    def load_images(self, letter):
        self.frames = []

        for x in range(0, 360, 30):
            filename = "pieces/p%d/%d_%d.png" %(letter, letter, x)
            image, rect = utils.load_images(filename, True)
            self.frames.append(image)

        w = rect.w / 4
        h = rect.h

    def set_frame(self, index):
        self.original_image = self.frames[index * 3]
        #self.image = self.frames[index * 3]
        self.frame_index = index
        self.matrix = self.matrix_list[index]

    def set_animation_frame(self, index):
        self.image = self.frames[index]

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
        self.animation = [0]
        self.delay = 10
        self.step = 0
        self.rotate_direction = 0

    def update(self):
        self.timer += 1

        if self.timer > 40 - self.speed * 5:
            self.timer = 0
            self.move(0, 1)

        self.update_animation()

    def update_animation(self):
        if self.delay <= 0:
            self.delay = 1
            
            if self.animation:
                next_frame = self.animation.pop(0)
                self.set_animation_frame(next_frame)
        else:
            self.delay -= 1


    def move(self, dx, dy):
        if dy > 0:
            self.timer = 0

        if self.can_move(dx, dy):
            self.position_col += dx
            self.position_row += dy
            self.update_position_rect()
        else:
            if dy > 0:
                # Ha llegado al suelo
                self.board.put_one_piece_here(self)
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
        self.rotate_direction = delta

        if self.board.can_put_this_piece_here(row, col, posible_next_matrix):
            last_frame = self.frame_index
            next_frame = (self.frame_index + delta) % 4
            self.start_animation(last_frame, next_frame)
            self.frame_index = next_frame
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
            self.inmediate_fall()

        if event.key == pygame.K_z:
            self.rotate_to_left()
        elif event.key == pygame.K_x:
            self.rotate_to_right()

        if event.key == pygame.K_DOWN:
            self.move(0, 1)

        if event.key == pygame.K_SPACE:
            self.inmediate_fall()

    def on_joyhatmotion_event(self, event):
        dx, dy = event.value

        if dy > 0.5:
            self.inmediate_fall()
        else:
            self.move(dx, -dy)


    def on_joybutton_event(self, event):
        button = event.button

        if button in [3, 0]:
            self.rotate_to_left()
        elif button in [2, 1]:
            self.rotate_to_right()

    def inmediate_fall(self):
        "Hace caer la ficha inmediatamente."

        while self.can_move(0, 1):
            self.move(0, 1)

        self.move(0, 1)

    def start_animation(self, last_frame, next_frame):
        last_frame *= 3 
        next_frame *= 3

        if self.rotate_direction > 0:
            if last_frame == 0:
                animation = [0, 1, 2, 3]
            elif last_frame == 3:
                animation = [3, 4, 5, 6]
            elif last_frame == 6:
                animation = [6, 7, 8, 9]
            elif last_frame == 9:
                animation = [9, 10, 11, 0]
        else:
            if last_frame == 9:
                animation = [9, 8, 7, 6]
            elif last_frame == 6:
                animation = [6, 5, 4, 3]
            elif last_frame == 3:
                animation = [3, 2, 1, 0]
            elif last_frame == 0:
                animation = [0, 11, 10, 9]

        self.animation = animation
