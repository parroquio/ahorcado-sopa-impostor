import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import os

# Palabras del juego (copiadas del original)
PALABRAS = [
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
    "pasillo", "vestíbulo", "recepción", "Mendívil", "taquilla", "mostrador", "caja", "entrada", "salida", "meta", "poste",
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

class ImpostorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Juego del Impostor")
        self.geometry("600x500")
        self.configure(bg="#2c3e50")
        
        # Estilos
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#2c3e50')
        self.style.configure('TLabel', background='#2c3e50', foreground='white', font=('Helvetica', 14))
        self.style.configure('Header.TLabel', font=('Helvetica', 24, 'bold'))
        self.style.configure('TButton', font=('Helvetica', 12), padding=10, background='#3498db', foreground='white')
        self.style.map('TButton', background=[('active', '#2980b9')])
        
        # Estado del juego
        self.jugadores_originales = []
        self.jugadores = []
        self.palabra = ""
        self.impostor = ""
        self.current_player_index = 0
        
        self.show_start_screen()

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_start_screen(self):
        self.clear_window()
        frame = ttk.Frame(self)
        frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        ttk.Label(frame, text="Bienvenido al", style='Header.TLabel').pack(pady=10)
        ttk.Label(frame, text="JUEGO DEL IMPOSTOR", style='Header.TLabel', foreground='#e74c3c').pack(pady=10)
        
        ttk.Label(frame, text="Un jugador será el impostor.\nEl resto, el pueblo.\n¡Descúbrelo antes de que sea tarde!", justify='center').pack(pady=30)
        
        ttk.Button(frame, text="Comenzar", command=self.show_setup_screen).pack(pady=20)

    def show_setup_screen(self):
        self.clear_window()
        frame = ttk.Frame(self)
        frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        ttk.Label(frame, text="Configuración", style='Header.TLabel').pack(pady=20)
        
        ttk.Label(frame, text="Introduce los nombres de los jugadores:").pack(pady=10)
        
        self.entries_frame = ttk.Frame(frame)
        self.entries_frame.pack(fill='both', expand=True)
        
        self.player_entries = []
        self.add_player_entry()
        self.add_player_entry()
        self.add_player_entry() # Empezar con 3 campos
        
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=20)
        
        ttk.Button(btn_frame, text="+ Jugador", command=self.add_player_entry).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Jugar", command=self.start_game).pack(side='left', padx=5)

    def add_player_entry(self):
        entry = ttk.Entry(self.entries_frame, font=('Helvetica', 12))
        entry.pack(pady=5, fill='x', padx=50)
        self.player_entries.append(entry)

    def start_game(self):
        names = [e.get().strip() for e in self.player_entries if e.get().strip()]
        if len(names) < 3:
            messagebox.showerror("Error", "Se necesitan al menos 3 jugadores.")
            return
        
        self.jugadores_originales = names.copy()
        self.start_round(new_game=True)

    def start_round(self, new_game=False):
        if new_game:
            self.jugadores = self.jugadores_originales.copy()
            self.palabra = random.choice(PALABRAS)
            self.impostor = random.choice(self.jugadores)
            self.current_player_index = 0
            self.show_pass_device_screen()
        else:
            self.show_timer_screen()

    def show_pass_device_screen(self):
        if self.current_player_index >= len(self.jugadores):
            self.show_timer_screen()
            return

        self.clear_window()
        frame = ttk.Frame(self)
        frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        player_name = self.jugadores[self.current_player_index]
        
        ttk.Label(frame, text="Pase el dispositivo a:", style='Header.TLabel').pack(pady=30)
        ttk.Label(frame, text=player_name, font=('Helvetica', 32, 'bold'), foreground='#f1c40f').pack(pady=20)
        
        ttk.Button(frame, text="Ver mi rol", command=lambda: self.show_role_screen(player_name)).pack(pady=40)

    def show_role_screen(self, player_name):
        self.clear_window()
        frame = ttk.Frame(self)
        frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        ttk.Label(frame, text=f"Hola {player_name}", style='Header.TLabel').pack(pady=20)
        
        if player_name == self.impostor:
            ttk.Label(frame, text="Eres el", font=('Helvetica', 18)).pack(pady=10)
            ttk.Label(frame, text="IMPOSTOR", font=('Helvetica', 36, 'bold'), foreground='#e74c3c').pack(pady=10)
            ttk.Label(frame, text="¡Engaña a todos!", font=('Helvetica', 14)).pack(pady=10)
        else:
            ttk.Label(frame, text="Eres", font=('Helvetica', 18)).pack(pady=10)
            ttk.Label(frame, text="PUEBLO", font=('Helvetica', 36, 'bold'), foreground='#2ecc71').pack(pady=10)
            ttk.Label(frame, text="La palabra secreta es:", font=('Helvetica', 14)).pack(pady=20)
            ttk.Label(frame, text=self.palabra, font=('Helvetica', 28, 'bold', 'underline'), foreground='white').pack(pady=10)
            
        ttk.Button(frame, text="Ocultar y Siguiente", command=self.next_player).pack(pady=40)

    def next_player(self):
        self.current_player_index += 1
        self.show_pass_device_screen()

    def show_timer_screen(self):
        self.clear_window()
        frame = ttk.Frame(self)
        frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        ttk.Label(frame, text="¡A JUGAR!", style='Header.TLabel').pack(pady=20)
        ttk.Label(frame, text="Debatid y encontrad al impostor.", justify='center').pack(pady=10)
        
        self.time_left = len(self.jugadores) * 60
        self.timer_label = ttk.Label(frame, text=self.format_time(self.time_left), font=('Helvetica', 48, 'bold'))
        self.timer_label.pack(pady=30)
        
        self.timer_running = True
        self.update_timer()
        
        ttk.Button(frame, text="Terminar y Votar", command=self.stop_timer_and_vote).pack(pady=20)

    def format_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        return '{:02d}:{:02d}'.format(mins, secs)

    def update_timer(self):
        if self.timer_running and self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=self.format_time(self.time_left))
            self.after(1000, self.update_timer)
        elif self.time_left == 0:
            self.stop_timer_and_vote()

    def stop_timer_and_vote(self):
        self.timer_running = False
        self.show_voting_screen()

    def show_voting_screen(self):
        self.clear_window()
        frame = ttk.Frame(self)
        frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        ttk.Label(frame, text="VOTACIÓN", style='Header.TLabel').pack(pady=20)
        ttk.Label(frame, text="¿Quién es el impostor?").pack(pady=10)
        
        for player in self.jugadores:
            ttk.Button(frame, text=player, command=lambda p=player: self.process_vote(p)).pack(pady=5, fill='x', padx=50)
            
        ttk.Button(frame, text="Empate / Blanco", command=lambda: self.process_vote(None)).pack(pady=20, fill='x', padx=50)

    def process_vote(self, voted_player):
        self.clear_window()
        frame = ttk.Frame(self)
        frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        if voted_player is None:
            ttk.Label(frame, text="Empate", style='Header.TLabel').pack(pady=20)
            ttk.Label(frame, text="Nadie ha sido expulsado.").pack(pady=10)
            self.check_game_over(frame, None)
        else:
            ttk.Label(frame, text=f"Se ha votado a {voted_player}", style='Header.TLabel').pack(pady=20)
            
            if voted_player == self.impostor:
                ttk.Label(frame, text="¡ERA EL IMPOSTOR!", font=('Helvetica', 24, 'bold'), foreground='#2ecc71').pack(pady=20)
                ttk.Label(frame, text="¡El Pueblo Gana!", font=('Helvetica', 18)).pack(pady=10)
                self.show_game_over_buttons(frame)
            else:
                ttk.Label(frame, text="Era INOCENTE", font=('Helvetica', 24, 'bold'), foreground='#e74c3c').pack(pady=20)
                self.jugadores.remove(voted_player)
                self.check_game_over(frame, voted_player)

    def check_game_over(self, frame, voted_player):
        # Verificar si quedan impostores (si llegamos aquí y se votó a alguien, NO era el impostor)
        # El impostor sigue vivo.
        
        if len(self.jugadores) <= 2:
            ttk.Label(frame, text="Solo quedan 2 jugadores.", font=('Helvetica', 18)).pack(pady=10)
            ttk.Label(frame, text="¡El Impostor Gana!", font=('Helvetica', 24, 'bold'), foreground='#e74c3c').pack(pady=10)
            ttk.Label(frame, text=f"El impostor era: {self.impostor}", font=('Helvetica', 14)).pack(pady=10)
            self.show_game_over_buttons(frame)
        else:
            ttk.Button(frame, text="Siguiente Ronda", command=lambda: self.start_round(new_game=False)).pack(pady=30)

    def show_game_over_buttons(self, frame):
        ttk.Button(frame, text="Jugar otra vez (Mismos jugadores)", command=lambda: self.start_round(new_game=True)).pack(pady=10, fill='x', padx=50)
        ttk.Button(frame, text="Nueva Partida (Nuevos jugadores)", command=self.show_setup_screen).pack(pady=10, fill='x', padx=50)
        ttk.Button(frame, text="Salir", command=self.quit).pack(pady=10, fill='x', padx=50)

if __name__ == "__main__":
    app = ImpostorApp()
    app.mainloop()
