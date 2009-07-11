# -*- coding: iso-8859-1 -*-
import pygame
import os
# Como no se aún el directorio donde se ubicaran las imágenes, dejo la variable
# con una ruta simbólica que más adelante sera sustituida por la auténtica.
DATOS = 'aqui_ruta_de_imagenes'

# Función para cargar imágenes, devuelve la imagén y su tamaño
def load_images(name, colorkey = False):
	fullname = os.path.join(DATOS, name)
	
	try: image = pygame.image.load(fullname)
	except pygame.error, message:
		print 'No se ha podido cargar la imagen', fullname
		raise SystemExit, message
	
	image = image.convert()
	if colorkey:
		colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey, RLEACCEL)
	return image, image.get_rect()
		
