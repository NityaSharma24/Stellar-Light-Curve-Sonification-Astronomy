//Cell 1

from google.colab import files
uploaded = files.upload();

//Cell 2
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

filename = "cyg_x1_approx_1000s_intervals.csv"
df = pd.read_csv(filename)

display(df.head())

//Cell 3
time = df["time_seconds_approx"].to_numpy()
counts = df["counts_approx"].to_numpy()

plt.figure(figsize = (12,4))
plt.plot(time, counts, marker = ".")
plt.xlabel("Time (seconds)")
plt.ylabel("Estimated X-Ray Counts")
plt.title("Cyg X-1: Approximate LightCurve")
plt.grid(True)
plt.show()

//Cell 4
normalized = ((counts - counts.min()) / (counts.max() - counts.min()))
midi_notes = 48 + normalized * 36
frequencies = 440 * 2 ** ((midi_notes - 69)/12)
print("First 10 MIDI notes: ", np.round(midi_notes[:10], 1))
print("First 10 frequences (Hz): ", np.round(frequencies[:10], 1))

//Cell 5
from IPython.display import Audio, display
sample_rate = 44100
note_duration = 0.25

samples_per_note = int(sample_rate * note_duration)

audio = np.zeros(len(frequencies) * samples_per_note)
for i, frequency in enumerate(frequencies):
    start = samples_per_note
    end = start + samples_per_note

    t = np.arange(samples_per_note) / sample_rate
    tone = np.sin(2 * np.pi * frequency * t)

    fade_n = int(0.01 * sample_rate)
    envelope = np.ones(samples_per_note)
    envelope[:fade_n] = np.linspace(0, 1, fade_n)
    envelope[-fade_n:] = np.linspace(1, 0, fade_n)

    audio[start:end] = tone * envelope
audio = 0.25 * audio / max(np.max(np.abs(audio)), 1e-12)
display(Audio(audio, rate=sample_rate))

//Cell 6
from scipy.io.wavfile import write
from google.colab import files

write(
    "cyg_x1_continuous_sonification.wav",
    sample_rate,
    np.int16(audio * 32767)
)

files.download("cyg_x1_continuous_sonification.wav")
