# -*- coding: utf-8 -*-

import pygame
import os

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
        image.set_colorkey(colorkey, RLEACCEL)
    else:
        image = image.convert_alpha()

    return image, image.get_rect()

def load_font(name, size):
    """Carga una fuente y la retorna"""

    fullname = os.path.join(DATOS, "../fonts", name)
    pygame.font.init()

    try:
        font = pygame.font.Font(fullname, size)
    except pygame.error, message:
        print 'No se ha podido cargar la fuente ', fullname
        raise message

        font = pygame.font.Font(None, size)
        print 'Cargando tipografía por defecto'

    return font

def render_text(text = '', font = None, antialias = False, color = (0,0,0), background = None):
    """Renderiza el texto retornando el texto renderizado y sus dimensiones"""
    if background != None:
        try:
            rendered_text = font.render(text, antialias, color, background)
        except pygame.error, message:
            print 'No se ha podido renderizar el texto ', text
            raise SysExit, message
            
    else:
        try:
            rendered_text = font.render(text, antialias, color)
        except pygame.error, message:
            print 'No se ha podido renderizar el texto ', text
            raise SysExit, message
    
    return rendered_text, font.size(text)
