import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv1D, MaxPooling1D, Flatten

def build_cnn_model(input_shape):
    """
    Build a simple Convolutional Neural Network (CNN) model for spam detection.
    
    Args:
        input_shape: Tuple specifying the shape of the input data.

    Returns:
        A compiled CNN model ready for training or inference.
    """
    model = Sequential()
    # 1D Convolutional layer
    model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=input_shape))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    # Dense layers
    model.add(Dense(50, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))  # Output layer for binary classification

    # Compile the model with binary crossentropy loss and an appropriate optimizer
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
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
    return model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)

def predict_spam(model, X_test):
    """
    Predict spam using the trained CNN model.

    Args:
        model: The trained CNN model.
        X_test: Test features to make predictions on.
    
    Returns:
        Array of predicted probabilities indicating spam likelihood.
    """
    return model.predict(X_test)