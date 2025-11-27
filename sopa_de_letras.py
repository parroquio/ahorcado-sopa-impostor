import random

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
                    while columnas<longitud:
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
                    while columnas<longitud:
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
                    while columnas<longitud or filas<longitud:
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
                    while columnas<longitud or filas<longitud:
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
                    while filas<longitud:
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
                    while filas<longitud:
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
           
matriz=[]
palabras_sopa=[]
posiciones_palabras=[]
filas=4 #minimo 4
columnas=4 #minimo 4
palabras_por_sopa=2
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
for i in matriz:
    for j in i:
        print(j,end="\t")
    print()
print(palabras_sopa)
print(posiciones_palabras)