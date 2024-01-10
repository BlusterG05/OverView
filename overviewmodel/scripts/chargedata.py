from tensorflow.keras.preprocessing.image import ImageDataGenerator

def load_dataset(directory, target_size=(1000, 1000), batch_size=32, class_mode='categorical'):
    datagen = ImageDataGenerator(rescale=1./255)

    generator = datagen.flow_from_directory(
        directory,
        target_size=target_size,
        batch_size=batch_size,
        class_mode=class_mode
    )

    return generator
