Diseño de la etapa 4
====================

.. sequence-diagram::
   :maxwidth: 500
   :linewrap: false
   :threadnumber: true

   actor:Actor
   sphinx:Sphinx[a]
   dot:Graphviz
   sdedit:Quick Sequence Diagram Editor

   actor:sphinx.make html
   sphinx:dot.render_diagram()
   sphinx:sdedit.render_diagram()

::

    [_] permitir que el usuario pueda hacer lineas
    [_] hacer que las piezas bajen a una determinada velocidad.
    [_] aumentar la velocidad de caida de las piezas conforme avanza
    [_] implementar un contador del lineas
    [_] imprimir un mensaje de GameOver cuando llega a la parte superior.

Velocidad de juego
------------------

A partir de esta etapa las piezas comienzan a bajar de forma automática,
conforme el usuario avanza de niveles la velocidad de caída aumenta.

La velocidad de descarga está implementada internamente en la clase
``Piece``. En cada instante del juego la clase ``Game`` se encarga
de llamar al método ``update`` de ``Piece``.



