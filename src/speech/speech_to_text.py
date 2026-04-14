# import whisper
# import sounddevice as sd
# import numpy as np
# import torch
# import tempfile
# import scipy.io.wavfile as wav

# # Load model once (important!)
# device = "cuda" if torch.cuda.is_available() else "cpu"
# print("Using device:", device)
# model = whisper.load_model("small").to(device)


# def record_audio(duration=5, samplerate=16000):
#     print("🎙 Recording for 5 seconds...")
#     audio = sd.rec(int(duration * samplerate),
#                    samplerate=samplerate,
#                    channels=1,
#                    dtype="int16")
#     sd.wait()
#     print("✅ Recording complete.")
#     return audio, samplerate


# def recognize_speech():
#     audio, samplerate = record_audio()

#     # Save to temporary file
#     with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
#         wav.write(f.name, samplerate, audio)
#         temp_filename = f.name

#     print("🧠 Transcribing...")
#     result = model.transcribe(temp_filename)

#     text = result["text"].strip()
#     print(f"📝 Recognized Text: {text}")

#     return text


# if __name__ == "__main__":
#     recognize_speech()
# import whisper
# import sounddevice as sd
# import numpy as np
# import torch
# import tempfile
# import scipy.io.wavfile as wav

# device = "cuda" if torch.cuda.is_available() else "cpu"
# model = None  # 👈 lazy load


# def get_model():
#     global model
#     if model is None:
#         print("🧠 Loading Whisper model...")
#         model = whisper.load_model("small").to(device)
#         print("✅ Whisper model loaded")
#     return model


# def record_audio(duration=5, samplerate=16000):
#     print("🎙 Recording for 5 seconds...")
#     audio = sd.rec(
#         int(duration * samplerate),
#         samplerate=samplerate,
#         channels=1,
#         dtype="int16"
#     )
#     sd.wait()
#     print("✅ Recording complete.")
#     return audio, samplerate


# def recognize_speech():
#     audio, samplerate = record_audio()

#     with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
#         wav.write(f.name, samplerate, audio)
#         temp_filename = f.name

#     model = get_model()

#     print("🧠 Transcribing...")
#     result = model.transcribe(temp_filename)

#     text = result["text"].strip()
#     print(f"📝 Recognized Text: {text}")

#     return text

# src/speech/speech_to_text.py

import whisper
import sounddevice as sd
import numpy as np
import torch
import tempfile
import scipy.io.wavfile as wav

device = "cuda" if torch.cuda.is_available() else "cpu"

# Load model ONCE
model = whisper.load_model("small").to(device)


def record_audio(duration=5, samplerate=16000):
    audio = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="int16"
    )
    sd.wait()
    return audio, samplerate
# def is_silent(audio, threshold=300):
#     return np.abs(audio).mean() < threshold

# def recognize_speech():
#     audio, samplerate = record_audio()

#     with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
#         wav.write(f.name, samplerate, audio)
#         temp_filename = f.name

#     result = model.transcribe(temp_filename)
#     return result["text"].strip()

def recognize_speech():
    audio, samplerate = record_audio()

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        wav.write(f.name, samplerate, audio)
        temp_filename = f.name

    result = model.transcribe(temp_filename)
    spoken_text = result["text"].strip()

    print(f"\n🎙 You said: {spoken_text}")
    return spoken_text


# def recognize_speech():
#     audio, samplerate = record_audio()

#     # 🔴 SILENCE CHECK
#     if is_silent(audio):
#         print("🔇 No speech detected (silence)")
#         return ""

#     with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
#         wav.write(f.name, samplerate, audio)
#         temp_filename = f.name

#     print("🧠 Transcribing...")
#     result = model.transcribe(temp_filename)

#     text = result["text"].strip()
#     print(f"📝 Recognized Text: {text}")

#     return text