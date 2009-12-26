# -*- encoding: utf-8 -*-
import scene
import utils
import pygame
import game_scene
import credits_scene
import pytweener



class Title:

    def __init__(self):
        self.image, self.rect = utils.load_images("mainmenu/title.png")
        self.rect.right = 0
        self.tweener = pytweener.Tweener()
        self.x = - self.rect.width
        self.tweener.addTween(self, x=200, tweenTime=1,
                tweenType=pytweener.Easing.Elastic.easeOut)

    def on_draw(self, screen):
        self.rect.x = self.x
        screen.blit(self.image, self.rect)

    def on_update(self):
        self.tweener.update(0.01)

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
        self.title = Title()
        
        self.menu = Menu(
            ["Jugar!", "Creditos", "Salir"],
            utils.load_font("FreeSans.ttf", 30), (0, 0, 0),
            utils.load_font("FreeSans.ttf", 30), (255, 255, 255)
        )

    def on_update(self):
        self.title.on_update()

    def on_draw(self, screen):
        self.menu.on_draw(screen, 200)
        self.title.on_draw(screen)
        
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.director.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.select_option()
            elif event.key == pygame.K_UP:
                self.menu.prev()
            elif event.key == pygame.K_DOWN:
                self.menu.next()
            elif event.key == pygame.K_ESCAPE:
                self.director.quit()
        else:
            if event.type == pygame.JOYHATMOTION:
                x, y = event.value

                if y < -0.5:
                    self.menu.next()
                elif y > 0.5:
                    self.menu.prev()
            elif event.type == pygame.JOYBUTTONDOWN:
                self.select_option()

    def select_option(self):
        "Selecciona la opcion actual."

        if self.menu.selected == utils.JUGAR:
            scene = game_scene.GameScene(self.director)
            self.director.change_scene(scene)
        elif self.menu.selected == utils.CREDITOS:
            scene = credits_scene.CreditScene(self.director)
            self.director.change_scene(scene)
        elif self.menu.selected == utils.SALIR:
            self.director.quit()
