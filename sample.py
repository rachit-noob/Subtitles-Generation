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
        st.error(f"Error: {e}")
        return None


# Define SRT Generation Function
def generate_srt(transcript_text):
    lines = transcript_text.split('\n')
    srt_content = ''
    index = 1
    start_time = 0
    
    for line in lines:
        if line.strip():
            # Format time in HH:MM:SS,mmm
            start_time_str = "{:02d}:{:02d}:{:02d},000".format(start_time // 3600, (start_time % 3600) // 60, start_time % 60)
            end_time_str = "{:02d}:{:02d}:{:02d},000".format((start_time + 5) // 3600, ((start_time + 5) % 3600) // 60, (start_time + 5) % 60)
            
            # Append subtitle index, time and text
            srt_content += f"{index}\n{start_time_str} --> {end_time_str}\n{line}\n\n"
            
            # Increment index and move to next time slot
            index += 1
            start_time += 5
    
    return srt_content

def main():
    st.title("Video Transcription and SRT Generation App")
    
    # File upload widget
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi", "mkv"])

    if uploaded_file is not None:
        # Transcribe and generate SRT on button click
        if st.button("Transcribe and Generate SRT"):
            # Save the uploaded file
            with open("temp_video.mp4", "wb") as f:
                f.write(uploaded_file.getvalue())

            # Transcribe video
            transcript_text = transcribe_video("temp_video.mp4")

            if transcript_text is not None:
                # Generate SRT content
                srt_content = generate_srt(transcript_text)

                # Provide options to print or download transcript
                if st.checkbox("Print Transcript"):
                    print(transcript_text)
                    st.write(transcript_text)

                if st.checkbox("Download Transcript"):
                    href = f'<a href="data:file/txt;base64,{base64.b64encode(transcript_text.encode()).decode()}" download="transcript.txt">Download Transcript</a>'
                    st.markdown(href, unsafe_allow_html=True)

                # Delete temporary files
                os.remove("temp_video.mp4")
            else:
                st.error("Error: Unable to transcribe the video.")

if __name__ == "__main__":
    main()
