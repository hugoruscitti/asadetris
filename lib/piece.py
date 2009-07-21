# -*- encoding: utf-8 -*-
import pygame
import utils

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
        self.rect = (290, 100)

    def set_frame(self, index):
        self.image = self.frames[index]

    def update(self):
        pass
