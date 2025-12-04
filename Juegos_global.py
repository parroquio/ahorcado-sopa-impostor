import os
import time
import sys
import random
import select
from IPython.display import clear_output

# Colores ANSI
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

def clear():
    os.system('clear')

def print_header():
    print(f"{CYAN}╔══════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║                                                              ║{RESET}")
    print(f"{CYAN}║   {YELLOW}{BOLD}       S A L A   D E   J U E G O S   A R C A D E        {CYAN}   ║{RESET}")
    print(f"{CYAN}║                                                              ║{RESET}")
    print(f"{CYAN}╚══════════════════════════════════════════════════════════════╝{RESET}")
    print()

# Limpiamos la pantalla y mostramos el encabezado
clear()
print_header()

# Mostramos las opciones
print(f"{BOLD}Selecciona tu desafío:{RESET}\n")
print(f"  {GREEN}[1]{RESET} {BOLD}Sopa de Letras{RESET}   {WHITE}- Encuentra las palabras ocultas{RESET}")
print(f"  {RED}[2]{RESET} {BOLD}Impostor{RESET}         {WHITE}- Descubre al traidor entre nosotros{RESET}")
print(f"  {BLUE}[3]{RESET} {BOLD}Ahorcado{RESET}         {WHITE}- Adivina la palabra antes de que sea tarde{RESET}")
print(f"\n  {MAGENTA}[0]{RESET} {BOLD}Salir{RESET}")
print("\n")

# Guardamos la respuesta en una variable
opcion = input(f"{YELLOW}>> Elige una opción: {RESET}")

# Aquí puedes continuar con tus ifs
if opcion == "1":

    def inicializar_matriz (filas,columnas):
        for i in range(filas):
            fila=[0]*columnas
            matriz.append(fila.copy())

    def elegir_colocar_palabra(matriz,palabras,filas,columnas):
        palabra=random.choice(palabras)
        longitud=len(palabra)
        contador=0
        horizontal_vertical=random.choice(["horizontal", "vertical","diagonal"])

        #Caso colocar palabra en Horizontal
        if horizontal_vertical=="horizontal":
            #si la palabra elegida es mas grande que la sopa de letras, cambiar la palabra
            while columnas<longitud:
                palabra=random.choice(palabras)
                longitud=len(palabra)
            #elegir si poner la palabra noraml o del reves
            direccion=random.choice(["normal","reversa"])
            #caso palabra normal
            if direccion=="normal":
                #validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
                validar=False
                while validar==False:
                    fila=random.randint(0,filas-1)
                    columna=random.randint(0,columnas-longitud)
                    for i in range(longitud):
                        if matriz[fila][columna+i]!=0 and matriz[fila][columna+i]!=palabra[i]:
                            validar=False
                            break
                        validar=True
                    contador+=1
                    #para que si es impsosible colocar esa palabra en la sopa de letras, que cambie de palabra
                    if contador%50==0:
                        palabra=random.choice(palabras)
                        longitud=len(palabra)
                        while columnas<=longitud:
                            palabra=random.choice(palabras)
                            longitud=len(palabra)
                #almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir
                palabras.remove(palabra)
                palabras_sopa.append(palabra)
                posiciones_palabras.append({"palabra":palabra,"inicio":(fila, columna),"final":(fila, columna+longitud-1)})
                #coloca la palabra
                for i in range(longitud):
                    matriz[fila][columna+i]=palabra[i]
            #caso palabra del reves
            else:
                #doy la vuelta a la palabra y uso la logica del codigo de la palabra normal
                palabra=palabra[::-1]
                #validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
                validar=False
                while validar==False:
                    fila=random.randint(0,filas-1)
                    columna=random.randint(0,columnas-longitud)
                    for i in range(longitud):
                        if matriz[fila][columna+i]!=0 and matriz[fila][columna+i]!=palabra[i]:
                            validar=False
                            break
                        validar=True
                    contador+=1
                    #para que si es impsosible colocar esa palabra en la sopa de letras, que cambie de palabra
                    if contador%50==0:
                        palabra=random.choice(palabras)
                        longitud=len(palabra)
                        while columnas<=longitud:
                            palabra=random.choice(palabras)
                            longitud=len(palabra)
                        palabra=palabra[::-1]
                #almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir (todo ello dandole la vuelta otra vez ya que ya lo teniamos del reves)
                palabras.remove(palabra[::-1])
                palabras_sopa.append(palabra[::-1])
                posiciones_palabras.append({"palabra":palabra[::-1],"inicio":(fila, columna+longitud-1),"final":(fila, columna)})
                #coloca la palabra
                for i in range(longitud):
                    matriz[fila][columna+i]=palabra[i]
                
        #Caso colocar palabra en Diagonal 
        if horizontal_vertical=="diagonal":
            #si la palabra elegida es mas grande que la sopa de letras, cambiar la palabra
            while columnas<longitud or filas<longitud:
                palabra=random.choice(palabras)
                longitud=len(palabra)
            #elegir si poner la palabra normal o del reves
            direccion=random.choice(["normal","reversa"])
            #caso palabra normal
            if direccion=="normal":
                #validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
                validar=False
                while validar==False:
                    fila=random.randint(0,filas-longitud)
                    columna=random.randint(0,columnas-longitud)
                    for i in range(longitud):
                        if matriz[fila+i][columna+i]!=0 and matriz[fila+i][columna+i]!=palabra[i]:
                            validar=False
                            break
                        validar=True
                    contador+=1
                    #para que si es impsosible colocar esa palabra en la sopa de letras, que cambie de palabra
                    if contador%50==0:
                        palabra=random.choice(palabras)
                        longitud=len(palabra)
                        while columnas<=longitud or filas<=longitud:
                            palabra=random.choice(palabras)
                            longitud=len(palabra)
                #almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir
                palabras.remove(palabra)
                palabras_sopa.append(palabra)
                posiciones_palabras.append({"palabra":palabra,"inicio":(fila, columna),"final":(fila+longitud-1, columna+longitud-1)})
                #coloca la palabra
                for i in range(longitud):
                    matriz[fila+i][columna+i]=palabra[i]
            #caso palabra del reves
            else:
                #doy la vuelta a la palabra y uso la logica del codigo de la palabra normal
                palabra=palabra[::-1]
                #validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
                validar=False
                while validar==False:
                    fila=random.randint(0,filas-longitud)
                    columna=random.randint(0,columnas-longitud)
                    for i in range(longitud):
                        if matriz[fila+i][columna+i]!=0 and matriz[fila+i][columna+i]!=palabra[i]:
                            validar=False
                            break
                        validar=True
                    contador+=1
                    #para que si es impsosible colocar esa palabra en la sopa de letras, que cambie de palabra
                    if contador%50==0:
                        palabra=random.choice(palabras)
                        longitud=len(palabra)
                        while columnas<=longitud or filas<=longitud:
                            palabra=random.choice(palabras)
                            longitud=len(palabra)
                        palabra=palabra[::-1]
                #almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir (todo ello dandole la vuelta otra vez ya que ya lo teniamos del reves)
                palabras.remove(palabra[::-1])
                palabras_sopa.append(palabra[::-1])
                posiciones_palabras.append({"palabra":palabra[::-1],"inicio":(fila+longitud-1, columna+longitud-1),"final":(fila, columna),})
                #coloca la palabra
                for i in range(longitud):
                    matriz[fila+i][columna+i]=palabra[i]

        #Caso colocar palabra en vertical
        elif horizontal_vertical=="vertical":
            #si la palabra elegida es mas grande que la sopa de letras, cambiar la palabra
            while filas<longitud:
                palabra=random.choice(palabras)
                longitud=len(palabra)
            #elegir si poner la palabra normal o del reves
            direccion=random.choice(["normal","reversa"])
            #caso palabra normal
            if direccion=="normal":
                #validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
                validar=False
                while validar==False:
                    fila=random.randint(0,filas-longitud)
                    columna=random.randint(0,columnas-1)
                    for i in range(longitud):
                        if matriz[fila+i][columna]!=0 and matriz[fila+i][columna]!=palabra[i]:
                            validar=False
                            break
                        validar=True
                    contador+=1
                    #para que si es impsosible colocar esa palabra en la sopa de letras, que cambie de palabra
                    if contador%50==0:
                        palabra=random.choice(palabras)
                        longitud=len(palabra)
                        while filas<=longitud:
                            palabra=random.choice(palabras)
                            longitud=len(palabra)
                #almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir
                palabras.remove(palabra)
                palabras_sopa.append(palabra)
                posiciones_palabras.append({"palabra":palabra,"inicio":(fila, columna),"final":(fila+longitud-1, columna),})
                #coloca la palabra
                for i in range(longitud):
                    matriz[fila+i][columna]=palabra[i]
            #caso palabra del reves
            else:
                #doy la vuelta a la palabra y uso la logica del codigo de la palabra normal
                palabra=palabra[::-1]
                #validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
                validar=False
                while validar==False:
                    fila=random.randint(0,filas-longitud)
                    columna=random.randint(0,columnas-1)
                    for i in range(longitud):
                        if matriz[fila+i][columna]!=0 and matriz[fila+i][columna]!=palabra[i]:
                            validar=False
                            break
                        validar=True
                    contador+=1
                    #para que si es impsosible colocar esa palabra en la sopa de letras, que cambie de palabra
                    if contador%50==0:
                        palabra=random.choice(palabras)
                        longitud=len(palabra)
                        while filas<=longitud:
                            palabra=random.choice(palabras)
                            longitud=len(palabra)
                        palabra=palabra[::-1]
                #almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir (todo ello dandole la vuelta otra vez ya que ya lo teniamos del reves)
                palabras.remove(palabra[::-1])
                palabras_sopa.append(palabra[::-1])
                posiciones_palabras.append({"palabra":palabra[::-1],"inicio":(fila+longitud-1, columna),"final":(fila, columna),})
                #coloca la palabra
                for i in range(longitud):
                    matriz[fila+i][columna]=palabra[i]


    def rellenar_sopa(matriz,filas,columnas):
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if matriz[i][j]==0:
                    matriz[i][j]=chr(random.randint(65,90))

    def encontrar_palabra_en_sopa(palabras_sopa,posiciones_palabras,palabras_acertadas, filas):
        filas=str(filas)
        intento_fila_inicial=input("Introduce el número de la fila en la que se encuentra la inicial de la palabra: ")
        while intento_fila_inicial.isdigit==False or intento_fila_inicial>filas:
            intento_fila_inicial=input("No puede ser ni mas grande que el tamaño de la sopa ni un caracter, pruebe otra vez: ")
            intento_fila_inicial=int(intento_fila_inicial)       
        intento_columna_inicial=input("Introduce el número de la columna en la que se encuentra la inicial de la palabra: ")
        while intento_columna_inicial.isdigit==False or intento_columna_inicial>filas:
            intento_columna_inicial=input("No puede ser ni mas grande que el tamaño de la sopa ni un caracter, pruebe otra vez: ")
            intento_columna_inicial=int(intento_columna_inicial)    
        intento_fila_final=input("Introduce el número de la fila en la que se encuentra la última letra de la palabra: ")
        while intento_fila_final.isdigit==False or intento_fila_final>filas:
            intento_fila_final=input("No puede ser ni mas grande que el tamaño de la sopa ni un caracter, pruebe otra vez: ")
            intento_fila_final=int(intento_fila_final)    
        intento_columna_final=input("Introduce el número de la columna en la que se encuentra la última letra de la palabra: ")
        while intento_columna_final.isdigit==False or intento_columna_final>filas:
            intento_columna_final=input("No puede ser ni mas grande que el tamaño de la sopa ni un caracter, pruebe otra vez: ")
            intento_columna_final=int(intento_columna_final)  
        intento_fila_inicial=int(intento_fila_inicial) 
        intento_columna_inicial=int(intento_columna_inicial)
        intento_fila_final=int(intento_fila_final)  
        intento_columna_final=int(intento_columna_final)   
        intento_fila_inicial-=1
        intento_columna_inicial-=1
        intento_fila_final-=1
        intento_columna_final-=1
        for i in range(len(palabras_sopa)):
            if posiciones_palabras[i]["inicio"]==(intento_fila_inicial, intento_columna_inicial) and posiciones_palabras[i]["final"]==(intento_fila_final, intento_columna_final):
                palabras_acertadas.append(posiciones_palabras[i]["palabra"])
                palabras_sopa.remove(posiciones_palabras[i]["palabra"])
                
    n="s"                    
    while n=="s" or n=="S":
        clear_output(wait=True)
        matriz=[]
        palabras_sopa=[]
        posiciones_palabras=[]
        palabras_acertadas=[]
        horizontal_vertical=None
        filas=input("Introduce de que tamaño quieres la matriz (Min 4): ")
        while filas.isdigit()==False or filas<"4":
            filas=input("No puedes introducir otros caracteres o número menores a 4, prube otra vez: ")
        columnas=int(filas)
        filas=columnas
        max_palabras_por_sopa=None
        if filas==4:
            max_palabras_por_sopa=None
        else:
            max_palabras_por_sopa=filas-1
            max_palabras_por_sopa=str(max_palabras_por_sopa)
        palabras_por_sopa=input("Introduce de cuantas palabras quieres que haya en la sopa (Max {}): ".format(max_palabras_por_sopa))
        while palabras_por_sopa.isdigit()==False or palabras_por_sopa>max_palabras_por_sopa:
            palabras_por_sopa=input("No puedes introducir otros caracteres o número mayores a {}, prube otra vez: ".format(max_palabras_por_sopa))
        palabras_por_sopa=int(palabras_por_sopa)
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
        inicializar_matriz(filas,columnas)
        for i in range(palabras_por_sopa):
            elegir_colocar_palabra(matriz,palabras,filas,columnas)
        rellenar_sopa(matriz,filas,columnas)
        palabras_restantes=len(palabras_sopa)
        contador=0
        while len(palabras_sopa)>0:
            if palabras_restantes!=len(palabras_sopa):
                print("\033[1;32mHAS ACERTADO LA PALABRA!!! SIGUE ASI!!! \033[0m") 
                palabras_restantes=len(palabras_sopa)
            elif contador!=0:
                print("\033[1;31mHAS FALLADO, SIGUELO INTENTANDO!!! \033[0m") 
            print()
            print("    ", end="")
            for j in range(len(matriz[0])):
                print(j+1, end="   ")
            print() 
            print(" - "*(len(matriz)*2-3))
            for i in range(len(matriz)):
                print(i+1, "|", end=" ")
                for j in range(len(matriz[0])):
                    print(matriz[i][j], end="   ")
                print()
            print()
            print("Palabras en la sopa: ", end="")
            for i in range (len(palabras_sopa)):
                if i+1!=len(palabras_sopa):
                    print(palabras_sopa[i],end=", ")
                else:
                    print(palabras_sopa[i],end="")
            print()
            encontrar_palabra_en_sopa(palabras_sopa,posiciones_palabras,palabras_acertadas, filas)
            if contador!=0:
                print("Palabras que te quedan en la sopa: ", palabras_sopa)
                print("Palabras acertadas: ", palabras_acertadas)
            contador+=1
            clear_output(wait=True)
        print("\033[1;32mHAS GANADO EL JUEGO!!! ENHORABUENA!!! \033[0m")
        print("Quieres seguir jugando (Introduce 's' si quieres seguir jugando y cualquier otra letra si no)?")
        n=input()
elif opcion == "2":

    palabras = [
        # Redes Sociales y Tecnología (Simplificada)
        "historia", "perfil", "usuario", "etiqueta", "filtro", "directo", "reels", "meme", "tendencia", "viral",
        "hashtag", "emoji", "notificación", "captura", "pantalla", "enlace", "código", "burbuja", "grupo", "chat",
        "búsqueda", "app", "plataforma", "streaming", "podcast", "vídeo", "audio", "micrófono",
        "gafas", "realidad", "avatar", "moneda", "cartera", "billete", "tarjeta", "donación", "premio", "desafío",
        # Ocio y Consumo
        "auriculares", "altavoz", "mando", "consola", "juego", "nivel", "equipo", "torneo", "puntuación", "jugador",
        "serie", "película", "palomitas", "cola", "entrada", "concierto", "festival", "escenario", "canción", "álbum",
        "ropa", "tienda", "marca", "diseño", "zapatillas", "gorra", "bolso", "botella", "mochila", "llave",
        "menú", "salsa", "postre", "receta", "tapa", "terraza", "café", "batido", "refresco",
        # Conceptos Sociales
        "debate", "opinión", "argumento", "postura", "crítica", "elogio", "bulo", "verdad", "mentira", "excusa",
        "promesa", "secreto", "duda", "confianza", "esperanza", "ilusión", "pasión", "motivación", "meta", "éxito",
        "fracaso", "presión", "estrés", "rutina", "equilibrio", "salud", "dieta", "ejercicio", "paciencia", "creatividad",
        "talento", "habilidad", "fuerza", "velocidad", "riesgo", "suerte", "miedo", "culpa", "perdón", "responsabilidad",
        # Lugares y Entorno
        "cafetería", "gimnasio", "parque", "plaza", "avenida", "carretera", "semáforo", "banco", "oficina", "biblioteca",
        "museo", "cine", "teatro", "piscina", "playa", "montaña", "sendero", "camping", "viaje", "maleta",
        "mapa", "guía", "hotel", "reserva", "destino", "recuerdo", "foto", "retrato", "selfie", "cámara",
        # Elementos Comunes
        "cable", "batería", "cargador", "ventilador", "espejo", "marco", "vela", "luz", "sombra", "ruido",
        "silencio", "sello", "sobre", "paquete", "caja", "tarro", "etiqueta", "cesta", "cubo", "calendario",
        "reloj", "hora", "minuto", "segundo", "día", "noche", "sol", "luna", "estrella", "planeta",
        # Estudio y Papelería
        "cuaderno", "libreta", "bolígrafo", "lápiz", "subrayador", "marcador", "papel", "hoja", "carpeta", "goma",
        "tijeras", "pegamento", "pizarra", "rotulador", "agenda", "apunte", "examen", "clase", "curso",
        # Comida Rápida y Aperitivos
        "pizza", "hamburguesa", "sushi", "pasta", "arroz", "tarta", "galleta", "chocolatina", "fruta", "verdura",
        "bebida", "zumo", "agua", "hielo", "tostada", "sandwich", "ensalada", "bocadillo", "recipiente", "fiambrera",
        # Utensilios de cocina y alimentos
        "tenedor", "cuchara", "plato", "vaso", "copa", "bandeja", "bol", "olla", "sartén", "nevera",
        "microondas", "tostadora", "licuadora", "exprimidor", "colador", "batidora", "escurridor", "termos", "servilleta", "mantel",
        "pan", "queso", "mantequilla", "aceite", "vinagre", "mostaza", "kétchup", "mayonesa", "especias", "perejil",
        "azúcar", "sal", "pimienta", "harina", "huevo", "leche", "yogur", "carne", "pescado", "pollo",
        "cerdo", "ternera", "cordero", "marisco", "postre", "caramelo", "bombón", "chuche",
        # Ropa, accesorios y aseo personal
        "calcetines", "medias", "jersey", "abrigo", "chaqueta", "bufanda", "guantes", "cinturón", "tirantes", "sombrero",
        "gorro", "capucha", "paraguas", "impermeable", "botas", "sandalias", "chanclas", "bañador", "toalla", "albornoz",
        "cepillo", "peine", "champú", "acondicionador", "jabón", "pasta", "colonia", "perfume", "crema", "maquillaje",
        "rímel", "pintalabios", "esmalte", "lima", "secador", "plancha", "cuchilla", "esponja", "papelera", "escoba",
        "fregona", "aspiradora", "detergente", "lejía", "suavizante", "percha", "armario", "cómoda", "sábana", "manta",
        # Instrumentos, herramientas y bricolaje
        "martillo", "clavo", "tornillo", "destornillador", "tuerca", "llave", "sierra", "taladro", "cinta", "pegamento",
        "tiza", "pincel", "pintura", "rodillo", "ladrillo", "cemento", "arena", "grava", "madera", "metal",
        "plástico", "cables", "enchufe", "interruptor", "pilas", "linterna", "candado", "cadena", "cuerda", "correa",
        "guitarra", "piano", "tambor", "flauta", "trompeta", "violín", "teclado", "partitura", "melodía", "ritmo",
        # Lugares y Partes del Cuerpo
        "escalera", "ascensor", "pasaje", "sótano", "ático", "garaje", "balcón", "terraza", "patio", "porche",
        "pasillo", "vestíbulo", "recepción", "Mendívil" "taquilla", "mostrador", "caja", "entrada", "salida", "meta", "poste",
        "cabeza", "cuerpo", "alma", "corazón", "brazo", "pierna",
        "mano", "pie", "dedo", "uña", "rodilla", "codo", "hombro", "espalda", "cuello", "rostro",
        "ojo", "nariz", "boca", "oreja", "pelo", "piel", "lengua", "diente", "bigote", "barba",
        # Conceptos y Medidas
        "metro", "kilómetro", "litro", "gramo", "kilo", "centímetro", "milímetro", "área", "volumen", "peso",
        "altura", "profundidad", "anchura", "distancia", "cantidad", "temperatura", "hora", "minuto", "siglo", "época",
        "semana", "mes", "año", "década", "calendario", "fecha", "promedio", "media", "resultado", "dato",
        "informe", "documento", "prueba", "regla", "concepto",
        # Animales y naturaleza
        "perro", "gato", "pájaro", "pez", "conejo", "ratón", "hormiga", "abeja", "mosca", "araña",
        "flor", "planta", "árbol", "raíz", "tallo", "hoja", "fruta", "semilla", "tierra", "barro",
        "agua", "río", "lago", "mar", "playa", "arena", "roca", "montaña", "bosque", "césped",
        "cielo", "nube", "lluvia", "sol", "luna", "estrella", "viento", "tormenta", "rayo", "trueno", "arcoíris",
        # Referencias a Frases y Escenas (Series)
        "chantaje", "moroso", "presidente", "comunidad", "deuda", "derrama", "junta", "vaciado", "despido", "negocio",
        "buhardilla", "ático", "portería", "chaleco", "burbuja", "leopardo", "vivienda", "propietario", "alquiler", "portero",
        "mafia", "sicario", "paella", "cacerolada", "piscina", "terraza", "patio", "ascensor", "escalera", "carril",
        "cuentista", "estafador", "mentira", "verdad", "discusión", "guerra", "tregua", "paz", "justicia", "fuga",
        "matrimonio", "divorcio", "relación", "pareja", "amante", "infidelidad", "placer", "vicio",
        "vampiro", "cruz", "castigo", "recompensa", "susto", "miedo", "temor", "fantasma", "bruja", "maldición",
        # Conceptos de Personajes
        "feminismo", "machismo", "solidaridad", "egoísmo", "egoismo", "ambición", "pereza", "lujuria", "avaricia",
        "orgullo", "vanidad", "locura", "cordura", "ansiedad", "pánico", "tranquilidad", "euforia", "depresión",
        "drama", "comedia", "tragicomedia", "ironía", "sarcasmo", "disfraz", "peluca", "gafas", "sombrero", "toga",
        "mística", "karma", "destino", "profecía", "vision", "milagro", "creencia", "fe", "dios", "demonio",
        # Objetos y Lugares Específicos
        "picaporte", "mirilla", "buzón", "portal", "garaje", "trastero", "cama", "camaelástica", "sofá", "televisor",
        "silla", "mesa", "armario", "nevera", "barra", "barbacoa", "cafetera", "tabaco", "alcohol", "cigarrillo",
        "peluquería", "clínica", "colegio", "campamento", "cárcel", "manicomio", "hospital", "ambulancia", "farmacia", "calle",
        "coche", "autobús", "furgoneta", "moto", "bicicleta", "taxi", "multa", "policía", "ley",
        # Frases de uso cotidiano (Sustantivos clave)
        "peligro", "locura", "pelotazo", "milagro", "grito", "silencio", "paciencia", "castigo", "burdel",
        "fabuloso", "terror", "broma", "desastre", "caos", "orden", "pacto", "traición", "familia", "vecindario",
        "alcalde", "político", "fraude", "impuesto", "ayuda", "papel", "bando",
        "caricia", "cachete", "bofetada", "abrazo", "beso", "toque", "mirada", "sonrisa", "ceño", "gesto",
        # Conceptos de la urbanización
        "urbanización", "ladrillo", "hipoteca", "crisis", "dinero", "banco", "inversión", "terreno", "parcela", "propiedad",
        "valla", "puerta", "jardin", "sociedad", "cultura", "clase", "pobreza", "riqueza", "poder",
        "venganza", "odio", "amor", "amistad", "religión", "ciencia", "historia", "mito", "leyenda", "cuento",
        # Más objetos de uso diario
        "anillo", "collar", "pulsera", "pendientes", "reloj", "perfume", "florero", "vasija", "estatua", "cuadro",
        "espejo", "alfombra", "cortina", "persiana", "cargador",
        "televisión", "cable", "antena", "radio", "auriculares", "disco", "cd", "vinilo", "cinta",
        # Sustantivos clave en diálogos (Ambigüedad)
        "pueblo", "ciudad", "barrio", "calle", "plaza", "avenida", "carretera", "semáforo", "puerto", "aeropuerto",
        "tren", "autobús", "tranvía", "taxista", "billete", "tarjeta", "máquina", "ticket", "parada", "estación"
        ]

    def seleccionar_impostor(n):
        #Esta funncion determina al impostor, siendo el n-ésimo jugador.
        impostor = random.randint(0, n-1)
        return impostor



    #Texto inicial que explica el juego.
    os.system('clear')

    print("Bienvenido al juego del impostor.")
    time.sleep(2.5)
    print("En este juego, uno de los jugadores será el impostor, el resto, el pueblo.")
    time.sleep(3)
    print("El pueblo sabe una palabra, la cual deben evitar que el impostor la identifique.")
    time.sleep(3)
    print("En cada ronda, el pueblo debe decir una palabra parecida o relacionada con la palabra secreta.")
    time.sleep(4)
    print("El sentido del juego es antihorario.")
    time.sleep(2.5)
    print("Al finalizar cada ronda, el pueblo debe votar quién creen que es el impostor.")
    time.sleep(3)
    print("El jugador con más votos será el impostor.")
    time.sleep(2.5)
    print("Si hay empate, o todos los votos en blanco, no se expulsa a nadie.")
    time.sleep(3)
    print("El juego termina cuando no queden impostores, que habrá ganado el pueblo,")
    print("o cuando queden 2 o menos jugadores, que habrá ganado el impostor.")
    time.sleep(6)

    os.system('clear')

    #Asigna la palabra secreta en la variable "palabra".
    x = random.randint(0, len(palabras)-1)
    palabra = palabras[x]

    #Aquí se añaden los jugadores.
    n = int(input("Introduce el número de jugadores: "))
    os.system('clear')

    jugadores = []

    for i in range(n):
        jugador = input("Introduce el nombre del jugador {}: ".format(i+1))
        jugadores.append(jugador)

    primeros_jugadores = jugadores.copy()

    res = "S"

    #Se selecciona al impostor.
    impostor = jugadores[seleccionar_impostor(n)]

    #Se muestra el rol de cada jugador. 
    #Se tiene que pasar el dispositivo a cada jugador para que pueda ver su rol.

    for nombre in jugadores:
        os.system('clear')
        print("Pase el dispositivo a {}".format(nombre))
        input("Presiona Enter para ver tu rol...")
        
        if nombre == impostor:
            print("Eres el \033[38;2;255;0;0mimpostor\033[0m.")
        else:
            print("Eres \033[38;2;0;255;0mpueblo\033[0m.")
            print("La palabra es: \033[1m{}\033[0m".format(palabra))
        
        input("Presiona Enter para ocultar tu rol...")
        os.system('clear')

    #Se inicia el juego.
    while res == "s" or res == "S":

        contador_impostores = 0
        partida_acabada = False



        minutos = n
        segundos = int(minutos * 60)
    #Menú que se ve durante la partida. Hay el mismo numero de jugadores que de minutos (5 jugadores = 5 minutos).
        while segundos > 0:
            mins, secs = divmod(segundos, 60)
            tiempo_formato = '{:02d}:{:02d}'.format(mins, secs)
            print("¡A jugar! Tiempo restante: {} (Pulsa Enter para terminar)".format(tiempo_formato), end='\r')
            
            r, _, _ = select.select([sys.stdin], [], [], 1)
            if r:
                input()
                break
                
            segundos -= 1

        os.system('clear')
        print("\n¡Tiempo agotado! Es hora de votar.")

        #Se muestra la lista de jugadores para que el pueblo pueda votar.
        for nombre in range(len(jugadores)):
            print("{}.\t".format(nombre+1), end='')
            print(jugadores[nombre])
            print()

        #Se recibe el voto del pueblo.
        voto = input("Introduzca el resultado de la votación (Vacío en caso de empate): ")

        if voto == "":
            print("Empate")
        else:
            print("Se ha votado a \033[1m{}\033[0m.".format(jugadores[int(voto)-1]))
            print("\n")

            #Se expulsa al jugador votado.
            if jugadores[int(voto)-1] == impostor:
                print("{} era el \033[38;2;255;0;0mimpostor\033[0m.".format(jugadores[int(voto)-1]))
            else:
                print("{} era \033[1minocente\033[0m.".format(jugadores[int(voto)-1]))
            
            jugadores.remove(jugadores[int(voto)-1])

            #Se verifica que sigan quedando impostores.
            for nombre in jugadores:
                if nombre == impostor:
                    contador_impostores += 1
            
            if contador_impostores == 0:
                print("Todos los impostores han sido expulsados. El pueblo ha ganado.")
                partida_acabada = True

            elif len(jugadores) <= 2:
                print("Solo quedan 2 jugadores. El impostor ha ganado.")
                partida_acabada = True

            if partida_acabada == False:
                res = input("¿Quieres jugar otra ronda? (s/n): ")
                if res == "s" or res == "S":
                    os.system('clear')
                    

            else:
                res = input("¿Quieres jugar otra partida con los mismos jugadores? (s/n): ")
                if res == "s" or res == "S":
                    jugadores = primeros_jugadores.copy()
                    contador_impostores = 0
                    partida_acabada = False
                    x = random.randint(0, len(palabras)-1)
                    palabra = palabras[x]
                    impostor = jugadores[seleccionar_impostor(n)]

                    for nombre in jugadores:
                        os.system('clear')
                        print("Pase el dispositivo a {}".format(nombre))
                        input("Presiona Enter para ver tu rol...")
        
                        if nombre == impostor:
                            print("Eres el \033[38;2;255;0;0mimpostor\033[0m.")
                        else:
                            print("Eres \033[38;2;0;255;0mpueblo\033[0m.")
                            print("La palabra es: \033[1m{}\033[0m".format(palabra))
        
                        input("Presiona Enter para ocultar tu rol...")
                        os.system('clear')


elif opcion == "3":

#OHIAN, PEGA AQUI TU CODIGO E IMPORTA LAS LIBRERIAS AL PRINCIPIO DEL CODIGO.