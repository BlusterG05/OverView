import tkinter as tk

class TranscriptionOutput:
    def __init__(self, transcription_frame):
        # apartado historial
        self.transcription_output_frame = tk.Frame(transcription_frame, bg='white')
        self.transcription_output_frame.pack(fill=tk.BOTH, expand=True)

        # label
        self.transcription_output_label = tk.Label(self.transcription_output_frame, text="Transcripción:", bg='white', font=("Arial", 14))
        self.transcription_output_label.pack(side=tk.TOP, anchor='nw')

        # apartado para el texto de la transcripción
        self.transcription_output_text = tk.Text(self.transcription_output_frame, height=4, bg='white', font=("Arial", 12))
        self.transcription_output_text.pack(fill=tk.BOTH, expand=True)
        
    def update_transcription(self, letter):

        self.transcription_output_text.delete("1.0", tk.END)
        self.transcription_output_text.insert(tk.END, letter)