"""
Examples of Using the Email Spam Filter with RNN

This script demonstrates how to use the email spam filter with a Recurrent Neural Network (RNN) model for detecting spam emails.

Before running this example, ensure you have installed necessary libraries:
- Python 3.x
- numpy
- tensorflow or keras
- scikit-learn

You can install these dependencies using pip:
pip install numpy tensorflow scikit-learn

1. Data Preparation
First, prepare your dataset. This example assumes you have a CSV file with labeled email data ('spam.csv').

2. Load and Preprocess Data
"""
import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('spam.csv', encoding='latin-1')
data = data[['v1', 'v2']]
data.columns = ['label', 'email']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data['email'], data['label'], test_size=0.2)

"""
3. Text Preprocessing
Convert the email texts to sequences that can be fed into an RNN model.
"""
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Tokenize text
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(X_train)
X_train_seq = tokenizer.texts_to_sequences(X_train)
X_test_seq = tokenizer.texts_to_sequences(X_test)

# Pad sequences to ensure uniform input length
max_len = 200
X_train_pad = pad_sequences(X_train_seq, maxlen=max_len)
X_test_pad = pad_sequences(X_test_seq, maxlen=max_len)

"""
4. Model Building
Build a simple RNN model using Keras.
"""
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

# Define the RNN model
model = Sequential()
model.add(Embedding(input_dim=5000, output_dim=16, input_length=max_len))
model.add(SimpleRNN(units=32))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

"""
5. Train the Model
Train your RNN on the prepared dataset.
"""
from sklearn.preprocessing import LabelEncoder

# Encode labels to binary format
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)

# Fit the model
model.fit(X_train_pad, y_train_encoded, epochs=5, validation_data=(X_test_pad, y_test_encoded))

"""
6. Evaluate and Use the Model
Evaluate the performance of your trained model and use it for predictions.
"""

# Model evaluation
loss, accuracy = model.evaluate(X_test_pad, y_test_encoded)
print(f'Test Accuracy: {accuracy * 100:.2f}%')

# Predict on a new email
def predict_email(email):
    seq = tokenizer.texts_to_sequences([email])
    padded_seq = pad_sequences(seq, maxlen=max_len)
    prediction = model.predict(padded_seq)[0][0]
    
    if prediction > 0.5:
        return "Spam"
    else:
        return "Not Spam"

# Example usage
test_email = "Congratulations! You've won a $1000 gift card. Click here to claim now."
print(f'Test Email: {test_email} is classified as {predict_email(test_email)}')

"""
7. Troubleshooting Common Issues

- **Issue:** Model not converging.
  - **Solution:** Try adjusting the learning rate or increasing epochs.

- **Issue:** High False Positive Rate.
  - **Solution:** Experiment with different architectures, such as adding more RNN layers or using LSTM/GRU units.

- **Issue:** Data preprocessing errors.
  - **Solution:** Ensure your CSV file is correctly formatted and that text encoding issues are resolved.
"""