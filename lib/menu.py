# -*- encoding: utf-8 -*-
import pygame
import utils


class Cursor:

    def __init__(self, start_y, item_height):
        self.image = pygame.Surface((200, 40))
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = 320
        self.start_y = start_y
        self.item_height = item_height

        self.set_position(0)

    def on_draw(self, screen):
        screen.blit(self.image, self.rect)

    def set_position(self, index):
        self.rect.y = self.start_y + index * self.item_height
    
    def on_update(self):
        pass


class Menu:

    def __init__(self, opts):
        self.opts = opts

        selected_font = utils.load_font("FreeSans.ttf", 30)
        selected_color = (255, 255, 255)
        font = utils.load_font("FreeSans.ttf", 30)
        color = (0, 0, 0)

        self.normal_font = font
        self.normal_color = color
        self.selected_font = selected_font
        self.selected_color = selected_color
        self.start_y = 200
        self.item_height = 50

        self.cursor = Cursor(self.start_y, self.item_height)
        
        self.selected = utils.JUGAR
        self.imgs_normal = []
        self.imgs_selected = []
        
        
        self._create_option_images()

    def on_update(self):
        self.cursor.on_update()

    def _create_option_images(self):
        "Genera todos los items del menú."
        line_step = 0

        for text in self.opts:
            img_normal, img_normal_size = utils.render_text(text, self.normal_font, 
                    self.normal_color)
            img_selected, img_selected_size = utils.render_text(text, 
                    self.selected_font, self.selected_color)
            
            self.imgs_normal.append(img_normal)
            self.imgs_selected.append(img_selected)
            
            line_step = max(max(img_normal_size[3], img_selected_size[3]), line_step)
        
        self.line_step = line_step
    
    def on_draw(self, screen):
        center_x = screen.get_width() / 2
        
        self.cursor.on_draw(screen)

        for i in range(len(self.opts)):
            if i == self.selected:
                img = self.imgs_selected[i]
            else:
                img = self.imgs_normal[i]
            
            x = center_x - img.get_width() / 2
            y = self.start_y + i * self.item_height
            
            screen.blit(img, (x,y))

    
    def prev(self):
        self.selected = (self.selected - 1) % len(self.opts)
        self.cursor.set_position(self.selected)
    
    def next(self):
        self.selected = (self.selected + 1) % len(self.opts)
        self.cursor.set_position(self.selected)
