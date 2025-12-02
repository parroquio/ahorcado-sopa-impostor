import random

def impostor(n):
    impostor = random.randint(1,n)
    return impostor


def palabra_pueblo(x):
        
# Lista de palabras para el juego del impostor (Objetos y conceptos populares y ambiguos)
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
    "pasillo", "vestíbulo", "recepción", "taquilla", "mostrador", "caja", "entrada", "salida", "meta", "poste",
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
    palabra = palabras[x]

    return palabra

