import random

#Dibujos para el ahorcado
#Juego para empezar
def dibujo_inicial():
    for i in range(N):
        for j in range(N):
            #########1 fila###########
            if i == 0 and not(j == 0):
                print('_', end=' ')
            elif i == 0 and j == 0:
                print(' ',end=' ')
            #########2 fila###########
            elif i == 1 and (j == 1 or j == 7):
                print('|',end=' ')
            elif i == 1 and not(j == 1 or j == 7):
                print(' ',end=' ')
            #########3 fila###########
            elif i ==2 and j == 7:
                print('|',end=' ')
            elif i ==2 and not(j == 7):
                print(' ',end=' ')
            #########4 fila###########
            elif i ==3 and j == 7:
                print('|',end=' ')
            elif i ==3 and not(j == 7):
                print(' ',end=' ')
            #########5 fila###########
            elif i ==4 and j == 7:
                print('|',end=' ')
            elif i ==4 and not(j == 7):
                print(' ',end=' ')
            #########6 fila###########
            elif i ==5 and j == 7:
                print('|',end=' ')
            elif i ==5 and not(j == 7):
                print(' ',end=' ')
            #########7 fila###########
            elif i ==6 and j == 7:
                print('|',end=' ')
            elif i ==6 and not(j == 7):
                print(' ',end=' ')
            #########8 fila###########
            elif i == 7 and (j == 6 or j == 7):
                print('--',end=' ')
            elif i == 7 and not(j == 6 or j == 7):
                print(' ',end=' ')
            
        print()

#primer error
def primer_error():
    for i in range(N):
        for j in range(N):
            #########1 fila###########
            if i == 0 and not(j == 0):
                print('_', end=' ')
            elif i == 0 and j == 0:
                print(' ',end=' ')
            #########2 fila###########
            elif i == 1 and (j == 1 or j == 7):
                print('|',end=' ')
            elif i == 1 and not(j == 1 or j == 7):
                print(' ',end=' ')
            #########3 fila###########
            elif i ==2 and j == 7:
                print('|',end=' ')
            elif i ==2 and j == 1:
                print('O',end=' ')
            elif i ==2 and not(j == 7 or j == 1):
                print(' ',end=' ')
            #########4 fila###########
            elif i ==3 and j == 7:
                print('|',end=' ')
            elif i ==3 and not(j == 7):
                print(' ',end=' ')
            #########5 fila###########
            elif i ==4 and j == 7:
                print('|',end=' ')
            elif i ==4 and not(j == 7):
                print(' ',end=' ')
            #########6 fila###########
            elif i ==5 and j == 7:
                print('|',end=' ')
            elif i ==5 and not(j == 7):
                print(' ',end=' ')
            #########7 fila###########
            elif i ==6 and j == 7:
                print('|',end=' ')
            elif i ==6 and not(j == 7):
                print(' ',end=' ')
            #########8 fila###########
            elif i == 7 and (j == 6 or j == 7):
                print('--',end=' ')
            elif i == 7 and not(j == 6 or j == 7):
                print(' ',end=' ')
            
        print()

#segundo error
def segundo_error():
    for i in range(N):
        for j in range(N):
            #########1 fila###########
            if i == 0 and not(j == 0):
                print('_', end=' ')
            elif i == 0 and j == 0:
                print(' ',end=' ')
            #########2 fila###########
            elif i == 1 and (j == 1 or j == 7):
                print('|',end=' ')
            elif i == 1 and not(j == 1 or j == 7):
                print(' ',end=' ')
            #########3 fila###########
            elif i ==2 and j == 7:
                print('|',end=' ')
            elif i ==2 and j == 1:
                print('O',end=' ')
            elif i ==2 and not(j == 7 or j == 1):
                print(' ',end=' ')
            #########4 fila###########
            elif i ==3 and j == 7:
                print('|',end=' ')
            elif i ==3 and j == 1:
                print('|',end=' ')
            elif i ==3 and not(j == 1 or j == 7 ):
                print(' ',end=' ')
            #########5 fila###########
            elif i ==4 and j == 7:
                print('|',end=' ')
            elif i ==4 and not(j == 7):
                print(' ',end=' ')
            #########6 fila###########
            elif i ==5 and j == 7:
                print('|',end=' ')
            elif i ==5 and not(j == 7):
                print(' ',end=' ')
            #########7 fila###########
            elif i ==6 and j == 7:
                print('|',end=' ')
            elif i ==6 and not(j == 7):
                print(' ',end=' ')
            #########8 fila###########
            elif i == 7 and (j == 6 or j == 7):
                print('--',end=' ')
            elif i == 7 and not(j == 6 or j == 7):
                print(' ',end=' ')
            
        print()

#tercer error
def tercer_error():
    for i in range(N):
        for j in range(N):
            #########1 fila###########
            if i == 0 and not(j == 0):
                print('_', end=' ')
            elif i == 0 and j == 0:
                print(' ',end=' ')
            #########2 fila###########
            elif i == 1 and (j == 1 or j == 7):
                print('|',end=' ')
            elif i == 1 and not(j == 1 or j == 7):
                print(' ',end=' ')
            #########3 fila###########
            elif i ==2 and j == 7:
                print('|',end=' ')
            elif i ==2 and j == 1:
                print('O',end=' ')
            elif i ==2 and not(j == 7 or j == 1):
                print(' ',end=' ')
            #########4 fila###########
            elif i ==3 and j == 7:
                print('|',end=' ')
            elif i ==3 and j == 0:
                print('/',end=' ')
            elif i ==3 and j == 1:
                print('|',end=' ')
            elif i ==3 and not(j == 0 or j == 1 or j == 7 ):
                print(' ',end=' ')
            #########5 fila###########
            elif i ==4 and j == 7:
                print('|',end=' ')
            elif i ==4 and not(j == 7):
                print(' ',end=' ')
            #########6 fila###########
            elif i ==5 and j == 7:
                print('|',end=' ')
            elif i ==5 and not(j == 7):
                print(' ',end=' ')
            #########7 fila###########
            elif i ==6 and j == 7:
                print('|',end=' ')
            elif i ==6 and not(j == 7):
                print(' ',end=' ')
            #########8 fila###########
            elif i == 7 and (j == 6 or j == 7):
                print('--',end=' ')
            elif i == 7 and not(j == 6 or j == 7):
                print(' ',end=' ')
            
        print()

# #cuarto error
def cuarto_error():
    for i in range(N):
        for j in range(N):
            #########1 fila###########
            if i == 0 and not(j == 0):
                print('_', end=' ')
            elif i == 0 and j == 0:
                print(' ',end=' ')
            #########2 fila###########
            elif i == 1 and (j == 1 or j == 7):
                print('|',end=' ')
            elif i == 1 and not(j == 1 or j == 7):
                print(' ',end=' ')
            #########3 fila###########
            elif i ==2 and j == 7:
                print('|',end=' ')
            elif i ==2 and j == 1:
                print('O',end=' ')
            elif i ==2 and not(j == 7 or j == 1):
                print(' ',end=' ')
            #########4 fila###########
            elif i ==3 and j == 7:
                print('|',end=' ')
            elif i ==3 and j == 0:
                print('/',end=' ')
            elif i ==3 and j == 1:
                print('|',end=' ')
            elif i ==3 and j == 2:
                print('\\',end=' ')
            elif i ==3 and not(j == 0 or j == 1 or j == 2 or j == 7 ):
                print(' ',end=' ')
            #########5 fila###########
            elif i ==4 and j == 7:
                print('|',end=' ')
            elif i ==4 and not(j == 7):
                print(' ',end=' ')
            #########6 fila###########
            elif i ==5 and j == 7:
                print('|',end=' ')
            elif i ==5 and not(j == 7):
                print(' ',end=' ')
            #########7 fila###########
            elif i ==6 and j == 7:
                print('|',end=' ')
            elif i ==6 and not(j == 7):
                print(' ',end=' ')
            #########8 fila###########
            elif i == 7 and (j == 6 or j == 7):
                print('--',end=' ')
            elif i == 7 and not(j == 6 or j == 7):
                print(' ',end=' ')
            
        print()

# #quinto error
def quinto_error():
    for i in range(N):
        for j in range(N):
            #########1 fila###########
            if i == 0 and not(j == 0):
                print('_', end=' ')
            elif i == 0 and j == 0:
                print(' ',end=' ')
            #########2 fila###########
            elif i == 1 and (j == 1 or j == 7):
                print('|',end=' ')
            elif i == 1 and not(j == 1 or j == 7):
                print(' ',end=' ')
            #########3 fila###########
            elif i ==2 and j == 7:
                print('|',end=' ')
            elif i ==2 and j == 1:
                print('O',end=' ')
            elif i ==2 and not(j == 7 or j == 1):
                print(' ',end=' ')
            #########4 fila###########
            elif i ==3 and j == 7:
                print('|',end=' ')
            elif i ==3 and j == 0:
                print('/',end=' ')
            elif i ==3 and j == 1:
                print('|',end=' ')
            elif i ==3 and j == 2:
                print('\\',end=' ')
            elif i ==3 and not(j == 0 or j == 1 or j == 2 or j == 7 ):
                print(' ',end=' ')
            #########5 fila###########
            elif i ==4 and j == 7:
                print('|',end=' ')
            elif i == 4 and j == 1:
                print('|',end=' ')
            elif i ==4 and not(j == 7 or j == 1):
                print(' ',end=' ')
            #########6 fila###########
            elif i ==5 and j == 7:
                print('|',end=' ')
            elif i ==5 and not(j == 7):
                print(' ',end=' ')
            #########7 fila###########
            elif i ==6 and j == 7:
                print('|',end=' ')
            elif i ==6 and not(j == 7):
                print(' ',end=' ')
            #########8 fila###########
            elif i == 7 and (j == 6 or j == 7):
                print('--',end=' ')
            elif i == 7 and not(j == 6 or j == 7):
                print(' ',end=' ')
            
        print()

# #sexto error
def sexto_error():
    for i in range(N):
        for j in range(N):
            #########1 fila###########
            if i == 0 and not(j == 0):
                print('_', end=' ')
            elif i == 0 and j == 0:
                print(' ',end=' ')
            #########2 fila###########
            elif i == 1 and (j == 1 or j == 7):
                print('|',end=' ')
            elif i == 1 and not(j == 1 or j == 7):
                print(' ',end=' ')
            #########3 fila###########
            elif i ==2 and j == 7:
                print('|',end=' ')
            elif i ==2 and j == 1:
                print('O',end=' ')
            elif i ==2 and not(j == 7 or j == 1):
                print(' ',end=' ')
            #########4 fila###########
            elif i ==3 and j == 7:
                print('|',end=' ')
            elif i ==3 and j == 0:
                print('/',end=' ')
            elif i ==3 and j == 1:
                print('|',end=' ')
            elif i ==3 and j == 2:
                print('\\',end=' ')
            elif i ==3 and not(j == 0 or j == 1 or j == 2 or j == 7 ):
                print(' ',end=' ')
            #########5 fila###########
            elif i ==4 and j == 7:
                print('|',end=' ')
            elif i == 4 and j == 1:
                print('|',end=' ')
            elif i ==4 and not(j == 7 or j == 1):
                print(' ',end=' ')
            #########6 fila###########
            elif i == 5 and j == 0:
                print('/',end=' ')
            elif i ==5 and j == 7:
                print('|',end=' ')
            elif i ==5 and not(j == 0 or j == 7):
                print(' ',end=' ')
            #########7 fila###########
            elif i ==6 and j == 7:
                print('|',end=' ')
            elif i ==6 and not(j == 7):
                print(' ',end=' ')
            #########8 fila###########
            elif i == 7 and (j == 6 or j == 7):
                print('--',end=' ')
            elif i == 7 and not(j == 6 or j == 7):
                print(' ',end=' ')
            
        print()

#ultimo error / fin de la partida
def ultimo_dibujo():
    for i in range(N):
        for j in range(N):
            #########1 fila###########
            if i == 0 and not(j == 0):
                print('_', end=' ')
            elif i == 0 and j == 0:
                print(' ',end=' ')
            #########2 fila###########
            elif i == 1 and (j == 1 or j == 7):
                print('|',end=' ')
            elif i == 1 and not(j == 1 or j == 7):
                print(' ',end=' ')
            #########3 fila###########
            elif i ==2 and j == 7:
                print('|',end=' ')
            elif i ==2 and j == 1:
                print('O',end=' ')
            elif i ==2 and not(j == 7 or j == 1):
                print(' ',end=' ')
            #########4 fila###########
            elif i ==3 and j == 7:
                print('|',end=' ')
            elif i ==3 and j == 0:
                print('/',end=' ')
            elif i ==3 and j == 1:
                print('|',end=' ')
            elif i ==3 and j == 2:
                print('\\',end=' ')
            elif i ==3 and not(j == 0 or j == 1 or j == 2 or j == 7 ):
                print(' ',end=' ')
            #########5 fila###########
            elif i ==4 and j == 7:
                print('|',end=' ')
            elif i == 4 and j == 1:
                print('|',end=' ')
            elif i ==4 and not(j == 7 or j == 1):
                print(' ',end=' ')
            #########6 fila###########
            elif i == 5 and j == 0:
                print('/',end=' ')
            elif i == 5 and j == 2:
                print('\\',end=' ')
            elif i ==5 and j == 7:
                print('|',end=' ')
            elif i ==5 and not(j == 0 or j == 2 or j == 7):
                print(' ',end=' ')
            #########7 fila###########
            elif i ==6 and j == 7:
                print('|',end=' ')
            elif i ==6 and not(j == 7):
                print(' ',end=' ')
            #########8 fila###########
            elif i == 7 and (j == 6 or j == 7):
                print('--',end=' ')
            elif i == 7 and not(j == 6 or j == 7):
                print(' ',end=' ')
            
        print()

#en esta funcion elege una palabra de las listas con lo longitud introducida
def elegir_longitud(x):
    longitud = int(input('Introduce la longitud de la palabra que quieres adivinar (entre 3 y 7 letras): '))

    if longitud == 3:
        palabra = Palabras_3_letras[x]
    elif longitud == 4:
        palabra = Palabras_4_letras[x]
    elif longitud == 5:
        palabra = Palabras_5_letras[x]
    elif longitud == 6:
        palabra = Palabras_6_letras[x]
    elif longitud == 7:
        palabra = Palabras_7_letras[x]

    return palabra

#pide una letra al usuario y se asegura de que la ha introducido bien
def pedir_letra():
    while True:
        letra = input('Ahora tienes que introducir letras del abecedario una a una (excepto la ñ),' 
    ' si coinciden se colocaran, y si no habras perdido una vida: ').upper()
        
        if len(letra) != 1:
            print()
            print('Has introducido mas de un elemento, intentalo de nuevo.')
            print()
            continue #la funcion vuelve a empezar
        
        if letra.upper() == 'Ñ':
            print()
            print('La letra ñ no esta permitida.')
            print()
            continue #la funcion vuelve a empezar

        if not(letra.upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            print()
            print('Solo son validas las letras del abecedario, intentalo de nuevo')
            print()
            continue #la funcion vuelve a empezar
            
        return letra
    
#muestra el progreso del usuario
def mostrar_progreso(palabra, letras_acertadas):
    progreso = []

    for i in palabra:
        if i in letras_acertadas:
            progreso.append(i)
        else:
            progreso.append('_')
    print(*progreso)

#funcion que imprime el dibujo correspondiente en base a los fallos
def mostrar_dibujo(fallos):
    
    if fallos == 0:
        dibujo_inicial()
    elif fallos == 1:
        primer_error()
    elif fallos == 2:
        segundo_error()
    elif fallos == 3:
        tercer_error()
    elif fallos == 4:
        cuarto_error()
    elif fallos == 5:
        quinto_error()
    elif fallos == 6:
        sexto_error()
    elif fallos >= 7:
        ultimo_dibujo()


N = 8

#Listas
Palabras_3_letras = ["SOL", "MAR", "PAN", "GAS", "LUZ", "AVE", "RIO", "OLA", "PIE", "SAL",
                        "BAR", "PAZ", "OJO", "UVA", "TIO"]
Palabras_4_letras = ["CASA", "MESA", "LUNA", "PATO", "GATO","RATA", "RANA", "FLOR", "FARO", "CAMA",
                    "LOBO", "SOPA", "PALO", "PESO", "PERO"]
Palabras_5_letras = ["QUESO", "HOJAS", "FRESA", "MANGO", "PLUMA","BICHO", "SUELO", "TECHO", "PARED", "CALOR",
                    "TORRE", "LLAVE", "NARIZ", "CARNE"]
Palabras_6_letras = ["PERROS", "GATITO", "RATONA", "LUCERO", "SILLAS", "PLAYAS", "BARCOS", "CAMPOS", "LIBROS",
                    "ZAPATO", "CAMISA", "MONEDA", "TRENES", "PUERTA", "PIEDRA"]
Palabras_7_letras = ["ZAPATOS", "BOTELLA", "VENTANA", "PUERTAS", "COCINAS","LIBRERO", "ARMARIO", "ANILLOS", 
                    "ESTUCHE", "PELUCHE","CARPETA", "PLANETA", "CABALLO", "CARRERA", "CAMINOS"]

#Introducción
print()
print('Has escogido jugar el juego AHORCADO')
print()

#Saca un número aleatorio
x = random.randint(0, 14)

palabra = elegir_longitud(x)
letras_acertadas = []
letras_falladas = []
fallos = 0
max_falllos = 7

#en el siguiente while entra si se pueden hacer mas fallos y si hay mas letras para adivinar
while fallos < max_falllos and len(letras_acertadas) < len(set(palabra)):

    mostrar_progreso(palabra, letras_acertadas)
    #aqui se muestran los fallos
    print()
    print('Letras falladas: ', *letras_falladas or 'ninguna')
    print()
    #llamamos a la funcion pedir letra
    letra = pedir_letra()
    #comprobueba si la letra introducida ya habia sido usada
    if (letra in letras_acertadas) or (letra in letras_falladas):
        print()
        print('Ya habias usado esta letra, prueba con otra.')
        print()
        continue #la funcion vuelve a empezar
    #Si acierta la letra, imprime la frase
    if letra in palabra:
        letras_acertadas.append(letra)
        print()
        print('Has acertado la letra!!')
        print()
    #Si falla la letra, imprime la frase
    else: 
        fallos += 1
        letras_falladas.append(letra)
        print()
        print('Has fallado. Es el fallo numero {}'.format(fallos))
        print()
        mostrar_dibujo(fallos)
#imprime la palabra que buscaba, y la frase de la victoria
if len(letras_acertadas) == len(set(palabra)):
    print()
    mostrar_progreso(palabra, letras_acertadas)
    print()
    print('ENHORABUENA!! Has adivinado la palabra que buscabas')
    print()
#Si no ha acertado la palabra, imprime la frase y la palabra que estaba buscando
else:
    print()
    print('¡¡¡¡AHORCADO!!!! :( ')
    print()
    print('La palabra que buscabas era: ', palabra)

