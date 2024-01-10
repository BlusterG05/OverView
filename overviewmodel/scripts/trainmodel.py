from chargedata import load_dataset
from buildmodel import build_model

def train_model(train_dir, val_dir, num_classes, epochs, batch_size):
    train_generator = load_dataset(train_dir, batch_size=batch_size)
    validation_generator = load_dataset(val_dir, batch_size=batch_size)

    model = build_model(num_classes)
    history = model.fit(
        train_generator,
        epochs=epochs,
        validation_data=validation_generator,
        steps_per_epoch=train_generator.samples // batch_size,
        validation_steps=validation_generator.samples // batch_size
    )

    return model, history

def evaluate_model(model, test_dir, batch_size):
    test_generator = load_dataset(test_dir, batch_size=batch_size)
    return model.evaluate(test_generator)
