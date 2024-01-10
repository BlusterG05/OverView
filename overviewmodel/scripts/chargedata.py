from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

def load_dataset(directory, target_size=(1000, 1000), batch_size=32):
    # Verificar si el directorio existe
    if not os.path.exists(directory):
        raise ValueError(f"El directorio proporcionado no existe: {directory}")

    datagen = ImageDataGenerator(rescale=1./255)

    generator = datagen.flow_from_directory(
        directory,
        target_size=target_size,
        batch_size=batch_size,
        class_mode='categorical'  # O 'binary' si solo tienes dos clases
    )
    return generator
