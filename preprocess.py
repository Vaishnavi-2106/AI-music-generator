from music21 import converter, instrument, note, chord
import glob
import pickle


notes = []

# Read MIDI files from dataset folder
for file in glob.glob("dataset/*.mid"):

    midi = converter.parse(file)

    parts = instrument.partitionByInstrument(midi)

    if parts:
        elements = parts.parts[0].recurse()
    else:
        elements = midi.flat.notes


    for element in elements:

        if isinstance(element, note.Note):
            notes.append(str(element.pitch))

        elif isinstance(element, chord.Chord):
            notes.append(".".join(str(n.pitch) for n in element.notes))


print("Total notes:", len(notes))


# Save notes
with open("notes.pkl", "wb") as f:
    pickle.dump(notes, f)


print("Preprocessing completed")