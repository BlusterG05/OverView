# trainmodel.py
from chargedata import load_dataset
from buildmodel import build_model
import tensorflow as tf

def train_model(train_dir, val_dir, num_classes, epochs=10, batch_size=32):
    # Cargar datos de entrenamiento y validación
    train_generator = load_dataset(train_dir, batch_size=batch_size)
    validation_generator = load_dataset(val_dir, batch_size=batch_size)

    # Construir el modelo
    model = build_model(num_classes)

    # Entrenar el modelo
    history = model.fit(
        train_generator,
        epochs=epochs,
        validation_data=validation_generator,
        steps_per_epoch=train_generator.samples // batch_size,
        validation_steps=validation_generator.samples // batch_size
    )

    return model, history

# Función para evaluar el modelo
def evaluate_model(model, test_dir, batch_size=32):
    test_generator = load_dataset(test_dir, batch_size=batch_size)
    evaluation = model.evaluate(test_generator)
    return evaluation