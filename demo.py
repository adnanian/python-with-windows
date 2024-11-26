

import sounddevice as sd
import numpy as np
import wave

print("Are you even working?")

# Parameters
duration = 5  # Duration in seconds
fs = 44100  # Sampling frequency

print("Recording...")
# Record audio
audio = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
sd.wait()  # Wait until recording is finished
print("Recording finished.")

# Save to a WAV file
with wave.open("output.wav", "wb") as wf:
    wf.setnchannels(2)  # Stereo
    wf.setsampwidth(2)  # 2 bytes per sample (16-bit audio)
    wf.setframerate(fs)  # Sampling frequency
    wf.writeframes(audio.tobytes())

print("Saved as output.wav.")
