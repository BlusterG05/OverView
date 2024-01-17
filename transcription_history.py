import tkinter as tk

class TranscriptionHistory:
    def __init__(self, history_frame):
        # apartado historial
        self.history_frame = tk.Frame(history_frame, bg='white')
        self.history_frame.pack(fill=tk.BOTH, expand=True)

        # label
        self.history_label = tk.Label(self.history_frame, text="Historial de Transcripciones:", bg='white', font=("Arial", 14))
        self.history_label.pack(side=tk.TOP, anchor='nw')

        # apartado para el texto del historial
        self.history_text = tk.Text(self.history_frame, height=4, bg='white', font=("Arial", 12))
        self.history_text.pack(fill=tk.BOTH, expand=True)
    
    def add_to_history(self, letter):
        print("Añadiendo al historial:", letter)  
        def update_history():
            self.history_text.insert(tk.END, letter + "\n")
            self.history_text.see(tk.END)
        self.history_frame.after(0, update_history)