
# Importing necessary modules
import tkinter as tk

class TranscriptionHistory:
    def __init__(self, history_frame):
        # Creating the history frame
        self.history_frame = tk.Frame(history_frame, bg='white')
        self.history_frame.pack(fill=tk.BOTH, expand=True)

        # Creating the history label
        self.history_label = tk.Label(self.history_frame, text="Historial de Transcripciones:", bg='white', font=("Arial", 14))
        self.history_label.pack(side=tk.TOP, anchor='nw')

        # Creating the history text box
        self.history_text = tk.Text(self.history_frame, height=4, bg='white', font=("Arial", 12))
        self.history_text.pack(fill=tk.BOTH, expand=True)

    def update_history(self, transcription):
        # Updating the history text box
        self.history_text.insert(tk.END, transcription + '\n')

