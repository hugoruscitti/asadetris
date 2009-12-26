# -*- encoding: utf-8 -*-
import scene
import utils
import pygame
import presents_scene
import menu

class OptionsScene(scene.Scene):

    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.background, rect = utils.load_images("options/background.png")
        self.menu = menu.Menu(
                [
                    ("Fullscreen", self.on_toggle),
                    ("Regresar", self.on_return),
                ])

    def on_update(self):
        self.menu.on_update()

    def on_draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.menu.on_draw(screen)

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.return_to_menu()
            if event.key == pygame.K_RETURN:
                self.menu.do_select()
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
                self.menu.do_select()

    def return_to_menu(self):
        scene = presents_scene.PresentsScene(self.director, 1)
        self.director.change_scene(scene)

    def on_toggle(self):
        pygame.display.toggle_fullscreen()

    def on_return(self):
        self.return_to_menu()
