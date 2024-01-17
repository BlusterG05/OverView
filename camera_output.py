import tkinter as tk
from tkinter import Label
import cv2
from PIL import Image, ImageTk
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import mediapipe as mp


MODEL_PATH = 'overviewmodel/modelos/overview_model.h5'

class CameraOutput:
    def __init__(self, camera_frame, model_path, output_widget, transcription_output, transcription_history):
        self.camera_frame = camera_frame
        self.model = load_model(model_path)
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=False,
                                         max_num_hands=1,
                                         min_detection_confidence=0.5)
        self.camera_label = Label(camera_frame)
        self.camera_label.pack()
        self.cap = cv2.VideoCapture(0)
        self.output_widget = output_widget
        self.transcription_output = transcription_output
        self.transcription_history = transcription_history
        self.class_mapping = ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'T', 'U', 'V', 'W', 'Y']
        
        self.update_camera_output()

    def update_camera_output(self):
        ret, frame = self.cap.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(frame_rgb)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
            
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)
            self.camera_label.imgtk = imgtk
            self.camera_label.configure(image=imgtk)
            self.predict_letter(frame_rgb)
        self.camera_label.after(10, self.update_camera_output)

    def predict_letter(self, frame):
        img = cv2.resize(frame, (300, 300)) 
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0
        prediction = self.model.predict(img_array)
        predicted_class_index = np.argmax(prediction, axis=1)[0]
        self.display_prediction(predicted_class_index)

    def display_prediction(self, predicted_class_index):
        predicted_letter = self.class_mapping[predicted_class_index]
        self.transcription_output.update_transcription(predicted_letter)
        self.transcription_history.add_to_history(predicted_letter)

    def close(self):
        self.cap.release()
        self.hands.close()
        self.camera_frame.destroy()

