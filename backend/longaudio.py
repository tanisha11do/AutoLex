from vosk import Model, KaldiRecognizer
import json
from pydub import AudioSegment

FRAME_RATE = 16000
CHANNELS=1


# # Transcribing Long Audio 
def voice_recognition(filename):
    model = Model(model_name="vosk-model-en-us-0.22")

    rec = KaldiRecognizer(model, FRAME_RATE)
    rec.SetWords(True)

    # AudioSegment.converter=r"C:\Users\HP\Desktop\ffmpeg\bin\ffmpeg.exe"

    mp3 = AudioSegment.from_mp3(filename)
    mp3 = mp3.set_channels(CHANNELS)
    mp3 = mp3.set_frame_rate(FRAME_RATE)

    step = 45000
    transcript = ""
    for i in range(0,len(mp3),step):
        print(f"Progress: {i/len(mp3)}")
        segment = mp3[i:(i+step)]

        rec.AcceptWaveform(segment.raw_data)
        result = rec.Result()

        text = json.loads(result)["text"]
        transcript += text

    print(transcript)

    with open("trascript.txt", "w") as file:
     file.write(transcript)

voice_recognition(r"C:\Users\HP\Downloads\GeorgeJackson.mp3")