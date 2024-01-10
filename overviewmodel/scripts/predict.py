from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

def load_and_prepare_image(image_path, target_size=(300, 300)):
    img = image.load_img(image_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Cambiar la forma para el modelo
    img_array /= 255.0  # Normalizar

    return img_array

def predict(model, image_path):
    img_array = load_and_prepare_image(image_path)
    predictions = model.predict(img_array)
    return predictions

# Ejemplo de uso
model = load_model('../modelos/overview_model.h5')  
pred = predict(model, '../data/test/A_test.jpg') 