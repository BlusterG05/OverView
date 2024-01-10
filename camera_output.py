from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import cv2
from PIL import Image, ImageTk
import numpy as np
from tkinter import Label

class CameraOutput:
    def __init__(self, window, model_path, output_widget):
        # Mapeo de índices a letras
        self.class_mapping = ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y']

        self.window = window
        self.output_widget = output_widget
        self.model = load_model(model_path)

        self.camera_label = Label(window)
        self.camera_label.pack()

        self.cap = cv2.VideoCapture(0)

        self.update_camera_output()

    def update_camera_output(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.camera_label.imgtk = imgtk
            self.camera_label.configure(image=imgtk)
            
            # Predecir letra
            self.predict_letter(frame)

            self.camera_label.after(10, self.update_camera_output)

    def predict_letter(self, frame):
        # Redimensionar y preprocesar la imagen para el modelo
        img = cv2.resize(frame, (300, 300))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0

        # Hacer la predicción
        prediction = self.model.predict(img_array)
        predicted_class = np.argmax(prediction, axis=1)

        # Actualizar el widget de salida con la letra predicha
        predicted_letter = self.class_mapping[predicted_class[0]]
        self.output_widget.config(text=predicted_letter)