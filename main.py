# Importing necessary modules
import tkinter as tk
from camera_output import CameraOutput
from interface import Interface
from menu import Menu
from transcription_output import TranscriptionOutput
from transcription_history import TranscriptionHistory

# Creating the main window
root = tk.Tk()
root.title("Over View")

# Creating the interface
interface = Interface(root)

# Ruta al archivo del modelo
model_path = 'overviewmodel/modelos/overview_model.h5'

# Widget de salida para mostrar las predicciones (cambiar según corresponda)
output_widget = interface.transcription_output_label  # Asegúrate de que este sea el nombre correcto

# Creating the camera output with model and output widget
camera_output = CameraOutput(interface.camera_frame, model_path, output_widget)


# Creating the menu
menu = Menu(interface.menu_frame)

# Creating the transcription output
transcription_output = TranscriptionOutput(interface.transcription_frame)

# Creating the transcription history
transcription_history = TranscriptionHistory(interface.history_frame)

# Running the main loop
root.mainloop()

