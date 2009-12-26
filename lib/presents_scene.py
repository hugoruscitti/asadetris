# -*- encoding: utf-8 -*-
import scene
import utils
import pygame
import game_scene
import credits_scene
import pytweener
import menu



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


class PresentsScene(scene.Scene):
    """Representa la escena de introducción al juego donde se muestra el logo.

    Esta escena es la primera que se ve al iniciar el juego."""

    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.title = Title()
        
        self.menu = menu.Menu(
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
