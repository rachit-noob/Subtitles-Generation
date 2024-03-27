import assemblyai as aai

aai.settings.api_key = "7dadd0dab12746c5ae0adb2d6743d220"
transcriber = aai.Transcriber()

def transcribe_audio(video_file):
    transcript = transcriber.transcribe(video_file)

    return transcript.text

print(transcribe_audio('uploads/How to add audio to your YouTube #shorts.mp4'))