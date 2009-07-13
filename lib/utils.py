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
        print 'No se ha podido cargar la imagen', fullname
        raise SystemExit, message
    

    if colorkey:
        colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    else:
        image = image.convert_alpha()

    return image, image.get_rect()
