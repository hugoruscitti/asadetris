Diseño de la etapa 5
====================

Velocidad del juego
-------------------

Cuando el usuario realiza 10 lineas buscamos que el juego aumente
de velocidad. Esto se logra mediante la interacción de los objectos `Display`, `Game` y `Piece`.

Básicamente quien coordina la velocidad del juego es la clase
`Game`. Mientras el usuario está jugando el objeto `Game` almacena
en su atributo `speed` la veocidad que le tiene que asignar
a cada pieza que genera. Este atributo de velocidad depende de
lo que le diga la clase `Display`, que conoce cuantas lineas
del juego a realiza el usuario y en qué nivel se encuenta.

El nivel, es simplemente la parte decimal de la cantidad de lineas:

::

    nivel = lineas / 10


Mensajes dentro del juego como subscenes
----------------------------------------

Mientras estás jugando es importante que el juego que
marque claramente cuando pierdes o comienza el nivel.

Por eso, se ha creado la posibilidad de que la clase
``game`` pueda presentar distintos mensajes durante la 
sesión de juego. Por ejemplo, cuando se inicia el
juego se presenta un mensaje de tipo ``listo... ya!!`` para
indicar que el juego ha comenzado.

Los mensajes se han incoporado como objetos dentro
del modulo ``game_scene_messages``.

Cuando el objeto ``GameScene`` quiere mostrar un mensaje, solo
tiene que llamar al método ``show_graphic_message`` y pasarle
como argumento la instancia de un objeto del módulo
``game_scene_messages``. Por ejemplo, cuando se inicia el
juego.


Algo similar ocurre cuando el jugador pierde. Simplemente se
llama al método ``on_game_over`` de la clase ``GameScene`` y
desde ahí se invoca a la siguiente sentencia.

.. code-block:: python

    def on_game_over(self):
        self.show_graphic_message(game_scene_messages.GameOverMessage(self))
