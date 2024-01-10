
# Importing necessary modules
import tkinter as tk
from camera_output import CameraOutput
from interface import Interface
from menu import Menu
from transcription_output import TranscriptionOutput
from transcription_history import TranscriptionHistory

# Creating the main window
root = tk.Tk()
root.title("Software de Lenguaje de Señas")

# Creating the interface
interface = Interface(root)

# Creating the camera output
camera_output = CameraOutput(interface.camera_frame)

# Creating the menu
menu = Menu(interface.menu_frame)

# Creating the transcription output
transcription_output = TranscriptionOutput(interface.transcription_frame)

# Creating the transcription history
transcription_history = TranscriptionHistory(interface.history_frame)

# Running the main loop
root.mainloop()

