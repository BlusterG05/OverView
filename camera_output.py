
# Importing necessary modules
import cv2
from tkinter import *
from PIL import Image, ImageTk

class CameraOutput:
    def __init__(self, window):
        # Creating a label to hold the camera output
        self.camera_label = Label(window)
        self.camera_label.pack()

        # Capturing video from the webcam
        self.cap = cv2.VideoCapture(0)

        # Updating the label with new frames from the webcam
        self.update_camera_output()

    def update_camera_output(self):
        # Getting a frame from the webcam
        ret, frame = self.cap.read()

        if ret:
            # Converting the image from BGR color space to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Converting the image into a PIL format
            image = Image.fromarray(frame)

            # Converting the image into a format that tkinter can use
            photo = ImageTk.PhotoImage(image)

            # Updating the label with the new image
            self.camera_label.config(image=photo)
            self.camera_label.image = photo

        # Calling this function again in 15 milliseconds
        self.camera_label.after(15, self.update_camera_output)

