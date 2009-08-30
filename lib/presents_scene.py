# -*- encoding: utf-8 -*-
import scene
import utils
import pygame
import game_scene
import credits_scene

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

class PresentsScene(scene.Scene):
    """Representa la escena de introducción al juego donde se muestra el logo.

    Esta escena es la primera que se ve al iniciar el juego."""

    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.title, self.rect = utils.load_images("mainmenu/title.png")
        
        self.menu = Menu(
            ["Jugar!", "Creditos", "Salir"],
            utils.load_font("FreeSans.ttf", 30), (0, 0, 0),
            utils.load_font("FreeSans.ttf", 30), (255, 255, 255)
        )

    def on_update(self):
        pass

    def on_draw(self, screen):
        screen.blit(self.title, (180, 20))
        self.menu.on_draw(screen, 20 + self.title.get_height() + 40)
        
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.director.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if self.menu.selected == utils.JUGAR:
                    scene = game_scene.GameScene(self.director)
                    self.director.change_scene(scene)
                elif self.menu.selected == utils.CREDITOS:
                    scene = credits_scene.CreditScene(self.director)
                    self.director.change_scene(scene)
                elif self.menu.selected == utils.SALIR:
                    self.director.quit()
            elif event.key == pygame.K_UP:
                self.menu.prev()
            elif event.key == pygame.K_DOWN:
                self.menu.next()
            elif event.key == pygame.K_ESCAPE:
                self.director.quit()
