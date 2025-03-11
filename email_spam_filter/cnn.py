import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv1D, MaxPooling1D, Flatten
import cProfile
import pstats
from concurrent.futures import ProcessPoolExecutor
import json
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ConfigReloader(FileSystemEventHandler):
    def __init__(self, config_path, callback):
        self.config_path = config_path
        self.callback = callback

    def on_modified(self, event):
        if event.src_path == self.config_path:
            print(f"Configuration file {self.config_path} has been modified.")
            with open(self.config_path, 'r') as f:
                new_config = json.load(f)
            self.callback(new_config)

def load_config(config_path='config.json'):
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Configuration file not found. Using default settings.")
        return {}

class ConfigWatcher(threading.Thread):
    def __init__(self, config_path, callback):
        super().__init__()
        self.config_path = config_path
        self.callback = callback
        self.observer = Observer()

    def run(self):
        event_handler = ConfigReloader(self.config_path, self.callback)
        self.observer.schedule(event_handler, path=self.config_path, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

def build_cnn_model(input_shape):
    """
    Build a simple Convolutional Neural Network (CNN) model for spam detection.
    
    Args:
        input_shape: Tuple specifying the shape of the input data.

    Returns:
        A compiled CNN model ready for training or inference.
    """
    config = load_config()
    learning_rate = config.get('learning_rate', 0.001)

    model = Sequential()
    # 1D Convolutional layer
    model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=input_shape))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    # Dense layers
    model.add(Dense(50, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))  # Output layer for binary classification

    # Compile the model with binary crossentropy loss and an appropriate optimizer
    model.compile(optimizer=f'adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    return model

def train_cnn_model(model, X_train, y_train, epochs=10, batch_size=32):
    """
    Train the CNN model on the provided data.

    Args:
        model: The compiled CNN model.
        X_train: Training features.
        y_train: Training labels.
        epochs: Number of epochs for training.
        batch_size: Batch size during training.
    
    Returns:
        History object containing training history information.
    """
    profiler = cProfile.Profile()
    profiler.enable()

    # Train the model
    history = model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)

    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats(10)  # Print top 10 time-consuming functions

    return history

def predict_spam(model, X_test):
    """
    Predict spam using the trained CNN model.

    Args:
        model: The trained CNN model.
        X_test: Test features to make predictions on.
    
    Returns:
        Array of predicted probabilities indicating spam likelihood.
    """
    # Profile this function for performance bottlenecks
    profiler = cProfile.Profile()
    profiler.enable()

    # Use ProcessPoolExecutor for parallel processing if applicable
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(model.predict, np.array_split(X_test, os.cpu_count())))

    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats(10)  # Print top 10 time-consuming functions

    return np.concatenate(results)

def on_config_change(new_config):
    print("Configuration updated:", new_config)
    # Add logic here to update any dependent components or settings
    # For example, re-compiling the model with a new learning rate if needed

if __name__ == "__main__":
    config_watcher = ConfigWatcher('config.json', on_config_change)
    config_watcher.start()