# -*- encoding: utf-8 -*-
import scene
import utils
import pygame
import presents_scene

class CreditScene(scene.Scene):
    """Muestra los nombres de los participantes del proyecto."""

    def __init__(self, director):
        scene.Scene.__init__(self, director)

        self.background, rect = utils.load_images("creditscene/background.png")
        self.font = utils.load_font("FreeSans.ttf", 25)
        
        self.authors = ["Hugo Ruscitti", "Juanxo", "Dokan", "lacabra25", \
                        "Juan Carlos", "thepoi", "joksnet", "Walter Velazquez"]
                        
        self.rendered_authors = self.render_authors()


    def on_update(self):
        pass

    def on_draw(self, screen):
        screen.blit(self.background, (0, 0))
        pos_y = 100
        for author in self.rendered_authors:
            pos_x = screen.get_width() / 2 - author.get_rect().width / 2
            screen.blit(author, (pos_x, pos_y))
            pos_y += author.get_rect().height + 5

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.director.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                scene = presents_scene.PresentsScene(self.director, 2)
                self.director.change_scene(scene)
    
    def render_authors(self):
        rendered_authors = []
        for author in self.authors:
            rendered_text = utils.render_text(author, self.font)[0]
            rendered_authors.append(rendered_text)
        return rendered_authors
