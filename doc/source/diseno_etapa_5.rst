Diseño de la etapa 5
====================

Velocidad del juego
-------------------

Cuando el usuario realiza 10 lineas buscamos que el juego aumente
de velocidad. Esto se logra mediante la interacción de los
objectos `Display`, `Game` y `Piece`.

Básicamente quien coordina la velocidad del juego es la clase
`Game`. Mientras el usuario está jugando el objeto `Game` almacena
en su atributo `speed` la velocidad que le tiene que asignar
a cada pieza que genera. Este atributo de velocidad depende de
lo que le diga la clase `Display`, que conoce cuantas lineas
del juego a realiza el usuario y en qué nivel se encuenta.

El nivel, es simplemente la parte decimal de la cantidad de lineas:

::

    nivel = lineas / 10

