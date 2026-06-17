import numpy as np
import pickle

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout


# Load notes
with open("notes.pkl","rb") as f:
    notes = pickle.load(f)


unique_notes = sorted(set(notes))


note_to_int = {
    n:i for i,n in enumerate(unique_notes)
}


sequence_length = 50


network_input = []


for i in range(len(notes)-sequence_length):

    sequence = notes[i:i+sequence_length]

    network_input.append(
        [note_to_int[n] for n in sequence]
    )


X = np.array(network_input)


X = np.reshape(
    X,
    (X.shape[0], X.shape[1], 1)
)


X = X / len(unique_notes)



model = Sequential()


model.add(
    LSTM(
        128,
        input_shape=(X.shape[1],1),
        return_sequences=True
    )
)


model.add(Dropout(0.2))


model.add(
    LSTM(128)
)


model.add(
    Dense(128, activation="relu")
)


model.add(
    Dense(len(unique_notes), activation="softmax")
)


model.compile(
    loss="sparse_categorical_crossentropy",
    optimizer="adam"
)



model.fit(
    X,
    X[:,-1],
    epochs=50,
    batch_size=64
)



model.save("music_model.h5")


print("Model training completed")