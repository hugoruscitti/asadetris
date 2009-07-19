Estilo de programación
======================

Este documento define las convenciones de programación que
utilizamos para el proyecto. Esta guia no permiten
lograr código consistente, fácil de leer y uniforme.

Aquí solo resumimos los aspectos mas importantes de la
convención, si quiere conocer mas detalles le recomendamos
ver el documento que define por completo el estilo adoptado:

    http://mundogeek.net/traducciones/guia-estilo-python.htm


Estructura del código
---------------------

Es indispensable que el código en python esté identando de
la misma forma en todo el proyecto. Aquí utilizamos **4 espacios**
para definir cada bloque de código.

Por ejemplo::

    def load_image(path):
        """Carga una imagen y retorna un objeto surface."""

        if os.path.exists(path):
            image = pygame.image.load(path)
        
        # etc...
    
            
.. note::
    
    Configure su editor para que adopte 4 espacios al pulsar la
    tecla TAB. Esta funcionalidad la soportan la mayoría de
    los editores.


Sistema de codificación
-----------------------

Utilizamos el sistema de codificación *UTF8*, esto nos permite escribir
comentarios en español con mayor naturalidad.

Los archivos python creados en este proyecto comienzan con el
texto::

    # -*- encoding: utf-8 -*-


Inclusiones
-----------

Para incluir rutinas de otros módulos usamos la forma mas simple::

    import os
    import pygame
    import utils

No utilizamos variantes, como por ejemplo ``from pygame import *``, con
la intensión de hacer explícitas las sentencias de todo el código.


Separaciones y caracteres en blanco
-----------------------------------

Los espacios en blanco se suelen colocar después de una
coma::

    def create_display(width, height):
        """ Genera una ventana para el tamaño solicitado."""
        return pygame.display.set_mode((width, height))

y entre operadores como por ejemplo::

    size = (640, 480)
    width, height = size
    screen = create_display(width, height)

    if fullscreen:
        print "Iniciando el modo pantalla completa."


Documentación
-------------

Documentamos funciones y clases de manera breve usando *docstrings*::

    class Sprite:
        """Representa un personaje animado en la pantalla."""

        def __init__(self, x, y, image):
            """Construye un elemento situado en la posición (x, y)."""

evitamos colocar comentarios redundantes, a menos que sea
estrictamente necesario.

Por ejemplo: ``x = 30  # asignamos una posición`` es un mensaje redundante...


Nombres
-------

Usamos nombres en *Inglés* que resulten representativos para el
dato que señalan. 

Las variables y las funciones se escriben en minúsculas, y si
se componen de varias palabras usamos el guion bajo para separarlas.

Por ejemplo::

    x = 40
    y = 100
    logo = utils.load_image('menu/logo.png')

    screen.blit(logo, (x, y))


En cambio, los nombres de clases se definen usando el estilo *CamelCase*, 
donde cada palabra se distingue de otra usando una mayúscula::

    class SimpleAnimation(Animation):
        # code...
        pass

    image = utils.load_image('animation.png')
    animation = SimpleAnimation(image, frames=5)
