Diseño de la etapa 1
====================

Este documento explica parte de las decisiones e ideas que
definen la estructura del juego.

Puede usar el contenido de este texto para conocer de manera
sencilla cómo funciona el juego, que componentes tiene y cómo 
se relacionan entre sí.


Objetos y desacoplamiento
-------------------------

El juego va a incluir mucha complejidad, necesitamos gestionar eventos, 
dibujar en pantalla, analizar colisiones, puntajes y sonidos.

Esta complejidad se suele resolver en programación utilizando una
estrategia muy simple, que consiste en dividir el sistema completo
en componentes mas pequeños. Es mucho mas previsible y sencillo
gestionar unidades de funcionalidad pequeñas que grandes.

A grandes rasgos, hay muchas estrategias para dividir todo el
diseño en componentes pequeños. Aquí utilizaremos conceptos de
programación orientada a objetos, en donde el funcionamiento
del sistema se basa en Objetos individuales que intercambian
mensajes entre sí.


Objeto principal: Director
--------------------------

El objeto ``Director`` (director.py) es el encargado de mantener
el juego en funcionamiento.

Este objeto hace lo mínimo y necesario para mantener operable la
ventana principal, básicamente hace solo estas cosas:

- Genera la ventana del juego (inicia).
- Dibuja constantemente la ventana (dibuja).
- Mantiene en movimiento los objetos en pantalla (actualiza)
- Atiene los eventos del usuario (responde).


Escenas, las partes de un juego
-------------------------------

En realidad, el objeto director representa solo la ``caja`` que
mantiene en funcionamiento el juego, esa es su responsabilidad.

Pero falta algo, en realidad este juego estará compuesto de
varias escenas como una *presentación*, el *menú de opciones*, la
pantalla de *juego* (con las piezas), *el ranking de puntajes* etc...

Si eligiéramos escribir todas estas funcionalidades en el mismo
objeto Director, llegaríamos a tener una rutina algo difícil
de manejar, con variables de control (estilo 
``if etapa == 'menu' or etapa == 'opci...'``).

En lugar de ello, vamos a optar por una solución que recibe el
nombre de **Patrón estrategia**, una solución que en programación
se suele agrupar en un conjunto mas grande llamado *patrones de diseño*.


Bajo esta solución, podemos representar el funcionamiento del juego
como la colaboración entre dos clases:


.. graphviz::

    digraph "digraph" {
            node [shape=ellipse, fontsize="11.0", fontname=Verdana];
            Director [shape=record, fontsize=10, fontname=Verdana, label="{Director|screen\nscene|loop()\nchange_scene()}"];
            Scene [shape=record, fontsize=10, fontname=Verdana, label="{Scene|...|}"];

            Director -> Scene [label="dibujar", fontsize="11.0", fontname=Verdana]
            Director -> Scene [label="actualizar",fontsize="11.0", fontname=Verdana]
            Director -> Scene [label="procesar evento", fontsize="11.0", fontname=Verdana]
    }


El objeto  director se encarga solamente de mantener en funcionamiento
la aplicación, esto consiste en actualizar periódicamente la pantalla,
atender eventos y actualizar objetos.

El objeto escena, en cambio, contiene todo el código necesario para
representar una sola escena del juego. Cuando llega la orden de
actualizar la pantalla, la escena dibuja lo que le corresponde. Cuando
llega un evento, la escena lo atiene y responde.

Lo interesante de diseñar estos objetos por separado radica en poder
desacoplarlos en cualquier momento, por ejemplo si queremos ir
de la presentación del juego al menú principal, solamente
tendremos que eliminar un objeto y reemplazarlo por otro:

.. graphviz::

    digraph "digraph" {
            node [shape=ellipse, fontsize="11.0", fontname=Verdana];
            Director [shape=record, fontsize=10, fontname=Verdana, label="{Director|screen\nscene|loop()\nchange_scene()}"];
            Scene [shape=record, fontsize=10, fontname=Verdana, label="{MainMenu|...|}"];

            Director -> Scene
    }


En términos de programación, no hay mayor dificultad, el objeto
Director está diseñado para operar con una escena, e incluso
para intercambiarlas.

Este ejemplo ilustrativo (no ejecutable) muestra como crear una
escena, imprimirla sobre la pantalla y luego cambiarla por otra::

    presentacion = new Presentacion()
    director.set_scene(presentacion)

    director.draw()           # imprime la escena menu.
    director.draw()           # imprime la escena menu por segunda vez.

    juego = new Juego()
    director.set_scene(juego)   # descarta la escena anterior.
    director.draw()             # imprime la escena de juego.


Escenas, ampliando
------------------

Algo interesante para observar, es que las escenas son muy
parecidas entre sí. Una escena tiene que definir solamente 3
métodos obligatorios, y por lo tanto se pueden crear nuevas
escenas a partir de una general:



.. graphviz::

    digraph "dhigraph" {
        graph [rankdir=BT];
            node [shape=ellipse, fontsize="11.0", fontname=Verdana];
            Scene [shape=record, fontsize=10, fontname=Verdana, label="{Scene|...|on_update()\non_draw(screen)\non_event()}"];
            S2 [shape=record, fontsize=10, fontname=Verdana, label="{PresentsScene|...|}"];
            S3 [shape=record, fontsize=10, fontname=Verdana, label="{MenuScene|...|}"];
            S4 [shape=record, fontsize=10, fontname=Verdana, label="{GameScene|...|}"];

            S2 -> Scene [label="hereda de...", fontsize=10, fontname=Verdana]
            S3 -> Scene [label="hereda de...", fontsize=10, fontname=Verdana]
            S4 -> Scene [label="hereda de...", fontsize=10, fontname=Verdana];
    }



Si bien puede haber muchas escenas, es importante notar que
en tiempo de ejecución solo habrá una escena activa (el objeto
Director solo sabe administrar una...)



El Director no sabe de que vá la película...
--------------------------------------------

El objeto director tampoco sabe con certeza en que etapa
del juego se encuentra el usuario, para el objeto Director
todas las scenas son iguales, solo le interesa llamar a los
3 métodos que obligatoriamente tiene cada una.

De hecho, cuando se quiere cambiar de una escena a la
otra, es precisamente una escena la que le dice al
objeto director a que otra escena debe cambiar...
