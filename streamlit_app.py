import streamlit as st
import requests

def main():
    st.title("Video Transcription App")
    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "wav", "mp3"])
    if uploaded_file is not None:
        try:
            response = requests.post("http://localhost:5000/upload", files={"file": uploaded_file})
            if response.status_code == 200:
                st.write("Transcription:")
                st.write(response.text)
            else:
                st.error("Error uploading file: {}".format(response.text))
        except Exception as e:
            st.error("An error occurred: {}".format(str(e)))

if __name__ == "__main__":
    main()
