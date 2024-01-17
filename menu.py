# Importing necessary modules
import tkinter as tk

class Menu:
    def __init__(self, parent):
       
        self.menu_frame = tk.Frame(parent, width=200, height=300, bg='white')
        self.menu_frame.pack(side=tk.TOP, fill=tk.X)

        
        self.menu = tk.Menu(self.menu_frame, tearoff=0)
        self.menu.add_command(label="Función 1", command=self.function1)
        self.menu.add_command(label="Función 2", command=self.function2)
        self.menu.add_command(label="Función 3", command=self.function3)

        self.menu_frame.bind("<Button-3>", self.show_menu)

    def show_menu(self, event):
        # Displaying the menu
        self.menu.post(event.x_root, event.y_root)

    def function1(self):
       
        pass

    def function2(self):
        
        pass

    def function3(self):
        
        pass