from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    try:
        # Get the uploaded audio file
        audio_file = request.files['audio']
        audio_path = 'uploaded_audio.mp3'
        audio_file.save(audio_path)

        # Call audio.py to generate transcript
        subprocess.run(['python', r'C:\Users\HP\Desktop\AutoLex\backend\longaudio.py'])

        # Call summary.py to generate summary
        subprocess.run(['python', r'C:\Users\HP\Desktop\AutoLex\backend\Summary.py'])

        # Call keywords.py to generate keywords and clusters
        subprocess.run(['python', r'C:\Users\HP\Desktop\AutoLex\backend\KeywordwithRAKE.py'])

        # Call search.py to generate resources
        subprocess.run(['python', r'C:\Users\HP\Desktop\AutoLex\backend\CustomSearch.py'])

        # Read the result files based on the selected button
        selected_button = request.form['selected_button']
        result_file = ''
        if selected_button == 'transcript':
            result_file = 'transcript.txt'
        elif selected_button == 'summary':
            result_file = 'summary.txt'
        elif selected_button == 'keywords':
            result_file = 'clusters.txt'
        elif selected_button == 'resources':
            result_file = 'results.txt'

        with open(result_file, 'r') as file:
            result_content = file.read()

        return jsonify({'result': result_content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
