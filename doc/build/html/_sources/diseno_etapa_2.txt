Diseño de la etapa 2
====================

En esta etapa se comienza a definir el modelo de las piezas, como
se representan en pantalla y cómo es su lógica.


Objetivos de la etapa
---------------------

Se debe crear una nueva escena, que de manera similar a las
anteriores etapas tiene que heredar de *Scene*:

.. image:: images/etapa_2_nueva_escena.png


Y en pantalla la escena solamente ofrece la posibilidad de mover
una sola pieza (similar a una letra L) y regresar a la escena
anterior, la de la etapa 1.

Esta es una representación preliminar de la pantalla:

.. image:: images/etapa_2_en_pantalla.png



Objetos
-------

Esta etapa incorpora dos clases importantes, Board y Piece.


Piece
~~~~~

La clase Piece representa una pieza del juego. El usuario puede
mover esta pieza pulsando los direccionales del teclado.

Internamente la pieza está representada de dos formas, una
imagen que ve el usuario y una estructura de colisiones similar
a lo siguiente::

    [ ] [X] [ ] [ ]
    [ ] [X] [ ] [ ]
    [ ] [X] [X] [ ]

De esta forma, es muy sencillo verificar si dos piezas están
en colisión o constituyen una linea. El juego tiene una 
lógica de estructuras invisibles pero muy simples.

La siguiente es una imagen que resume la pantalla que ve
el usuario (a la izquierda) y la representación interna
del juego con estructuras:

.. image:: images/etapa_2_visual_y_logica.png


Tanto la imagen de la izquierda, como el modelo de la derecha, se
almacenan internamente en el objeto *Piece*.


Board
~~~~~

El objeto *Board* representa el tablero completo, y al igual que
*Piece* tiene una estructura invisible al usuario en donde se
almacenan los bloques utilizados.

Y también tiene una representación visual, en donde se dibujan
las piezas que tocan el suelo y el usuario ya no puede mover.


Interacción entre Piece y Board
-------------------------------

El objeto *Piece* responde a las ordenes del usuario, pero a la vez
tiene que prohibir movimientos incorrectos, ya sea porque salen
de la pantalla o porque existe una colisión con otra pieza.

Para manejar las restricciones, el objeto *Piece* consulta en cada
momento al objeto *Board*, y a su vez, *Board* inspecciona en su
modelo de matriz si tiene lugar para situar la pieza.


Inicialización de piezas
------------------------

Cada pieza tiene una forma que está compuesta por bloques que
colisionan, y otros que no.

La forma de estas piezas se encuentra en archivos separados, uno
por cada pieza, y se almacenan todos en el directorio *mask*.

Este es un ejemplo de la figura "L", el archivo tiene marcado
con *x* los bloques que colisionan::


    ..x.
    xxx.
    ....

    .x..
    .x..
    .xx.
    ....

    ....
    xxx.
    x...
    ....

    xx..
    .x..
    .x..
    ....

