from flask import Flask, request, jsonify
import speech_recognition as sr
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/transcribe', methods=['POST'])
def transcribe():
    # Initialize recognizer class in speech_recognition
    recognizer = sr.Recognizer()

    # Get the audio file from the request
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio']

    try:
        # Recognize speech using Google Speech Recognition
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
        print(text)
        return jsonify({'text': text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
