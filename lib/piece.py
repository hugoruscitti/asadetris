# -*- encoding: utf-8 -*-
import pygame
import utils

LEFT_CORNER = 223
TOP_CORNER = 97



"Constantes"
PIECE_L, PIECE_O, PIECE_T, PIECE_S, PIECE_Z, PIECE_J, PIECE_I = range(7)

class Piece(pygame.sprite.Sprite):
    """Representa una pieza del tetris"""

    def __init__(self, letter = PIECE_L):
        pygame.sprite.Sprite.__init__(self)
        self.letter = letter
        self.load_images("pieces/p2.png")
        self.set_frame(0)

    def load_images(self, path):
        image, rect = utils.load_images(path, True)
        w = rect.w / 4
        h = rect.h
        self.frames = [image.subsurface(x * w, 0, w, h) for x in range(0, 4)]
        self.rect = pygame.Rect(LEFT_CORNER + 20 * 3, TOP_CORNER, w, h)

    def set_frame(self, index):
        self.image = self.frames[index]
        self.frame_index = index

    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.move(-1, 0)
        elif key[pygame.K_RIGHT]:
            self.move(1, 0)

        if key[pygame.K_DOWN]:
            self.move(0, 1)
        elif key[pygame.K_UP]:
            self.move(0, -1)

        if key[pygame.K_z]:
            self.rotate_to_left()
        elif key[pygame.K_x]:
            self.rotate_to_right()

    def move(self, dx, dy):
        self.rect.move_ip(dx * 20, dy * 20)
        # TODO: quitar este delay...
        pygame.time.delay(100)

    def rotate_to_left(self):
        self.rotate(-1)
        # TODO: quitar este delay...
        pygame.time.delay(100)

    def rotate_to_right(self):
        self.rotate(1)
        # TODO: quitar este delay...
        pygame.time.delay(100)
        

    def rotate(self, delta):
        self.frame_index = (self.frame_index + delta) % 4
        self.set_frame(self.frame_index)

        

