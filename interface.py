

# Importing necessary modules
import tkinter as tk

class Interface:
    def __init__(self, root):
        # Creating the main frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Creating the camera frame
        self.camera_frame = tk.Frame(self.main_frame, width=500, height=500, bg='black')
        self.camera_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Creating the right frame
        self.right_frame = tk.Frame(self.main_frame, width=200, bg='grey')
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

        # Creating the menu frame
        self.menu_frame = tk.Frame(self.right_frame, width=200, height=300, bg='white')
        self.menu_frame.pack(side=tk.TOP, fill=tk.X)

        # Creating the history frame
        self.history_frame = tk.Frame(self.right_frame, width=200, height=200, bg='white')
        self.history_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Creating the transcription frame
        self.transcription_frame = tk.Frame(root, width=700, height=100, bg='white')
        self.transcription_frame.pack(side=tk.BOTTOM, fill=tk.X)

