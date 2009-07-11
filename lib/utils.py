# -*- coding: utf-8 -*-

import pygame
import os
# Como no se aún el directorio donde se ubicaran las imágenes, dejo la variable
# con una ruta simbólica que más adelante sera sustituida por la auténtica.
DATOS = os.path.dirname(os.path.abspath(__file__))

# Función para cargar imágenes, devuelve la imagen y su tamaño
def load_images(name, colorkey = False):
	fullname = os.path.join(DATOS, "../images", name)
	
	try: image = pygame.image.load(fullname)
	except pygame.error, message:
		print 'No se ha podido cargar la imagen', fullname
		raise SystemExit, message
	

	if colorkey:
		colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey, RLEACCEL)
        else:
	    image = image.convert_alpha()

	return image, image.get_rect()
		
