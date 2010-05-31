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
        self.font = utils.load_font("FreeSans.ttf", 20)
        
        self.program = ["Hugo Ruscitti", "Juanxo", "Dokan", "lacabra25", 
                        "Juan Carlos", "thepoi", "joksnet"]
        self.art = ["Walter Velazquez"]
                        
        self.rendered_program = self.render_authors(self.program)
        self.rendered_art = self.render_authors(self.art)


    def on_update(self):
        pass

    def on_draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.render_names(screen, self.rendered_program, 60, 150)
        self.render_names(screen, self.rendered_art, 400, 150)

    def render_names(self, screen, names, x, y):
        "Imprime una lista de imagenes (con nombres de personas) sobre screen."

        for author in names:
            screen.blit(author, (x, y))
            y += author.get_rect().height + 5

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.director.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                scene = presents_scene.PresentsScene(self.director, 2)
                self.director.change_scene(scene)
    
    def render_authors(self, names):
        rendered_authors = []

        for author in names:
            rendered_text = utils.render_text(author, self.font)[0]
            rendered_authors.append(rendered_text)

        return rendered_authors
