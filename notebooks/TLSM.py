import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
import numpy as np
import pandas as pd


# leemos el csv
df = pd.read_csv('data/train.csv')
# Datos de ejemplo (reemplaza esto con tus datos)
texts = ["Este es un comentario no tóxico.", "Este comentario es ofensivo.", "Otro comentario inofensivo.", "Texto ofensivo aquí." ]
labels = [0, 1, 0, 1]  # 0 para no tóxico, 1 para tóxico

# Tokenización y secuenciación de textos
max_words = 1000
tokenizer = Tokenizer(num_words=max_words, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
padded_sequences = pad_sequences(sequences, maxlen=50, truncating='post', padding='post')

# Creación del modelo de red neuronal
model = Sequential()
model.add(Embedding(input_dim=max_words, output_dim=32, input_length=50))
model.add(LSTM(64))
model.add(Dense(1, activation='sigmoid'))

# Compilación del modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
padded_sequences = np.array(padded_sequences)
labels = np.array(labels)
# Entrenamiento del modelo
model.fit(padded_sequences, labels, epochs=10, batch_size=2)

# Ejemplo de predicción
test_text = ["Este es otro comentario no tóxico."]
test_sequence = tokenizer.texts_to_sequences(test_text)
padded_test_sequence = pad_sequences(test_sequence, maxlen=50, truncating='post', padding='post')
prediction = model.predict(padded_test_sequence)

print("Predicción:", prediction)
