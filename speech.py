"""
This file takes in voice commands
For a given sentence, outputs the color of the block that should be picked up
"""

import whisper
import sounddevice as sd

model = whisper.load_model("tiny")

while True:
    # Record
    audio = sd.rec(3 * 16000, samplerate=16000, channels=1)
    sd.wait()

    # Speech to Text
    recording = model.transcribe(audio.flatten())
    text = recording["text"].lower()
    print("Detected: ", text)

    for color in ["red", "green", "blue"]:
        if color in text:
            print("The robot will pick up: ", color)
            break
