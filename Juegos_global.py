import os
import time
import random
from IPython.display import clear_output
import msvcrt


#Funciones de la Sopa de letras

#Funcion que crea una matriz de ceros del tamaño que pida el usuario
def inicializar_matriz (tamaño):
    for i in range(tamaño):
        fila=[0]*tamaño
        matriz.append(fila.copy())
#La funcion que elige una palabra de la lista, la añade con direccion y orientacion random y verifica que no moleste con otras
def elegir_colocar_palabra(matriz,palabras,tamaño):
    #elige una palabra random de la lista
    palabra=random.choice(palabras)
    longitud=len(palabra)
    contador=0
    horizontal_vertical_diagonal=random.choice(["horizontal", "vertical","diagonal"]) #elige orientación de la palabra

    #Caso colocar palabra en Horizontal
    if horizontal_vertical_diagonal=="horizontal":
        #si la palabra elegida es mas grande que la sopa de letras, cambiar la palabra
        while tamaño<longitud:
            palabra=random.choice(palabras)
            longitud=len(palabra)
        #elegir si poner la palabra noraml o del reves
        direccion=random.choice(["normal","reversa"])
        #caso palabra normal
        if direccion=="normal":
            #validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
            validar=False
            while validar==False:
                fila=random.randint(0,tamaño-1)
                columna=random.randint(0,tamaño-longitud)
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
                    while tamaño<longitud:
                        palabra=random.choice(palabras)
                        longitud=len(palabra)
            #almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir
            palabras.remove(palabra)
            palabras_sopa.append(palabra)
            posiciones_palabras.append({"palabra":palabra,"inicio":(fila, columna),"final":(fila, columna+longitud-1)})
            #coloca la palabra
            for i in range(longitud):
                if modo=="2":
                    emoji=ord(palabra[i])-65
                    matriz[fila][columna+i]=modo_emoji[emoji]
                else:
                    matriz[fila][columna+i]=palabra[i]
        #caso palabra del reves
        else:
            #doy la vuelta a la palabra y uso la logica del codigo de la palabra normal
            palabra=palabra[::-1]
            #validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
            validar=False
            while validar==False:
                fila=random.randint(0,tamaño-1)
                columna=random.randint(0,tamaño-longitud)
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
                    while tamaño<longitud:
                        palabra=random.choice(palabras)
                        longitud=len(palabra)
                    palabra=palabra[::-1]
            #almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir (todo ello dandole la vuelta otra vez ya que ya lo teniamos del reves)
            palabras.remove(palabra[::-1])
            palabras_sopa.append(palabra[::-1])
            posiciones_palabras.append({"palabra":palabra[::-1],"inicio":(fila, columna+longitud-1),"final":(fila, columna)})
            #coloca la palabra
            for i in range(longitud):
                if modo=="2":
                    emoji=ord(palabra[i])-65
                    matriz[fila][columna+i]=modo_emoji[emoji]
                else:
                    matriz[fila][columna+i]=palabra[i]
                
    #Caso colocar palabra en Diagonal 
    if horizontal_vertical_diagonal=="diagonal":
        #si la palabra elegida es mas grande que la sopa de letras, cambiar la palabra
        while tamaño<longitud or tamaño<longitud:
            palabra=random.choice(palabras)
            longitud=len(palabra)
        #elegir si poner la palabra normal o del reves
        direccion=random.choice(["normal","reversa"])
        #caso palabra normal
        if direccion=="normal":
            #validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
            validar=False
            while validar==False:
                fila=random.randint(0,tamaño-longitud)
                columna=random.randint(0,tamaño-longitud)
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
                    while tamaño<longitud or tamaño<longitud:
                        palabra=random.choice(palabras)
                        longitud=len(palabra)
            #almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir
            palabras.remove(palabra)
            palabras_sopa.append(palabra)
            posiciones_palabras.append({"palabra":palabra,"inicio":(fila, columna),"final":(fila+longitud-1, columna+longitud-1)})
            #coloca la palabra
            for i in range(longitud):
                if modo=="2":
                    emoji=ord(palabra[i])-65
                    matriz[fila+i][columna+i]=modo_emoji[emoji]
                else:
                    matriz[fila+i][columna+i]=palabra[i]
        #caso palabra del reves
        else:
            #doy la vuelta a la palabra y uso la logica del codigo de la palabra normal
            palabra=palabra[::-1]
            #validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
            validar=False
            while validar==False:
                fila=random.randint(0,tamaño-longitud)
                columna=random.randint(0,tamaño-longitud)
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
                    while tamaño<longitud or tamaño<longitud:
                        palabra=random.choice(palabras)
                        longitud=len(palabra)
                    palabra=palabra[::-1]
            #almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir (todo ello dandole la vuelta otra vez ya que ya lo teniamos del reves)
            palabras.remove(palabra[::-1])
            palabras_sopa.append(palabra[::-1])
            posiciones_palabras.append({"palabra":palabra[::-1],"inicio":(fila+longitud-1, columna+longitud-1),"final":(fila, columna),})
            #coloca la palabra
            for i in range(longitud):
                if modo=="2":
                    emoji=ord(palabra[i])-65
                    matriz[fila+i][columna+i]=modo_emoji[emoji]
                else:
                    matriz[fila+i][columna+i]=palabra[i]

    #Caso colocar palabra en vertical
    elif horizontal_vertical_diagonal=="vertical":
        #si la palabra elegida es mas grande que la sopa de letras, cambiar la palabra
        while tamaño<longitud:
            palabra=random.choice(palabras)
            longitud=len(palabra)
        #elegir si poner la palabra normal o del reves
        direccion=random.choice(["normal","reversa"])
        #caso palabra normal
        if direccion=="normal":
            #validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
            validar=False
            while validar==False:
                fila=random.randint(0,tamaño-longitud)
                columna=random.randint(0,tamaño-1)
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
                    while tamaño<longitud:
                        palabra=random.choice(palabras)
                        longitud=len(palabra)
            #almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir
            palabras.remove(palabra)
            palabras_sopa.append(palabra)
            posiciones_palabras.append({"palabra":palabra,"inicio":(fila, columna),"final":(fila+longitud-1, columna),})
            #coloca la palabra
            for i in range(longitud):
                if modo=="2":
                    emoji=ord(palabra[i])-65
                    matriz[fila+i][columna]=modo_emoji[emoji]
                else:
                    matriz[fila+i][columna]=palabra[i]
        #caso palabra del reves
        else:
            #doy la vuelta a la palabra y uso la logica del codigo de la palabra normal
            palabra=palabra[::-1]
            #validar que la posicion elegida para la palabra es correcta (no interfiere con otras)
            validar=False
            while validar==False:
                fila=random.randint(0,tamaño-longitud)
                columna=random.randint(0,tamaño-1)
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
                    while tamaño<longitud:
                        palabra=random.choice(palabras)
                        longitud=len(palabra)
                    palabra=palabra[::-1]
            #almacena la palabra que a puesto en la sopa y se asegura que no vuelva a salir (todo ello dandole la vuelta otra vez ya que ya lo teniamos del reves)
            palabras.remove(palabra[::-1])
            palabras_sopa.append(palabra[::-1])
            posiciones_palabras.append({"palabra":palabra[::-1],"inicio":(fila+longitud-1, columna),"final":(fila, columna),})
            #coloca la palabra
            for i in range(longitud):
                if modo=="2":
                    emoji=ord(palabra[i])-65
                    matriz[fila+i][columna]=modo_emoji[emoji]
                else:
                    matriz[fila+i][columna]=palabra[i]

#la funcion rellena con letras mayusuculas al azar los elementos de la matriz que no tienen puesta palabras (es decir, que siguen siendo 0)
def rellenar_sopa(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==0:
                if modo=="2":
                    matriz[i][j]=random.choice(modo_emoji)
                else:
                    matriz[i][j]=chr(random.randint(65,90))

#función para localizar palabra en la sopa y saber si esta bien
def encontrar_palabra_en_sopa(palabras_sopa,posiciones_palabras,palabras_acertadas, tamaño, palabras_por_sopa):
    #el usuario elige la fila de la inicial de la palabra (y verifica que sea un número y en el rango posible)
    time.sleep(2)
    intento_fila_inicial=input("Introduce el número de la fila en la que se encuentra la inicial de la palabra: ")
    while intento_fila_inicial.isdigit()==False or int(intento_fila_inicial)>tamaño:
        time.sleep(0.5)
        intento_fila_inicial=input("No puede ser ni mas grande que el tamaño de la sopa ni un caracter, pruebe otra vez: ")
    intento_fila_inicial=int(intento_fila_inicial)        
    #el usuario elige la columna de la inicial de la palabra (y verifica que sea un número y en el rango posible)
    time.sleep(0.5)
    intento_columna_inicial=input("Introduce el número de la columna en la que se encuentra la inicial de la palabra: ")
    while intento_columna_inicial.isdigit()==False or int(intento_columna_inicial)>tamaño:
        time.sleep(0.5)
        intento_columna_inicial=input("No puede ser ni mas grande que el tamaño de la sopa ni un caracter, pruebe otra vez: ")
    intento_columna_inicial=int(intento_columna_inicial)
    #el usuario elige la fila de la última letra de la palabra (y verifica que sea un número y en el rango posible)
    time.sleep(0.5)
    intento_fila_final=input("Introduce el número de la fila en la que se encuentra la última letra de la palabra: ")
    while intento_fila_final.isdigit()==False or int(intento_fila_final)>tamaño:
        time.sleep(0.5)
        intento_fila_final=input("No puede ser ni mas grande que el tamaño de la sopa ni un caracter, pruebe otra vez: ")
    intento_fila_final=int(intento_fila_final)    
    #el usuario elige la columna de la última letra de la palabra (y verifica que sea un número y en el rango posible)
    time.sleep(0.5)
    intento_columna_final=input("Introduce el número de la columna en la que se encuentra la última letra de la palabra: ")
    while intento_columna_final.isdigit()==False or int(intento_columna_final)>tamaño:
        time.sleep(0.5)
        intento_columna_final=input("No puede ser ni mas grande que el tamaño de la sopa ni un caracter, pruebe otra vez: ")
    intento_columna_final=int(intento_columna_final)
    #como ya he verificado que es un número, pasamos el input a int
    intento_fila_inicial=int(intento_fila_inicial)    
    intento_columna_inicial=int(intento_columna_inicial)
    intento_fila_final=int(intento_fila_final)    
    intento_columna_final=int(intento_columna_final)    
    #restamos 1 a filas y columnas ya que python empeiza a contar desde 0
    intento_fila_inicial-=1
    intento_columna_inicial-=1
    intento_fila_final-=1
    intento_columna_final-=1
    #verifica si el usuario ha localizado bien la palabra o no (si ha acertado remueve la palabra de la lista palabras_sopa y la añade a la lista palabras_acertadas)
    for i in range(palabras_por_sopa):
        if posiciones_palabras[i]["inicio"]==(intento_fila_inicial, intento_columna_inicial) and posiciones_palabras[i]["final"]==(intento_fila_final, intento_columna_final):
            palabras_acertadas.append(posiciones_palabras[i]["palabra"])
            palabras_sopa.remove(posiciones_palabras[i]["palabra"])
            
#Función conjuntos de for y prints para imprimir la matriz con una sopa con eje x e y para que sea más facil para el usuario jugar
def imprimir_matriz(matriz,modo):
    if modo == "1":
        print("   ", end="")
        for j in range(len(matriz[0])):
            if j <= 8:
                print(f"\033[38;5;208m{j+1}\033[0m", end="   ")
            else:
                print(f"\033[38;5;208m{j+1}\033[0m", end="  ")
        print()
        print(" ",end =" -")
        print("----"*(len(matriz) - 1),end = "")
        print("-")
        for i in range(len(matriz)):
            if i <= 8:
                print(f"\033[38;5;208m{i+1}{" |"}\033[0m", end="")
            else:
                print(f"\033[38;5;208m{i+1}{"|"}\033[0m", end="")
            for j in range(len(matriz[0])):
                print(matriz[i][j], end="   ")
            print()
        print()
        print("Palabras en la sopa: ", end="")
    else:
        print("   ", end=" ")
        for j in range(len(matriz[0])):
            if j % 2 == 0 and j <= 8:
                print(f"\033[38;5;208m{j+1}\033[0m", end="    ")
            elif j % 2 != 0 and j > 8:
                print(f"\033[38;5;208m{j+1}\033[0m", end="    ")
            elif j % 2 == 0 and j > 8:
                print(f"\033[38;5;208m{j+1}\033[0m", end="    ")
            else:
                print(f"\033[38;5;208m{j+1}\033[0m", end="     ")
        print()
        print(" ",end =" -")
        print("-----"*(len(matriz)-1),end = "")
        x = 0.5 * (len(matriz)-1)
        print("-"*(int(x)),end = "")
        print("--")

        for i in range(len(matriz)):
            if i <= 8:
                print(f"\033[38;5;208m{i+1}{" |"}\033[0m", end="")
            else:
                print(f"\033[38;5;208m{i+1}{"|"}\033[0m", end="")
            for j in range(len(matriz[0])):
                print(matriz[i][j], end="    ")
            print()
        print()
        print("Palabras en la sopa: ", end="")

#Funciones del impostor

def seleccionar_impostor(n):
    #Esta funncion determina al impostor, siendo el n-ésimo jugador.
    impostor = random.randint(0, n-1)
    return impostor

#Funciones del ahorcado

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

#Pantalla principal
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
    os.system('cls')

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
print(f"{YELLOW}>> Elige una opción: {RESET}",end="")
opcion = input()

#SOPA DE LETRAS
if opcion == "1":
    #Lista de las palabras que pueden aparecer en la sopa
    palabras = ["ABEJA", "ABECEDA", "ACORDEON", "ADULTO", "ADOPCION", "AGUA", "AIRE", "ALBUM",
        "ALFOMBRA", "ALMUERZO", "ALMOHADA", "ALTO", "AMABILIDAD", "AMABLE", "AMIGO", "AMOR", "ANILLO", "ANIMAL",
        "APOYO", "ARENA", "ARBITRO", "ARMA", "ARTISTA", "ARTE", "AVENA", "AVION", "AZUCAR", "BAILARIN", "BANCO",
        "BARCO", "DUCHA", "BEBE", "BEBIDA", "BELLO", "BIBLIOTECA", "BOLA", "BONITO", "BOSQUE", "BOCA", "BRAZO",
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
        "MARCO", "MARIPOSA", "MARMOL", "MASCOTA", "MENSAJE", "MERCADO", "MES", "MESA", "MONTE", "MUNDO", "MUSICA",
        "NACION", "NIEVE", "NOCHE", "NOMBRE", "NOVELA", "NOVIEMBRE", "NUBE", "CHICO", "CHICA", "OBJETO", "OLA", "OJOS",
        "OSASUNA", "OSOS", "PALABRA", "PALACIO", "PALMERA", "PAPEL", "PAJARO", "PARAGUAS", "PARQUE", "PARRILLA",
        "PELOTA", "PELICULA", "PERIODICO", "PERRO", "PERSONA", "PLANTA", "PLANETA", "PLAZA", "PLATO", "POESIA", "PUEBLO",
        "PUENTE", "PUERTA", "PUERTO", "QUESO", "RAIZ", "RATON", "REINA", "RELOJ", "RECUERDO", "REGALO", "REUNION", "RIO",
        "ROPA", "RAPIDO", "SALA", "SALUD", "SALON", "SABOR", "SECRETO", "SEMILLA", "SENDERO", "SIESTA", "SOCIEDAD",
        "SOL", "SOLUCION", "SOMBRERO", "SOMBRILLA", "SONRISA", "TRANQUILO", "TIERRA", "TAZA", "TECHO",
        "TELEVISIÓN", "TIEMPO", "TUNEL", "TREN", "UNIVERSIDAD", "VACACIONES", "VACA", "VENTANA", "VALLE", "VENTILADOR",
        "VERSO", "VIDA", "VINO", "VIENTO", "YATE", "ZANAHORIA", "ZOOLOGICO", "ZUMO"]
    modo_emoji=[ "🐝", # A - Abeja 
                               "🛢️", # B - Barril 
                               "🐴", # C - Caballo 
                               "🐬", # D - Delfín 
                               "🐘", # E - Elefante 
                               "🌸", # F - Flor 
                               "🐈", # G - Jirafa 
                               "🦛", # H - Hipopotamo 
                               "🦎", # I - Iguana 
                               "🦒", # J - Jirafa 
                               "🐨", # K - Koala 
                               "🦁", # L - León 
                               "🐒", # M - Mono 
                               "🦦", # N - Nutria 
                               "🐑", # O - Oveja 
                               "🐼", # P - Panda 
                               "🧀", # Q - Queso 
                               "🐀", # R - Rata 
                               "🐍", # S - Serpiente 
                               "🐅", # T - Tigre 
                               "🦄", # U - Unicornio 
                               "🐄", # V - Vaca 
                               "🤽‍♂️", # W - Waterpolo 
                               "❌", # X - X 
                               "🪀", # Y - Yo yo 
                               "💤" # Z - zzz 
                              ]
    #bucle principal del programa  (el while para que pueda jugar las veces que quiera)         
    n="s"                    
    while n=="s" or n=="S":
        clear_output(wait=True) #limpia pantalla (funcional cuando quieres volver a jugar)
        #creo variables que tienen utilidad en funciones y en este while
        matriz=[]
        palabras_sopa=[]
        posiciones_palabras=[]
        palabras_acertadas=[]
        print("\033[1;32mBIENVENIDO A LA SOPA DE LETRAS!!! \033[0m")
        time.sleep(2)
        print("Esta versión de la sopa de letras tiene dos modos: ")
        time.sleep(2)
        #elige modo al que jugar normal o emoji
        print("1. Modo Normal")
        time.sleep(2)
        print("2. Modo Emoji")
        time.sleep(2)
        modo=input("Introduce 1 o 2 dependiendo del modo que quieras jugar: ")
        while modo!="1" and modo!="2":
            time.sleep(0.5)
            modo=input("Introduce unicamente 1 o 2 dependiendo del modo que quieras jugar: ")
        clear_output(wait=True)
        #elige el tamaño de la sopa, verifica que no sea menor que 4x4  
        if modo=="1":
            time.sleep(0.5)
            print("\033[1;32mHas elegido el modo normal, tienes que encontrar las palabras en la sopa de letras\033[0m")
            time.sleep(4)
        else:
            time.sleep(0.5)
            print("\033[1;33mHas elegido el modo emoji, cada emoji representa un objeto/animal cuya inicial es con la que debes crear la palabra a buscar\033[0m")
            time.sleep(4)
        tamaño=input("Por favor, introduce de que tamaño quieres la sopa de letras (Min 4): ")
        while tamaño.isdigit()==False or (int(tamaño)<4):
            time.sleep(0.5)
            tamaño=input("No puedes introducir otros caracteres o número menores a 4, prube otra vez: ")
        tamaño=int(tamaño)
        #pone un limite a el número de palabras que puede añadir para ese tamaño de sopa
        max_palabras_por_sopa=None
        if tamaño==4:
            max_palabras_por_sopa="2"
        else:
            max_palabras_por_sopa=tamaño-1
            max_palabras_por_sopa=str(max_palabras_por_sopa)
        #pide cuantas palabras quiere en la sopa con el maximo ya establecido y verifica que este dentro del rango y sea un número
        time.sleep(1)
        palabras_por_sopa=input(f"Introduce de cuantas palabras quieres que haya en la sopa (Max {max_palabras_por_sopa}): ")
        while palabras_por_sopa.isdigit()==False or palabras_por_sopa>max_palabras_por_sopa:
            time.sleep(0.5)
            palabras_por_sopa=input(f"No puedes introducir otros caracteres o número mayores a {max_palabras_por_sopa}, prube otra vez: ")
        palabras_por_sopa=int(palabras_por_sopa)
        inicializar_matriz(tamaño) #matriz de ceros
        #se añade tantas palabras a la sopa como haya puesto el usuario
        for i in range(palabras_por_sopa):
            elegir_colocar_palabra(matriz,palabras,tamaño)
        rellenar_sopa(matriz) #se rellena el resto de la sopa con letras al azar
        #variable que si inicializa con el valor de el número de palabras en la sopa, y que me servira para que si cambia el valor de len(palabras_sopa) significa que la funcion encontrar_palabra ha acertado la palabra 
        palabras_restantes=len(palabras_sopa)
        #el contador es unicamente para que en la primera ronda no imprima has acertado/has fallado/ y lo de palabras restantes...
        contador=0
        while len(palabras_sopa)>0:
            #si cambia el valor de len(palabras_sopa) significa que en la funcion encontrar_palabra el usuaario ha encontrado la palabra y borrado la palabra de la lista palabras_sopa
            if palabras_restantes!=len(palabras_sopa):
                time.sleep(0.5)
                print("\033[1;32mHAS ACERTADO LA PALABRA!!! SIGUE ASI!!! \033[0m") 
                time.sleep(2)
            #por lo contrario si no se ha borrado ninguna palabra, significa que el usuario ha fallado
            elif contador!=0:
                time.sleep(0.5)
                print("\033[1;31mHAS FALLADO, SIGUELO INTENTANDO!!! \033[0m") 
                time.sleep(2)
            palabras_restantes = len(palabras_sopa)
            print() #dejo un hueco
            time.sleep(1)
            imprimir_matriz(matriz, modo) #imprimimos la matriz ya con las palabras y letras al azar (y sus ejes)
            #bucle for para imprimir las palabras que hay que buscar en la sopa
            for i in range (len(palabras_sopa)):
                if i+1!=len(palabras_sopa):
                    print(palabras_sopa[i],end=", ")
                else:
                    print(palabras_sopa[i],end="")
            print() #dejo un hueco
            #ejecuto la funcion que permite al usuario encontrar palabra y verifica si la ha encontrado
            encontrar_palabra_en_sopa(palabras_sopa,posiciones_palabras,palabras_acertadas, tamaño, palabras_por_sopa)
            contador+=1
            clear_output(wait=True) #limpia pantalla en cada intento para que sea mas estetico
        #final del juego
        time.sleep(0.5)
        print("\033[1;32mHAS GANADO EL JUEGO!!! ENHORABUENA!!! \033[0m")
        time.sleep(2.5)
        print("Quieres seguir jugando (Introduce 's' si quieres seguir jugando y cualquier otra letra si no)?")
        n=input()
    
#IMPOSTOR
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

    #Texto inicial que explica el juego.
    os.system('cls')

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
    print("El jugador con más votos será expulsado.")
    time.sleep(2.5)
    print("Si hay empate, o todos los votos en blanco, no se expulsa a nadie.")
    time.sleep(3)
    print("El juego termina cuando no queden impostores, que habrá ganado el pueblo,")
    print("o cuando queden 2 o menos jugadores, que habrá ganado el impostor.")
    time.sleep(6)

    os.system('cls')

    #Asigna la palabra secreta en la variable "palabra".
    x = random.randint(0, len(palabras)-1)
    palabra = palabras[x]

    #Aquí se añaden los jugadores.
    n = int(input("Introduce el número de jugadores: "))
    os.system('cls')

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
        os.system('cls')
        print("Pase el dispositivo a {}".format(nombre))
        input("Presiona Enter para ver tu rol...")
    
        if nombre == impostor:
            print("Eres el \033[38;2;255;0;0mimpostor\033[0m.")
        else:
            print("Eres \033[38;2;0;255;0mpueblo\033[0m.")
            print("La palabra es: \033[1m{}\033[0m".format(palabra))
    
        input("Presiona Enter para ocultar tu rol...")
        os.system('cls')

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
        
            start_time = time.time()
            input_detected = False
            while time.time() - start_time < 1:
                if msvcrt.kbhit():
                    input()
                    input_detected = True
                    break
                    time.sleep(0.1)
                if input_detected:
                    break
                
            if input_detected:
                break
            segundos -= 1

        os.system('cls')
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
                    os.system('cls')
                

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
                        os.system('cls')
                        print("Pase el dispositivo a {}".format(nombre))
                        input("Presiona Enter para ver tu rol...")
    
                        if nombre == impostor:
                            print("Eres el \033[38;2;255;0;0mimpostor\033[0m.")
                        else:
                            print("Eres \033[38;2;0;255;0mpueblo\033[0m.")
                            print("La palabra es: \033[1m{}\033[0m".format(palabra))
    
                        input("Presiona Enter para ocultar tu rol...")
                        os.system('cls')

#AHORCADO
elif opcion == "3":  
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
