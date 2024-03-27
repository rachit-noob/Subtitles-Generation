# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

# aai.settings.api_key = "7dadd0dab12746c5ae0adb2d6743d220"
# transcriber = aai.Transcriber()

# transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
# transcript = transcriber.transcribe("./my-local-audio-file.wav")
# print(transcript.text)


import assemblyai as aai

aai.settings.api_key = "7dadd0dab12746c5ae0adb2d6743d220"
transcriber = aai.Transcriber()

def transcribe_audio(video_file):
    transcript = transcriber.transcribe(video_file)
    return transcript.text
