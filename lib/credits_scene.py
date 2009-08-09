# -*- encoding: utf-8 -*-
import scene
import utils
import pygame
import presents_scene

class CreditScene(scene.Scene):
    """Muestra los nombres de los participantes del proyecto."""

    def __init__(self, director):
        scene.Scene.__init__(self, director)

        self.title , self.title_rect = utils.load_images("creditscene/title.png")
        
        self.font = utils.load_font("FreeSans.ttf",25)
        
        self.authors = ["Hugo Ruscitti", "Juanxo", "Dokan", "lacabra25", \
                        "Juan Carlos", "thepoi", "joksnet"]
                        
        self.rendered_authors = self.render_authors()


    def on_update(self):
        pass

    def on_draw(self, screen):
        self.title_rect.x = screen.get_width() / 2 - self.title_rect.width / 2
        self.title_rect.y = 10;
        screen.blit(self.title, self.title_rect)
        pos_y = self.title_rect.bottom + 50
        for author in self.rendered_authors:
            pos_x = screen.get_width() / 2 - author.get_rect().width / 2
            screen.blit(author, (pos_x, pos_y))
            pos_y += author.get_rect().height + 5

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.director.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                scene = presents_scene.PresentsScene(self.director)
                self.director.change_scene(scene)
    
    def render_authors(self):
        rendered_authors = []
        for author in self.authors:
            rendered_text = utils.render_text(author, self.font)[0]
            rendered_authors.append(rendered_text)
        return rendered_authors
