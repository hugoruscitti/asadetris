# -*- encoding: utf-8 -*-
import pygame
import utils

class Display:
    """Representa el contador de lineas y la siguiente pieza a manejar."""

    def __init__(self):
        self.lines = 0
        self.update_image()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def on_line_complete(self):
        self.lines += 1
        self.update_image()

    def update_image(self):
        font = utils.load_font("FreeSans.ttf", 30)
        text = "Lines: %d" %(self.lines)
        self.image, self.rect = utils.render_text(text, font)
        self.rect.right = 630
