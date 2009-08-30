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
    interline = 5               # Distancia entre lineas
    lines = []

    # Genera una lista con todas las lineas de texto.
    for line in text.split('\n'):

        if background:
            rendered_text = font.render(line, antialias, color, background)
        else:
            rendered_text = font.render(line, antialias, color)

        lines.append(rendered_text)
    
    # calcula el tamaño de la imagen final.
    width = max([s.get_width() for s in lines])
    height = sum([s.get_height() + interline for s in lines])

    # genera y agrupa todas las imagenes de las lineas de texto.
    image = pygame.Surface((width, height), pygame.SRCALPHA, 32)

    dst_y = 0

    for line in lines:
        image.blit(line, (0, dst_y))
        dst_y += interline + line.get_height()

    return image, pygame.Rect(0, 0, width, height)
