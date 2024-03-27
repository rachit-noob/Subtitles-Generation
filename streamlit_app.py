import streamlit as st
import requests

def main():
    st.title("Video Transcription App")
    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "wav", "mp3"])
    if uploaded_file is not None:
        response = requests.post("http://localhost:5000/upload", files={"file": uploaded_file})
        if response.status_code == 200:
            st.write("Transcription:")
            st.write(response.text)
        else:
            print(response)
            st.write("Error uploading file")

if __name__ == "__main__":
    main()
