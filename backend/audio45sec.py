from vosk import Model, KaldiRecognizer
from pydub import AudioSegment
import json

FRAME_RATE = 16000
CHANNELS=1

model = Model(model_name="vosk-model-en-us-0.22")

rec = KaldiRecognizer(model, FRAME_RATE)
rec.SetWords(True)

# AudioSegment.converter=r"C:\Users\HP\Desktop\ffmpeg\bin\ffmpeg.exe"

# # Transcribing a 45sec audio

mp3 = AudioSegment.from_mp3(r"C:\Users\HP\Desktop\backend-AutoLex\speech_recognition_marketplace.mp3")
mp3 = mp3.set_channels(CHANNELS)
mp3 = mp3.set_frame_rate(FRAME_RATE)

rec.AcceptWaveform(mp3.raw_data)
result = rec.Result()



text = json.loads(result)["text"]

print(text)