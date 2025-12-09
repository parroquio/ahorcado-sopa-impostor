import random
import time
import os

def clear_output(wait=False):
    # Función para limpiar la pantalla de la terminal
    os.system('cls' if os.name == 'nt' else 'clear')

#funcion que inicializa una matriz de ceros del tamaño que diga el usuario
def inicializar_matriz(tamaño):
    for i in range(tamaño):
        fila = [0] * tamaño
        matriz.append(fila.copy())

# La funcion que elige una palabra de la lista, la añade con direccion y orientacion random y verifica que no moleste con otras
def elegir_colocar_palabra(matriz, palabras, tamaño):
    # elige una palabra random de la lista
    palabra = random.choice(palabras)
    longitud = len(palabra)
    contador = 0
    horizontal_vertical_diagonal = random.choice(
        ["horizontal", "vertical", "diagonal"])  # elige orientación de la palabra

    # Caso colocar palabra en Horizontal
    if horizontal_vertical_diagonal == "horizontal":
        # si la palabra elegida es mas grande que la sopa de letras, cambiar la palabra
        while tamaño < longitud:
            palabra = random.choice(palabras)
            longitud = len(palabra)
        # elegir si poner la palabra noraml o del reves
        direccion = random.choice(["normal", "reversa"])
        # caso palabra normal
        if direccion == "normal":
            # validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
            validar = False
            while validar == False:
                fila = random.randint(0, tamaño - 1)
                columna = random.randint(0, tamaño - longitud)
                for i in range(longitud):
                    if matriz[fila][columna + i] != 0 and matriz[fila][columna + i] != palabra[i]:
                        validar = False
                        break
                    validar = True
                contador += 1
                # para que si es impsosible colocar esa palabra en la sopa de letras, que cambie de palabra
                if contador % 50 == 0:
                    palabra = random.choice(palabras)
                    longitud = len(palabra)
                    while tamaño < longitud:
                        palabra = random.choice(palabras)
                        longitud = len(palabra)
            # almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir
            palabras.remove(palabra)
            palabras_sopa.append(palabra)
            posiciones_palabras.append(
                {"palabra": palabra, "inicio": (fila, columna), "final": (fila, columna + longitud - 1)})
            # coloca la palabra
            for i in range(longitud):
                if modo == "2":
                    emoji = ord(palabra[i]) - 65
                    matriz[fila][columna + i] = modo_emoji[emoji]
                else:
                    matriz[fila][columna + i] = palabra[i]
        # caso palabra del reves
        else:
            # doy la vuelta a la palabra y uso la logica del codigo de la palabra normal
            palabra = palabra[::-1]
            # validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
            validar = False
            while validar == False:
                fila = random.randint(0, tamaño - 1)
                columna = random.randint(0, tamaño - longitud)
                for i in range(longitud):
                    if matriz[fila][columna + i] != 0 and matriz[fila][columna + i] != palabra[i]:
                        validar = False
                        break
                    validar = True
                contador += 1
                # para que si es impsosible colocar esa palabra en la sopa de letras, que cambie de palabra
                if contador % 50 == 0:
                    palabra = random.choice(palabras)
                    longitud = len(palabra)
                    while tamaño < longitud:
                        palabra = random.choice(palabras)
                        longitud = len(palabra)
                    palabra = palabra[::-1]
            # almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir (todo ello dandole la vuelta otra vez ya que ya lo teniamos del reves)
            palabras.remove(palabra[::-1])
            palabras_sopa.append(palabra[::-1])
            posiciones_palabras.append(
                {"palabra": palabra[::-1], "inicio": (fila, columna + longitud - 1), "final": (fila, columna)})
            # coloca la palabra
            for i in range(longitud):
                if modo == "2":
                    emoji = ord(palabra[i]) - 65
                    matriz[fila][columna + i] = modo_emoji[emoji]
                else:
                    matriz[fila][columna + i] = palabra[i]

    # Caso colocar palabra en Diagonal
    if horizontal_vertical_diagonal == "diagonal":
        # si la palabra elegida es mas grande que la sopa de letras, cambiar la palabra
        while tamaño < longitud or tamaño < longitud:
            palabra = random.choice(palabras)
            longitud = len(palabra)
        # elegir si poner la palabra normal o del reves
        direccion = random.choice(["normal", "reversa"])
        # caso palabra normal
        if direccion == "normal":
            # validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
            validar = False
            while validar == False:
                fila = random.randint(0, tamaño - longitud)
                columna = random.randint(0, tamaño - longitud)
                for i in range(longitud):
                    if matriz[fila + i][columna + i] != 0 and matriz[fila + i][columna + i] != palabra[i]:
                        validar = False
                        break
                    validar = True
                contador += 1
                # para que si es impsosible colocar esa palabra en la sopa de letras, que cambie de palabra
                if contador % 50 == 0:
                    palabra = random.choice(palabras)
                    longitud = len(palabra)
                    while tamaño < longitud or tamaño < longitud:
                        palabra = random.choice(palabras)
                        longitud = len(palabra)
            # almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir
            palabras.remove(palabra)
            palabras_sopa.append(palabra)
            posiciones_palabras.append({"palabra": palabra, "inicio": (fila, columna),
                                        "final": (fila + longitud - 1, columna + longitud - 1)})
            # coloca la palabra
            for i in range(longitud):
                if modo == "2":
                    emoji = ord(palabra[i]) - 65
                    matriz[fila + i][columna + i] = modo_emoji[emoji]
                else:
                    matriz[fila + i][columna + i] = palabra[i]
        # caso palabra del reves
        else:
            # doy la vuelta a la palabra y uso la logica del codigo de la palabra normal
            palabra = palabra[::-1]
            # validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
            validar = False
            while validar == False:
                fila = random.randint(0, tamaño - longitud)
                columna = random.randint(0, tamaño - longitud)
                for i in range(longitud):
                    if matriz[fila + i][columna + i] != 0 and matriz[fila + i][columna + i] != palabra[i]:
                        validar = False
                        break
                    validar = True
                contador += 1
                # para que si es impsosible colocar esa palabra en la sopa de letras, que cambie de palabra
                if contador % 50 == 0:
                    palabra = random.choice(palabras)
                    longitud = len(palabra)
                    while tamaño < longitud or tamaño < longitud:
                        palabra = random.choice(palabras)
                        longitud = len(palabra)
                    palabra = palabra[::-1]
            # almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir (todo ello dandole la vuelta otra vez ya que ya lo teniamos del reves)
            palabras.remove(palabra[::-1])
            palabras_sopa.append(palabra[::-1])
            posiciones_palabras.append(
                {"palabra": palabra[::-1], "inicio": (fila + longitud - 1, columna + longitud - 1),
                 "final": (fila, columna), })
            # coloca la palabra
            for i in range(longitud):
                if modo == "2":
                    emoji = ord(palabra[i]) - 65
                    matriz[fila + i][columna + i] = modo_emoji[emoji]
                else:
                    matriz[fila + i][columna + i] = palabra[i]

    # Caso colocar palabra en vertical
    elif horizontal_vertical_diagonal == "vertical":
        # si la palabra elegida es mas grande que la sopa de letras, cambiar la palabra
        while tamaño < longitud:
            palabra = random.choice(palabras)
            longitud = len(palabra)
        # elegir si poner la palabra normal o del reves
        direccion = random.choice(["normal", "reversa"])
        # caso palabra normal
        if direccion == "normal":
            # validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
            validar = False
            while validar == False:
                fila = random.randint(0, tamaño - longitud)
                columna = random.randint(0, tamaño - 1)
                for i in range(longitud):
                    if matriz[fila + i][columna] != 0 and matriz[fila + i][columna] != palabra[i]:
                        validar = False
                        break
                    validar = True
                contador += 1
                # para que si es impsosible colocar esa palabra en la sopa de letras, que cambie de palabra
                if contador % 50 == 0:
                    palabra = random.choice(palabras)
                    longitud = len(palabra)
                    while tamaño < longitud:
                        palabra = random.choice(palabras)
                        longitud = len(palabra)
            # almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir
            palabras.remove(palabra)
            palabras_sopa.append(palabra)
            posiciones_palabras.append(
                {"palabra": palabra, "inicio": (fila, columna), "final": (fila + longitud - 1, columna), })
            # coloca la palabra
            for i in range(longitud):
                if modo == "2":
                    emoji = ord(palabra[i]) - 65
                    matriz[fila + i][columna] = modo_emoji[emoji]
                else:
                    matriz[fila + i][columna] = palabra[i]
        # caso palabra del reves
        else:
            # doy la vuelta a la palabra y uso la logica del codigo de la palabra normal
            palabra = palabra[::-1]
            # validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
            validar = False
            while validar == False:
                fila = random.randint(0, tamaño - longitud)
                columna = random.randint(0, tamaño - 1)
                for i in range(longitud):
                    if matriz[fila + i][columna] != 0 and matriz[fila + i][columna] != palabra[i]:
                        validar = False
                        break
                    validar = True
                contador += 1
                # para que si es impsosible colocar esa palabra en la sopa de letras, que cambie de palabra
                if contador % 50 == 0:
                    palabra = random.choice(palabras)
                    longitud = len(palabra)
                    while tamaño < longitud:
                        palabra = random.choice(palabras)
                        longitud = len(palabra)
                    palabra = palabra[::-1]
            # almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir (todo ello dandole la vuelta otra vez ya que ya lo teniamos del reves)
            palabras.remove(palabra[::-1])
            palabras_sopa.append(palabra[::-1])
            posiciones_palabras.append(
                {"palabra": palabra[::-1], "inicio": (fila + longitud - 1, columna), "final": (fila, columna), })
            # coloca la palabra
            for i in range(longitud):
                if modo == "2":
                    emoji = ord(palabra[i]) - 65
                    matriz[fila + i][columna] = modo_emoji[emoji]
                else:
                    matriz[fila + i][columna] = palabra[i]


# la funcion rellena con letras mayusuculas al azar los elementos de la matriz que no tienen puesta palabras (es decir, que siguen siendo 0)
def rellenar_sopa(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 0:
                if modo == "2":
                    matriz[i][j] = random.choice(modo_emoji)
                else:
                    matriz[i][j] = chr(random.randint(65, 90))


# función para localizar palabra en la sopa y saber si esta bien
def encontrar_palabra_en_sopa(palabras_sopa, posiciones_palabras, palabras_acertadas, tamaño, palabras_por_sopa):
    # el usuario elige la fila de la inicial de la palabra (y verifica que sea un número y en el rango posible)
    time.sleep(2)
    intento_fila_inicial = input("Introduce el número de la fila en la que se encuentra la inicial de la palabra: ")
    while intento_fila_inicial.isdigit() == False or int(intento_fila_inicial) > tamaño:
        time.sleep(0.5)
        intento_fila_inicial = input(
            "No puede ser ni mas grande que el tamaño de la sopa ni un caracter, pruebe otra vez: ")
    intento_fila_inicial = int(intento_fila_inicial)
    # el usuario elige la columna de la inicial de la palabra (y verifica que sea un número y en el rango posible)
    time.sleep(0.5)
    intento_columna_inicial = input(
        "Introduce el número de la columna en la que se encuentra la inicial de la palabra: ")
    while intento_columna_inicial.isdigit() == False or int(intento_columna_inicial) > tamaño:
        time.sleep(0.5)
        intento_columna_inicial = input(
            "No puede ser ni mas grande que el tamaño de la sopa ni un caracter, pruebe otra vez: ")
    intento_columna_inicial = int(intento_columna_inicial)
    # el usuario elige la fila de la última letra de la palabra (y verifica que sea un número y en el rango posible)
    time.sleep(0.5)
    intento_fila_final = input(
        "Introduce el número de la fila en la que se encuentra la última letra de la palabra: ")
    while intento_fila_final.isdigit() == False or int(intento_fila_final) > tamaño:
        time.sleep(0.5)
        intento_fila_final = input(
            "No puede ser ni mas grande que el tamaño de la sopa ni un caracter, pruebe otra vez: ")
    intento_fila_final = int(intento_fila_final)
    # el usuario elige la columna de la última letra de la palabra (y verifica que sea un número y en el rango posible)
    time.sleep(0.5)
    intento_columna_final = input(
        "Introduce el número de la columna en la que se encuentra la última letra de la palabra: ")
    while intento_columna_final.isdigit() == False or int(intento_columna_final) > tamaño:
        time.sleep(0.5)
        intento_columna_final = input(
            "No puede ser ni mas grande que el tamaño de la sopa ni un caracter, pruebe otra vez: ")
    intento_columna_final = int(intento_columna_final)
    # como ya he verificado que es un número, pasamos el input a int
    intento_fila_inicial = int(intento_fila_inicial)
    intento_columna_inicial = int(intento_columna_inicial)
    intento_fila_final = int(intento_fila_final)
    intento_columna_final = int(intento_columna_final)
    # restamos 1 a filas y columnas ya que python empeiza a contar desde 0
    intento_fila_inicial -= 1
    intento_columna_inicial -= 1
    intento_fila_final -= 1
    intento_columna_final -= 1
    # verifica si el usuario ha localizado bien la palabra o no (si ha acertado remueve la palabra de la lista palabras_sopa y la añade a la lista palabras_acertadas)
    for i in range(palabras_por_sopa):
        if posiciones_palabras[i]["inicio"] == (intento_fila_inicial, intento_columna_inicial) and \
                posiciones_palabras[i]["final"] == (intento_fila_final, intento_columna_final):
            palabras_acertadas.append(posiciones_palabras[i]["palabra"])
            palabras_sopa.remove(posiciones_palabras[i]["palabra"])


# Función conjuntos de for y prints para imprimir la matriz con una sopa con eje x e y para que sea más facil para el usuario jugar
def imprimir_matriz(matriz, modo):
    if modo == "1":
        print("   ", end="")
        for j in range(len(matriz[0])):
            if j <= 8:
                print(f"\033[38;5;208m{j + 1}\033[0m", end="   ")
            else:
                print(f"\033[38;5;208m{j + 1}\033[0m", end="  ")
        print()
        print(" ", end=" -")
        print("----" * (len(matriz) - 1), end="")
        print("-")
        for i in range(len(matriz)):
            if i <= 8:
                print(f"\033[38;5;208m{i + 1}{' |'}\033[0m", end="")
            else:
                print(f"\033[38;5;208m{i + 1}{'|'}\033[0m", end="")
            for j in range(len(matriz[0])):
                print(matriz[i][j], end="   ")
            print()
        print()
        print("Palabras en la sopa: ", end="")
    else:
        print("   ", end=" ")
        for j in range(len(matriz[0])):
            if j % 2 == 0 and j <= 8:
                print(f"\033[38;5;208m{j + 1}\033[0m", end="    ")
            elif j % 2 != 0 and j > 8:
                print(f"\033[38;5;208m{j + 1}\033[0m", end="   ")
            elif j % 2 == 0 and j > 8:
                print(f"\033[38;5;208m{j + 1}\033[0m", end="    ")
            else:
                print(f"\033[38;5;208m{j + 1}\033[0m", end="     ")
        print()
        print(" ", end=" -")
        print("-----" * (len(matriz) - 1), end="")
        x = 0.5 * (len(matriz) - 1)
        print("-" * (int(x)), end="")
        print("--")

        for i in range(len(matriz)):
            if i <= 8:
                print(f"\033[38;5;208m{i + 1}{' |'}\033[0m", end="")
            else:
                print(f"\033[38;5;208m{i + 1}{'|'}\033[0m", end="")
            for j in range(len(matriz[0])):
                print(matriz[i][j], end="   ")
            print()
        print()
        print("Palabras en la sopa: ", end="")


# Lista de las palabras que pueden aparecer en la sopa
palabras = ["ABEJA", "ABECEDA", "ACORDEON", "ADULTO", "ADOPCION", "AGUA", "AIRE", "ALBUM",
            "ALFOMBRA", "ALMUERZO", "ALMOHADA", "ALTO", "AMABILIDAD", "AMABLE", "AMIGO", "AMOR", "ANILLO", "ANIMAL",
            "APOYO", "ARENA", "ARBITRO", "ARMA", "ARTISTA", "ARTE", "AVENA", "AVION", "AZUCAR", "BAILARIN", "BANCO",
            "BARCO", "DUCHA", "BEBE", "BEBIDA", "BELLO", "BIBLIOTECA", "BOLA", "BONITO", "BOSQUE", "BOCA", "BRAZO",
            "BRISA", "BUFANDA", "BURRO", "CABA", "CAFE", "CAJA", "CALLE", "CALOR", "CAMA", "CAMPO", "CAMBIO",
            "CANGREJO",
            "CANTO", "CARACOL", "CARNE", "CARRERA", "CARRO", "CARTA", "CASTILLO", "CEREAL", "CENA", "CESTA",
            "CIENCIA",
            "CIUDAD", "CLASE", "CLAVE", "COCHE", "COLEGIO", "COLINA", "COMETA", "COMIDA", "COMPANIA",
            "CONOCIMIENTO",
            "CONEJO", "COPA", "CORAZON", "CORONA", "CORTE", "CUCHILLO", "CUERPO", "CUEVA", "CURA", "DEDOS", "DADO",
            "DIA",
            "DINERO", "DIFICIL", "DINOSAURIO", "DISCO", "DOCTOR", "DOLOR", "DULCE", "DULZURA", "EDAD", "EDUCACION",
            "EDIFICIO",
            "EMOCION", "ENFERMO", "ESCALERA", "ESCUELA", "ESPEJO", "ESTADIO", "ESTRELLA", "ESTUDIO", "EXAMEN",
            "EXITO",
            "FACIL", "FAMILIA", "FANTASMA", "FERIA", "FELICIDAD", "FLOR", "FOCA", "FUEGO", "FRUTA", "FUERTE",
            "GALAXIA",
            "GALERIA", "GALLO", "GATO", "GENTE", "GLOBO", "GOL", "GRANJA", "GRUPO", "GUANTE", "GUITARRA",
            "HABITACION",
            "HADA", "HELADO", "HELADERIA", "HERMANO", "HERMOSO", "HERRAMIENTA", "HIJO", "HOGAR", "HOMBRE", "HORA",
            "HOTEL",
            "HUERTA", "IDEA", "IGLESIA", "IMAGEN", "INFANCIA", "INQUIETO", "INTELIGENTE", "INVIERNO", "JARDIN",
            "JUEGO",
            "JORNADA", "JUGUETE", "JUGUETERIA", "JUNIO", "KILOMETRO", "LAGO", "LAMPARA", "LAPIZ", "LATIDO",
            "LECCION",
            "LECHE", "LEON", "LENGUA", "LIBRO", "LIBRERIA", "LUCHA", "LUZ", "LUMINOSO", "MAMA", "MAESTRO", "MAPA",
            "MAR",
            "MARCO", "MARIPOSA", "MARMOL", "MASCOTA", "MENSAJE", "MERCADO", "MES", "MESA", "MONTE", "MUNDO",
            "MUSICA",
            "NACION", "NIEVE", "NOCHE", "NOMBRE", "NOVELA", "NOVIEMBRE", "NUBE", "CHICO", "CHICA", "OBJETO", "OLA",
            "OJOS",
            "OSASUNA", "OSOS", "PALABRA", "PALACIO", "PALMERA", "PAPEL", "PAJARO", "PARAGUAS", "PARQUE", "PARRILLA",
            "PELOTA", "PELICULA", "PERIODICO", "PERRO", "PERSONA", "PLANTA", "PLANETA", "PLAZA", "PLATO", "POESIA",
            "PUEBLO",
            "PUENTE", "PUERTA", "PUERTO", "QUESO", "RAIZ", "RATON", "REINA", "RELOJ", "RECUERDO", "REGALO",
            "REUNION", "RIO",
            "ROPA", "RAPIDO", "SALA", "SALUD", "SALON", "SABOR", "SECRETO", "SEMILLA", "SENDERO", "SIESTA",
            "SOCIEDAD",
            "SOL", "SOLUCION", "SOMBRERO", "SOMBRILLA", "SONRISA", "TRANQUILO", "TIERRA", "TAZA", "TECHO",
            "TELEVISIÓN", "TIEMPO", "TUNEL", "TREN", "UNIVERSIDAD", "VACACIONES", "VACA", "VENTANA", "VALLE",
            "VENTILADOR",
            "VERSO", "VIDA", "VINO", "VIENTO", "YATE", "ZANAHORIA", "ZOOLOGICO", "ZUMO"]
modo_emoji = ["🐝",  # A - Abeja
              "🛢️",  # B - Barril
              "🐴",  # C - Caballo
              "🐬",  # D - Delfín
              "🐘",  # E - Elefante
              "🌸",  # F - Flor
              "🐈",  # G - Jirafa
              "🦛",  # H - Hipopotamo
              "🦎",  # I - Iguana
              "🦒",  # J - Jirafa
              "🐨",  # K - Koala
              "🦁",  # L - León
              "🐒",  # M - Mono
              "🦦",  # N - Nutria
              "🐑",  # O - Oveja
              "🐼",  # P - Panda
              "🧀",  # Q - Queso
              "🐀",  # R - Rata
              "🐍",  # S - Serpiente
              "🐅",  # T - Tigre
              "🦄",  # U - Unicornio
              "🐄",  # V - Vaca
              "🤽‍♂️",  # W - Waterpolo
              "❌",  # X - X
              "🪀",  # Y - Yo yo
              "💤"  # Z - zzz
              ]
# bucle principal del programa  (el while para que pueda jugar las veces que quiera)
n = "s"
while n == "s" or n == "S":
    clear_output(wait=True)  # limpia pantalla (funcional cuando quieres volver a jugar)
    # creo variables que tienen utilidad en funciones y en este while
    matriz = []
    palabras_sopa = []
    posiciones_palabras = []
    palabras_acertadas = []
    print("\033[1;32mBIENVENIDO A LA SOPA DE LETRAS!!! \033[0m")
    time.sleep(2)
    print("Esta versión de la sopa de letras tiene dos modos: ")
    time.sleep(2)
    # elige modo al que jugar normal o emoji
    print("1. Modo Normal")
    time.sleep(2)
    print("2. Modo Emoji")
    time.sleep(2)
    modo = input("Introduce 1 o 2 dependiendo del modo que quieras jugar: ")
    while modo != "1" and modo != "2":
        time.sleep(0.5)
        modo = input("Introduce unicamente 1 o 2 dependiendo del modo que quieras jugar: ")
    clear_output(wait=True)
    # elige el tamaño de la sopa, verifica que no sea menor que 4x4
    if modo == "1":
        time.sleep(0.5)
        print("\033[1;32mHas elegido el modo normal, tienes que encontrar las palabras en la sopa de letras\033[0m")
        time.sleep(5)
    else:
        time.sleep(0.5)
        print(
            "\033[1;33mHas elegido el modo emoji, cada emoji representa un objeto/animal cuya inicial es con la que debes crear la palabra a buscar\033[0m")
        time.sleep(5)
    tamaño = input("Por favor, introduce de que tamaño quieres la sopa de letras (Min 4): ")
    while tamaño.isdigit() == False or (int(tamaño) < 4):
        time.sleep(0.5)
        tamaño = input("No puedes introducir otros caracteres o número menores a 4, prube otra vez: ")
    tamaño = int(tamaño)
    # pone un limite a el número de palabras que puede añadir para ese tamaño de sopa
    max_palabras_por_sopa = None
    if tamaño == 4:
        max_palabras_por_sopa = "2"
    else:
        max_palabras_por_sopa = tamaño - 1
        max_palabras_por_sopa = str(max_palabras_por_sopa)
    # pide cuantas palabras quiere en la sopa con el maximo ya establecido y verifica que este dentro del rango y sea un número
    time.sleep(1.5)
    palabras_por_sopa = input(
        f"Introduce de cuantas palabras quieres que haya en la sopa (Max {max_palabras_por_sopa}): ")
    while palabras_por_sopa.isdigit() == False or palabras_por_sopa > max_palabras_por_sopa:
        time.sleep(0.5)
        palabras_por_sopa = input(
            f"No puedes introducir otros caracteres o número mayores a {max_palabras_por_sopa}, prube otra vez: ")
    palabras_por_sopa = int(palabras_por_sopa)
    inicializar_matriz(tamaño)  # matriz de ceros
    # se añade tantas palabras a la sopa como haya puesto el usuario
    for i in range(palabras_por_sopa):
        elegir_colocar_palabra(matriz, palabras, tamaño)
    rellenar_sopa(matriz)  # se rellena el resto de la sopa con letras al azar
    # variable que si inicializa con el valor de el número de palabras en la sopa, y que me servira para que si cambia el valor de len(palabras_sopa) significa que la funcion encontrar_palabra ha acertado la palabra
    palabras_restantes = len(palabras_sopa)
    # el contador es unicamente para que en la primera ronda no imprima has acertado/has fallado/ y lo de palabras restantes...
    contador = 0
    while len(palabras_sopa) > 0:
        # si cambia el valor de len(palabras_sopa) significa que en la funcion encontrar_palabra el usuaario ha encontrado la palabra y borrado la palabra de la lista palabras_sopa
        if palabras_restantes != len(palabras_sopa):
            time.sleep(1)
            print("\033[1;32mHAS ACERTADO LA PALABRA!!! SIGUE ASI!!! \033[0m")
            time.sleep(2)
        # por lo contrario si no se ha borrado ninguna palabra, significa que el usuario ha fallado
        elif contador != 0:
            time.sleep(1)
            print("\033[1;31mHAS FALLADO, SIGUELO INTENTANDO!!! \033[0m")
            time.sleep(2)
        palabras_restantes = len(palabras_sopa)
        print()  # dejo un hueco
        time.sleep(1)
        imprimir_matriz(matriz, modo)  # imprimimos la matriz ya con las palabras y letras al azar (y sus ejes)
        # bucle for para imprimir las palabras que hay que buscar en la sopa
        for i in range(len(palabras_sopa)):
            if i + 1 != len(palabras_sopa):
                print(palabras_sopa[i], end=", ")
            else:
                print(palabras_sopa[i], end="")
        print()  # dejo un hueco
        # ejecuto la funcion que permite al usuario encontrar palabra y verifica si la ha encontrado
        encontrar_palabra_en_sopa(palabras_sopa, posiciones_palabras, palabras_acertadas, tamaño, palabras_por_sopa)
        contador += 1
        clear_output(wait=True)  # limpia pantalla en cada intento para que sea mas estetico
    # final del juego
    time.sleep(0.5)
    print("\033[1;32mHAS GANADO EL JUEGO!!! ENHORABUENA!!! \033[0m")
    time.sleep(2.5)
    print("Quieres seguir jugando (Introduce 's' si quieres seguir jugando y cualquier otra letra si no)?")
    n = input()
