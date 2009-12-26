# -*- encoding: utf-8 -*-
import utils

class Menu:

    def __init__(self, opts, font, color, selected_font, selected_color, margin=0):
        self.opts = opts
        self.normal_font = font
        self.normal_color = color
        self.selected_font = selected_font
        self.selected_color = selected_color
        self.margin = margin
        
        self.selected = utils.JUGAR
        self.imgs_normal = []
        self.imgs_selected = []
        
        line_step = 0
        
        for text in self.opts:
            img_normal, img_normal_size = utils.render_text(text, self.normal_font, self.normal_color)
            img_selected, img_selected_size = utils.render_text(text, self.selected_font, self.selected_color)
            
            self.imgs_normal.append(img_normal)
            self.imgs_selected.append(img_selected)
            
            line_step = max(max(img_normal_size[3], img_selected_size[3]) + self.margin, line_step)
        
        self.line_step = line_step
    
    def on_draw(self, screen, start_y):
        center_x = screen.get_width() / 2
        
        for i in range(len(self.opts)):
            if i == self.selected:
                img = self.imgs_selected[i]
            else:
                img = self.imgs_normal[i]
            
            x = center_x - img.get_width() / 2
            y = start_y + self.line_step * i - img.get_height() / 2
            
            screen.blit(img, (x,y))
    
    def prev(self):
        self.selected = (self.selected - 1) % len(self.opts)
    
    def next(self):
        self.selected = (self.selected + 1) % len(self.opts)
