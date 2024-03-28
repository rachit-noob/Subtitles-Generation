import streamlit as st
import os
import assemblyai as aai
import base64

# Set up AssemblyAI API key
aai.settings.api_key = "7dadd0dab12746c5ae0adb2d6743d220"


def transcribe_video(video_path):
    try:
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(video_path)
        return transcript.text
    except Exception as e:
        print(f"Error: {e}")
        return None
    
print(transcribe_video('uploads/How to add audio to your YouTube #shorts.mp4'))