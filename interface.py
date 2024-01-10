import tkinter as tk

class Interface:
    def __init__(self, root):
        # Crear el marco principal
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Crear el marco de la cámara
        self.camera_frame = tk.Frame(self.main_frame, width=500, height=500, bg='black')
        self.camera_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Crear el marco derecho
        self.right_frame = tk.Frame(self.main_frame, width=200, bg='grey')
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

        # Crear el marco del menú
        self.menu_frame = tk.Frame(self.right_frame, width=200, height=300, bg='white')
        self.menu_frame.pack(side=tk.TOP, fill=tk.X)

        # Crear el marco del historial
        self.history_frame = tk.Frame(self.right_frame, width=200, height=200, bg='white')
        self.history_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Crear el marco de transcripción
        self.transcription_frame = tk.Frame(root, width=700, height=100, bg='white')
        self.transcription_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Crear el widget de etiqueta para mostrar las transcripciones
        self.transcription_output_label = tk.Label(self.transcription_frame, text="Transcription Output", bg="white")
        self.transcription_output_label.pack(fill=tk.BOTH, expand=True)