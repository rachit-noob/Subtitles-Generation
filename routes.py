from flask import render_template, request, redirect, url_for
import os
from app import app
from assemblyai_transcribe import transcribe_audio


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp4', 'wav', 'mp3'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = file.filename
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        transcript = transcribe_audio(file_path)
        # Here you can do further processing like generating SRT file
        return transcript
    return 'Error uploading file'
