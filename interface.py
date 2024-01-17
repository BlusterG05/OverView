import tkinter as tk

class Interface:
    def __init__(self, root):
        root.geometry("600x600")
        root.resizable(False, False)

        # Marco principal
        self.main_frame = tk.Frame(root, bg="light grey")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

       
        self.camera_frame = tk.Frame(self.main_frame, bg="black", highlightbackground="light grey", highlightthickness=5)
        self.camera_frame.pack(pady=5)

  
        self.transcription_frame = tk.Frame(self.main_frame, bg="white")
        self.transcription_frame.pack(pady=10, padx=10, fill=tk.X)

        self.history_frame = tk.Frame(self.main_frame, bg="white")
        self.history_frame.pack(pady=10, padx=10, fill=tk.X)

      
        self.right_frame = tk.Frame(self.main_frame, bg="light grey")
        self.right_frame.pack(pady=10, fill=tk.BOTH, expand=True)

   
        self.transcription_output_label = tk.Label(self.transcription_frame, text="Transcription Output", bg="white")
        self.transcription_output_label.pack(fill=tk.BOTH, expand=True)