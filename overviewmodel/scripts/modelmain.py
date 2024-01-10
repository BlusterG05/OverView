from chargedata import load_dataset
from buildmodel import build_model
from trainmodel import train_model, evaluate_model
import os

def main():
    # Configuración de los parámetros del modelo y las rutas de los datos
    num_classes = 20
    epochs = 10
    batch_size = 32
    # Asumiendo que este script se ejecuta desde /overviewmodel/scripts/
    train_dir = "../data/train"
    val_dir = "../data/validation"
    test_dir = "../data/test"

    # Cargar y preparar los datos de entrenamiento y validación
    print("Cargando datos de entrenamiento y validación...")
    train_generator = load_dataset(train_dir, batch_size=batch_size)
    validation_generator = load_dataset(val_dir, batch_size=batch_size)

    # Construir y entrenar el modelo
    print("Construyendo y entrenando el modelo...")
    model = build_model(num_classes)
    model, history = train_model(train_dir, val_dir, num_classes, epochs, batch_size)

    # Evaluar el modelo
    print("Evaluando el modelo...")
    evaluation = evaluate_model(model, test_dir, batch_size)
    print(f"Test Loss: {evaluation[0]}, Test Accuracy: {evaluation[1]}")

    # Guardar el modelo
    model_save_path = "../modelos/overview_model.h5"
    model.save(model_save_path)
    print(f"Modelo guardado en {model_save_path}")

if __name__ == "__main__":
    main()
