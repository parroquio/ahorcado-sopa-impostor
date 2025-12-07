## Arcade Python: La Sala de Minijuegos

Este proyecto de informática consiste en el desarrollo de una pequeña sala de juegos *arcade* implementada en Python. El corazón del proyecto es una interfaz principal desde la que el usuario puede navegar y seleccionar entre tres minijuegos distintos.

A través del menú principal, el jugador puede acceder a tres juegos diferentes: La sopa de letras, el impostor y el ahorcado.

Cada uno de estos tres juegos ha sido diseñado y programado por un miembro del grupo. En las secciones siguientes se detalla qué ha realizado cada integrante en el proyecto.

---

### Repositorio del Proyecto

Hemos creado un repositorio en GitHub donde hemos subido todo más ordenado:

> **[https://github.com/parroquio/ahorcado-sopa-impostor](https://github.com/parroquio/ahorcado-sopa-impostor)**

---

### DISTRIBUCIÓN DEL TRABAJO

#### SOPA DE LETRAS (Aitor)

Por un lado, la sopa de letras, de la cual su elaboración al completo se ha encargado Aitor. El juego se ha llevado a cabo en base a varias funciones, crear la sopa con ceros, imprimir la sopa/matriz, rellenar la sopa con letras al azar... de las cuales destaca la función de colocar y elegir una palabra, que se ocupa de la elección al azar de una palabra de una gran lista de 300 palabras, y su colocación de manera horizontal, vertical o diagonal (y la palabra normal o dada la vuelta) en la sopa de letras comprobando no tapar otra palabra ya puesta. Además, la sopa de letras cuenta con dos modos, el clásico de toda la vida y uno nuevo con emojis que se ha logrado relacionando cada emoji a una letra (ej: A- emoji de Abeja).

---

#### IMPOSTOR (Javier Iglesias)

En segundo lugar, Javier Iglesias ha asumido la responsabilidad principal del desarrollo de la lógica del programa del impostor y de la creación de los datos esenciales. Esto incluye, específicamente, el diseño y la implementación de los diccionarios que usa el juego para su funcionamiento interno, así como toda la lógica que define la dinámica de la partida, la asignación de roles y la gestión de la interacción entre jugadores.

Adicionalmente, y con el objetivo de facilitar la usabilidad del proyecto, Javier se ha encargado de la creación de una versión ejecutable con interfaz gráfica (GUI) para Windows. Para esta tarea, se han empleado herramientas de Inteligencia Artificial que han asistido en la conversión y empaquetamiento, asegurando que el juego sea accesible y fácil de ejecutar para cualquier usuario en dicho sistema operativo.

---

#### AHORCADO (Oihan Hernaz)

Y por último el ahorcado. De desarrollarlo se ha encargado el último miembro del grupo que falta por nombrar, Oihan Hernaz. Oihan ha desarrollado el juego el ahorcado al completo. Se ha encargado de la lógica del juego (elección de las palabras, control de intentos, comprobación de letras, detección de victoria o derrota) y de las funciones que muestran en pantalla al usuario el estado de la palabra, las letras falladas y el dibujo del ahorcado según los errores.
