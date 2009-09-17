# -*- encoding: utf-8 -*-
import pygame
import utils
import piece

class Display:
    """Representa el contador de lineas y la siguiente pieza a manejar."""

    def __init__(self):
        self.rect = pygame.Rect((480, 20, 140, 300))
        
        self.lines = 0
        self.level = 0
        self.update_image()
        
        self.pieces_next = pygame.sprite.GroupSingle()
        self.set_next_piece()

    def draw(self, screen):
        color = (250, 250, 250)
        screen.fill(color, self.rect)
        
        screen.blit(self.image, self.image_rect)
        self.pieces_next.draw(screen)

    def on_line_complete(self):
        self.lines += 1
        self.update_image()

        # el nivel avanza cada 10 lineas.
        self.level = self.lines / 10
        print "Con %d lineas le corresponde el nivel %d" %(self.lines, self.level)

    def update_image(self):
        font = utils.load_font("FreeSans.ttf", 30)
        text = "Lines: %d" %(self.lines)
        self.image, self.image_rect = utils.render_text(text, font)
        self.image_rect.move_ip(self.rect.x + ((self.rect.w - self.image_rect.w) / 2), self.rect.y + 10)

    def set_next_piece(self):
        nextp = piece.PieceStatic()
        nextp.set_position_rect(self.rect.x + ((self.rect.w - nextp.rect.w) / 2), self.rect.y + self.image_rect.h + 20)
        
        self.pieces_next.add(nextp)

    def get_next_piece_letter(self):
        return self.pieces_next.sprites().pop().letter
