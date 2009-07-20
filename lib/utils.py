# -*- coding: utf-8 -*-

import pygame
import os



"""Definimos las constantes"""
JUGAR = 0
CREDITOS = 1
SALIR = 2

DATOS = os.path.dirname(os.path.abspath(__file__))

def load_images(name, colorkey = False):
    """Carga una imagen retornando una superficie y su rectangulo.  """

    fullname = os.path.join(DATOS, "../images", name)

    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'No se ha podido cargar la imagen ', fullname
        raise SystemExit, message


    if colorkey:
        colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    else:
        image = image.convert_alpha()

    return image, image.get_rect()

def load_font(name, size):
    """Carga una fuente y la retorna"""

    fullname = os.path.join(DATOS, "../fonts", name)
    pygame.font.init()

    try:
        font = pygame.font.Font(fullname, size)
    except IOError:
        print 'No se ha podido cargar la fuente ', fullname
        #raise message

        font = pygame.font.Font(None, size)
        print 'Cargando tipografía por defecto'

    return font

def render_text(text, font, color=(0,0,0), background=None):
    """Renderiza el texto retornando el texto renderizado y sus dimensiones"""
    antialias = True

    if background:
        rendered_text = font.render(text, antialias, color, background)
    else:
        rendered_text = font.render(text, antialias, color)
    
    return rendered_text, font.size(text)
