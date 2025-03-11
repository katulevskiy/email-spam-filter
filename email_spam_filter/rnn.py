import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, SimpleRNN, Dense

class RnnSpamDetector:
    def __init__(self, vocab_size, embedding_dim=50, rnn_units=64):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.rnn_units = rnn_units
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential()
        model.add(Embedding(input_dim=self.vocab_size, output_dim=self.embedding_dim))
        model.add(SimpleRNN(units=self.rnn_units))
        model.add(Dense(1, activation='sigmoid'))
        
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def train(self, X_train, y_train, epochs=5):
        self.model.fit(X_train, y_train, epochs=epochs)

    def predict(self, X_test):
        predictions = self.model.predict(X_test)
        return (predictions > 0.5).astype(int)

def preprocess_email(email_content, vocab_dict, max_length):
    tokenized_email = [vocab_dict.get(word, 1) for word in email_content.lower().split()]
    padded_email = np.pad(tokenized_email, 
                          (0, max(0, max_length - len(tokenized_email))), 
                          'constant', constant_values=0)
    
    return padded_email[:max_length]

# Example usage:
# vocab_dict and max_length need to be defined based on the dataset used for training.

This code provides a basic implementation of an RNN-based spam detector using Keras. The `RnnSpamDetector` class encapsulates the model building, training, and prediction processes. 

- **Initialization**: The constructor initializes necessary parameters like vocabulary size, embedding dimensions, and units in the RNN layer.
  
- **Model Building**: A simple sequential model is created with an Embedding layer followed by a SimpleRNN layer and a Dense output layer with sigmoid activation for binary classification.

- **Training**: The `train` method allows fitting the model to training data.

- **Prediction**: The `predict` method returns binary predictions based on a threshold of 0.5.

- **Preprocessing**: A utility function `preprocess_email` tokenizes and pads email content, converting it into a numerical format suitable for input to the RNN model.

This setup assumes you have already prepared your dataset with necessary preprocessing steps like building a vocabulary dictionary (`vocab_dict`) and defining `max_length`, which should be the length of the longest sequence in your training data. Adjust these aspects based on your specific use case and dataset.