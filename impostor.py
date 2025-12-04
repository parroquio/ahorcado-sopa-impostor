# REVISAR TEMPORIZADOR


import random
import os
import time
import sys
import select
import msvcrt

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
print("El jugador con más votos será el impostor.")
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

