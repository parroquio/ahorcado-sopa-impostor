import random
import os

def clear_output(wait=False):
    os.system('clear')

def inicializar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = [0] * columnas
        matriz.append(fila.copy())
    return matriz

def elegir_colocar_palabra(matriz, palabras, filas, columnas, palabras_sopa, posiciones_palabras):
    palabra = random.choice(palabras)
    longitud = len(palabra)
    contador = 0
    horizontal_vertical = random.choice(["horizontal", "vertical", "diagonal"])

    # Caso colocar palabra en Horizontal
    if horizontal_vertical == "horizontal":
        # si la palabra elegida es mas grande que la sopa de letras, cambiar la palabra
        while columnas < longitud:
            palabra = random.choice(palabras)
            longitud = len(palabra)
        # elegir si poner la palabra normal o del reves
        direccion = random.choice(["normal", "reversa"])
        # caso palabra normal
        if direccion == "normal":
            # validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
            validar = False
            while validar == False:
                fila = random.randint(0, filas - 1)
                columna = random.randint(0, columnas - longitud)
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
                    while columnas <= longitud:
                        palabra = random.choice(palabras)
                        longitud = len(palabra)
            # almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir
            palabras.remove(palabra)
            palabras_sopa.append(palabra)
            posiciones_palabras.append({"palabra": palabra, "inicio": (fila, columna), "final": (fila, columna + longitud - 1)})
            # coloca la palabra
            for i in range(longitud):
                matriz[fila][columna + i] = palabra[i]
        # caso palabra del reves
        else:
            # doy la vuelta a la palabra y uso la logica del codigo de la palabra normal
            palabra = palabra[::-1]
            # validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
            validar = False
            while validar == False:
                fila = random.randint(0, filas - 1)
                columna = random.randint(0, columnas - longitud)
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
                    while columnas <= longitud:
                        palabra = random.choice(palabras)
                        longitud = len(palabra)
                    palabra = palabra[::-1]
            # almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir (todo ello dandole la vuelta otra vez ya que ya lo teniamos del reves)
            palabras.remove(palabra[::-1])
            palabras_sopa.append(palabra[::-1])
            posiciones_palabras.append({"palabra": palabra[::-1], "inicio": (fila, columna + longitud - 1), "final": (fila, columna)})
            # coloca la palabra
            for i in range(longitud):
                matriz[fila][columna + i] = palabra[i]

    # Caso colocar palabra en Diagonal
    if horizontal_vertical == "diagonal":
        # si la palabra elegida es mas grande que la sopa de letras, cambiar la palabra
        while columnas < longitud or filas < longitud:
            palabra = random.choice(palabras)
            longitud = len(palabra)
        # elegir si poner la palabra normal o del reves
        direccion = random.choice(["normal", "reversa"])
        # caso palabra normal
        if direccion == "normal":
            # validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
            validar = False
            while validar == False:
                fila = random.randint(0, filas - longitud)
                columna = random.randint(0, columnas - longitud)
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
                    while columnas <= longitud or filas <= longitud:
                        palabra = random.choice(palabras)
                        longitud = len(palabra)
            # almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir
            palabras.remove(palabra)
            palabras_sopa.append(palabra)
            posiciones_palabras.append({"palabra": palabra, "inicio": (fila, columna), "final": (fila + longitud - 1, columna + longitud - 1)})
            # coloca la palabra
            for i in range(longitud):
                matriz[fila + i][columna + i] = palabra[i]
        # caso palabra del reves
        else:
            # doy la vuelta a la palabra y uso la logica del codigo de la palabra normal
            palabra = palabra[::-1]
            # validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
            validar = False
            while validar == False:
                fila = random.randint(0, filas - longitud)
                columna = random.randint(0, columnas - longitud)
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
                    while columnas <= longitud or filas <= longitud:
                        palabra = random.choice(palabras)
                        longitud = len(palabra)
                    palabra = palabra[::-1]
            # almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir (todo ello dandole la vuelta otra vez ya que ya lo teniamos del reves)
            palabras.remove(palabra[::-1])
            palabras_sopa.append(palabra[::-1])
            posiciones_palabras.append({"palabra": palabra[::-1], "inicio": (fila + longitud - 1, columna + longitud - 1), "final": (fila, columna)})
            # coloca la palabra
            for i in range(longitud):
                matriz[fila + i][columna + i] = palabra[i]

    # Caso colocar palabra en vertical
    elif horizontal_vertical == "vertical":
        # si la palabra elegida es mas grande que la sopa de letras, cambiar la palabra
        while filas < longitud:
            palabra = random.choice(palabras)
            longitud = len(palabra)
        # elegir si poner la palabra normal o del reves
        direccion = random.choice(["normal", "reversa"])
        # caso palabra normal
        if direccion == "normal":
            # validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
            validar = False
            while validar == False:
                fila = random.randint(0, filas - longitud)
                columna = random.randint(0, columnas - 1)
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
                    while filas <= longitud:
                        palabra = random.choice(palabras)
                        longitud = len(palabra)
            # almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir
            palabras.remove(palabra)
            palabras_sopa.append(palabra)
            posiciones_palabras.append({"palabra": palabra, "inicio": (fila, columna), "final": (fila + longitud - 1, columna)})
            # coloca la palabra
            for i in range(longitud):
                matriz[fila + i][columna] = palabra[i]
        # caso palabra del reves
        else:
            # doy la vuelta a la palabra y uso la logica del codigo de la palabra normal
            palabra = palabra[::-1]
            # validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
            validar = False
            while validar == False:
                fila = random.randint(0, filas - longitud)
                columna = random.randint(0, columnas - 1)
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
                    while filas <= longitud:
                        palabra = random.choice(palabras)
                        longitud = len(palabra)
                    palabra = palabra[::-1]
            # almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir (todo ello dandole la vuelta otra vez ya que ya lo teniamos del reves)
            palabras.remove(palabra[::-1])
            palabras_sopa.append(palabra[::-1])
            posiciones_palabras.append({"palabra": palabra[::-1], "inicio": (fila + longitud - 1, columna), "final": (fila, columna)})
            # coloca la palabra
            for i in range(longitud):
                matriz[fila + i][columna] = palabra[i]

def rellenar_sopa(matriz, filas, columnas):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 0:
                matriz[i][j] = chr(random.randint(65, 90))

def encontrar_palabra_en_sopa(palabras_sopa, posiciones_palabras, palabras_acertadas, filas_total):
    filas_str = str(filas_total)
    intento_fila_inicial = input("Introduce el número de la fila en la que se encuentra la inicial de la palabra: ")
    while intento_fila_inicial.isdigit() == False or int(intento_fila_inicial) > filas_total:
        intento_fila_inicial = input("No puede ser ni mas grande que el tamaño de la sopa ni un caracter, pruebe otra vez: ")
    
    intento_columna_inicial = input("Introduce el número de la columna en la que se encuentra la inicial de la palabra: ")
    while intento_columna_inicial.isdigit() == False or int(intento_columna_inicial) > filas_total:
        intento_columna_inicial = input("No puede ser ni mas grande que el tamaño de la sopa ni un caracter, pruebe otra vez: ")
    
    intento_fila_final = input("Introduce el número de la fila en la que se encuentra la última letra de la palabra: ")
    while intento_fila_final.isdigit() == False or int(intento_fila_final) > filas_total:
        intento_fila_final = input("No puede ser ni mas grande que el tamaño de la sopa ni un caracter, pruebe otra vez: ")
    
    intento_columna_final = input("Introduce el número de la columna en la que se encuentra la última letra de la palabra: ")
    while intento_columna_final.isdigit() == False or int(intento_columna_final) > filas_total:
        intento_columna_final = input("No puede ser ni mas grande que el tamaño de la sopa ni un caracter, pruebe otra vez: ")
    
    intento_fila_inicial = int(intento_fila_inicial)
    intento_columna_inicial = int(intento_columna_inicial)
    intento_fila_final = int(intento_fila_final)
    intento_columna_final = int(intento_columna_final)
    
    intento_fila_inicial -= 1
    intento_columna_inicial -= 1
    intento_fila_final -= 1
    intento_columna_final -= 1
    
    for i in range(len(palabras_sopa)):
        if posiciones_palabras[i]["inicio"] == (intento_fila_inicial, intento_columna_inicial) and posiciones_palabras[i]["final"] == (intento_fila_final, intento_columna_final):
            palabras_acertadas.append(posiciones_palabras[i]["palabra"])
            palabras_sopa.remove(posiciones_palabras[i]["palabra"])
            return

def main():
    n = "s"
    while n == "s" or n == "S":
        clear_output(wait=True)
        matriz = []
        palabras_sopa = []
        posiciones_palabras = []
        palabras_acertadas = []
        
        filas = input("Introduce de que tamaño quieres la matriz (Min 4): ")
        while filas.isdigit() == False or int(filas) < 4:
            filas = input("No puedes introducir otros caracteres o número menores a 4, prube otra vez: ")
        
        columnas = int(filas)
        filas = columnas
        
        max_palabras_por_sopa = None
        if filas == 4:
            max_palabras_por_sopa = None # Logic in original code seems to imply no limit or handled differently? 
            # In original: if filas==4: max=None else: max=filas-1. 
            # But then input prompt uses format(max). If max is None, format might fail or print None.
            # Let's assume for 4 it's small.
            max_palabras_por_sopa = 4 # Reasonable default
        else:
            max_palabras_por_sopa = filas - 1
            
        palabras_por_sopa = input("Introduce de cuantas palabras quieres que haya en la sopa (Max {}): ".format(max_palabras_por_sopa))
        while palabras_por_sopa.isdigit() == False or int(palabras_por_sopa) > max_palabras_por_sopa:
            palabras_por_sopa = input("No puedes introducir otros caracteres o número mayores a {}, prube otra vez: ".format(max_palabras_por_sopa))
        palabras_por_sopa = int(palabras_por_sopa)
        
        palabras = ["ABEJA", "ABECEDA", "ACORDEON", "ADULTO", "ADOPCION", "AGUA", "AIRE", "ALBUM",
        "ALFOMBRA", "ALMUERZO", "ALMOHADA", "ALTO", "AMABILIDAD", "AMABLE", "AMIGO", "AMOR", "ANILLO", "ANIMAL",
        "APOYO", "ARENA", "ARBITRO", "ARMA", "ARTISTA", "ARTE", "AVENA", "AVION", "AZUCAR", "BAILARIN", "BANCO",
        "BARCO", "BAÑO", "BEBE", "BEBIDA", "BELLO", "BIBLIOTECA", "BOLA", "BONITO", "BOSQUE", "BOCA", "BRAZO",
        "BRISA", "BUFANDA", "BURRO", "CABA", "CAFE", "CAJA", "CALLE", "CALOR", "CAMA", "CAMPO", "CAMBIO", "CANGREJO",
        "CANTO", "CARACOL", "CARNE", "CARRERA", "CARRO", "CARTA", "CASTILLO", "CEREAL", "CENA", "CESTA", "CIENCIA",
        "CIUDAD", "CLASE", "CLAVE", "COCHE", "COLEGIO", "COLINA", "COMETA", "COMIDA", "COMPANIA", "CONOCIMIENTO",
        "CONEJO", "COPA", "CORAZON", "CORONA", "CORTE", "CUCHILLO", "CUERPO", "CUEVA", "CURA", "DEDOS", "DADO", "DIA",
        "DINERO", "DIFICIL", "DINOSAURIO", "DISCO", "DOCTOR", "DOLOR", "DULCE", "DULZURA", "EDAD", "EDUCACION", "EDIFICIO",
        "EMOCION", "ENFERMO", "ESCALERA", "ESCUELA", "ESPEJO", "ESTADIO", "ESTRELLA", "ESTUDIO", "EXAMEN", "EXITO",
        "FACIL", "FAMILIA", "FANTASMA", "FERIA", "FELICIDAD", "FLOR", "FOCA", "FUEGO", "FRUTA", "FUERTE", "GALAXIA",
        "GALERIA", "GALLO", "GATO", "GENTE", "GLOBO", "GOL", "GRANJA", "GRUPO", "GUANTE", "GUITARRA", "HABITACION",
        "HADA", "HELADO", "HELADERIA", "HERMANO", "HERMOSO", "HERRAMIENTA", "HIJO", "HOGAR", "HOMBRE", "HORA", "HOTEL",
        "HUERTA", "IDEA", "IGLESIA", "IMAGEN", "INFANCIA", "INQUIETO", "INTELIGENTE", "INVIERNO", "JARDIN", "JUEGO",
        "JORNADA", "JUGUETE", "JUGUETERIA", "JUNIO", "KILOMETRO", "LAGO", "LAMPARA", "LAPIZ", "LATIDO", "LECCION",
        "LECHE", "LEON", "LENGUA", "LIBRO", "LIBRERIA", "LUCHA", "LUZ", "LUMINOSO", "MAMA", "MAESTRO", "MAPA", "MAR",
        "MARCO", "MARIPOSA", "MARMOL", "MASCOTA", "MENSAJE", "MERCADO", "MES", "MESA", "MONTAÑA", "MUNDO", "MUSICA",
        "NACION", "NIEVE", "NOCHE", "NOMBRE", "NOVELA", "NOVIEMBRE", "NUBE", "NIÑO", "NIÑA", "OBJETO", "OLA", "OJOS",
        "OSASUNA", "OSO", "PALABRA", "PALACIO", "PALMERA", "PAPEL", "PAJARO", "PANTANO", "PARAGUAS", "PARQUE", "PARRILLA",
        "PELOTA", "PELICULA", "PERIODICO", "PERRO", "PERSONA", "PLANTA", "PLANETA", "PLAZA", "PLATO", "POESIA", "PUEBLO",
        "PUENTE", "PUERTA", "PUERTO", "QUESO", "RAIZ", "RATON", "REINA", "RELOJ", "RECUERDO", "REGALO", "REUNION", "RIO",
        "ROPA", "RAPIDO", "SALA", "SALUD", "SALON", "SABOR", "SECRETO", "SEMILLA", "SENDERO", "SIESTA", "SOCIEDAD",
        "SOL", "SOLUCION", "SOMBRERO", "SOMBRILLA", "SONRISA", "SUEÑO", "TRANQUILO", "TIERRA", "TAZA", "TECHO",
        "TELEVISIÓN", "TIEMPO", "TUNEL", "TREN", "UNIVERSIDAD", "VACACIONES", "VACA", "VENTANA", "VALLE", "VENTILADOR",
        "VERSO", "VIDA", "VINO", "VIENTO", "YATE", "ZANAHORIA", "ZOOLOGICO", "ZUMO"]

        matriz = inicializar_matriz(filas, columnas)
        for i in range(palabras_por_sopa):
            elegir_colocar_palabra(matriz, palabras, filas, columnas, palabras_sopa, posiciones_palabras)
        rellenar_sopa(matriz, filas, columnas)
        
        palabras_restantes = len(palabras_sopa)
        contador = 0
        
        while len(palabras_sopa) > 0:
            clear_output(wait=True)
            if palabras_restantes != len(palabras_sopa):
                print("\033[1;32mHAS ACERTADO LA PALABRA!!! SIGUE ASI!!! \033[0m")
                palabras_restantes = len(palabras_sopa)
            elif contador != 0:
                print("\033[1;31mHAS FALLADO, SIGUELO INTENTANDO!!! \033[0m")
            print()
            print("    ", end="")
            for j in range(len(matriz[0])):
                # Adjust spacing for double digits if necessary, but simple for now
                print(f"{j+1:<3}", end=" ")
            print()
            print(" - " * (len(matriz) * 2)) # Adjusted separator
            for i in range(len(matriz)):
                print(f"{i+1:<2} |", end=" ")
                for j in range(len(matriz[0])):
                    print(f"{matriz[i][j]:<3}", end=" ")
                print()
            print()
            print("Palabras en la sopa: ", end="")
            print(", ".join(palabras_sopa))
            print()
            
            encontrar_palabra_en_sopa(palabras_sopa, posiciones_palabras, palabras_acertadas, filas)
            
            if contador != 0:
                # This part in original code was printed after finding/not finding?
                # Actually in original code it prints "Palabras que te quedan..." if contador!=0 inside the loop
                # But here we just cleared output.
                pass
            
            contador += 1
            
        print("\033[1;32mHAS GANADO EL JUEGO!!! ENHORABUENA!!! \033[0m")
        print("Quieres seguir jugando (Introduce 's' si quieres seguir jugando y cualquier otra letra si no)?")
        n = input()

if __name__ == "__main__":
    main()
