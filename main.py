import tkinter as tk
from camera_output import CameraOutput
from interface import Interface
from transcription_output import TranscriptionOutput
from transcription_history import TranscriptionHistory

root = tk.Tk()
root.title("Software de Lenguaje de Señas")
# Interfaz
interface = Interface(root)
# Ruta al archivo del modelo
model_path = 'overviewmodel/modelos/overview_model.h5'
# Instancias de TranscriptionOutput y TranscriptionHistory
transcription_output = TranscriptionOutput(interface.transcription_frame)

transcription_history = TranscriptionHistory(interface.history_frame)

# Widget de salida para mostrar las predicciones
output_widget = interface.transcription_output_label  
app = CameraOutput(interface.camera_frame, model_path, output_widget, transcription_output, transcription_history)

root.mainloop()