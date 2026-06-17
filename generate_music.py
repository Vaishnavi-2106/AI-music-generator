from tensorflow.keras.models import load_model
import pickle
import numpy as np

from music21 import stream, note


model = load_model("music_model.h5")


with open("notes.pkl","rb") as f:
    notes = pickle.load(f)


unique_notes = sorted(set(notes))


int_to_note = {
    i:n for i,n in enumerate(unique_notes)
}



output_notes = []


for i in range(100):

    random_index = np.random.randint(
        0,
        len(unique_notes)
    )

    output_notes.append(
        int_to_note[random_index]
    )



music = stream.Stream()



for item in output_notes:

    if "." in item:

        first_note = item.split(".")[0]

        music.append(
            note.Note(first_note)
        )

    else:

        music.append(
            note.Note(item)
        )



music.write(
    "midi",
    fp="generated_music.mid"
)


print("Generated music saved as generated_music.mid")