# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import subprocess

# app = Flask(__name__)
# CORS(app)

# @app.route('/upload-audio', methods=['POST'])
# def upload_audio():
#     try:
#         # Get the uploaded audio file
#         audio_file = request.files['audio']
#         audio_path = 'uploaded_audio.mp3'
#         audio_file.save(audio_path)

#         # Call audio.py to generate transcript
#         subprocess.run(['python', r'C:\Users\HP\Desktop\AutoLex\backend\longaudio.py'])

#         # Call summary.py to generate summary
#         subprocess.run(['python', r'C:\Users\HP\Desktop\AutoLex\backend\Summary.py'])

#         # Call keywords.py to generate keywords and clusters
#         subprocess.run(['python', r'C:\Users\HP\Desktop\AutoLex\backend\KeywordwithRAKE.py'])

#         # Call search.py to generate resources
#         subprocess.run(['python', r'C:\Users\HP\Desktop\AutoLex\backend\CustomSearch.py'])

#         # Read the result files based on the selected button
#         selected_button = request.form['selected_button']
#         result_files = {
#             'transcript': 'transcript.txt',
#             'summary': 'summary.txt',
#             'keywords': 'clusters.txt',
#             'resources': 'results.txt'
#         }

#         result_content = {}
#         for key, file_name in result_files.items():
#             with open(file_name, 'r') as file:
#                 result_content[key] = file.read()

#         return jsonify({'result': result_content})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import re
import subprocess
import json
from vosk import Model, KaldiRecognizer
import json
from pydub import AudioSegment
from transformers import pipeline
from rake_nltk import Rake
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


app = Flask(__name__)
CORS(app)

@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    try:
        # Get the uploaded audio file
        audio_file = request.files['audio']
        audio_path = 'uploaded_audio.mp3' 
        audio_file.save(audio_path)

        # Call audio processing function
        result = process_audio(audio_path)

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def process_audio(audio_path, selected_button):
    result = {}

    transcript = speech_to_text(audio_path)
    summary = generate_summary(transcript)
    keywords = generate_keywords(transcript)
    resources = custom_search(keywords)
    
    result['transcript'] = transcript
    result['summary'] = summary
    result['keywords'] = keywords
    result['resources'] = resources

    return result



def speech_to_text(audio_path):
    FRAME_RATE = 16000
    CHANNELS=1
    model = Model(model_name="vosk-model-en-us-0.22")

    rec = KaldiRecognizer(model, FRAME_RATE)
    rec.SetWords(True)

    mp3 = AudioSegment.from_mp3(audio_path)
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
        with open("transcript.txt", "w") as file:
            file.write(transcript)
        return transcript 


def generate_summary(transcript):
    summarizer = pipeline("summarization")

    with open("transcript.txt", "r") as file:
        transcript = file.read()
    
    split_tokens = transcript.split(" ")
    docs = []

    for i in range(0, len(split_tokens), 850):
        selection = " ".join(split_tokens[i:(i+850)])
    docs.append(selection)
    summaries = summarizer(docs)
    summary = "\n\n".join(d["summary_text"] for d in summaries)

    with open("summary.txt", "w") as file:
        file.write(summary)
    return summary

def generate_keywords(transcript):
    r = Rake()

    with open("transcript.txt", "r") as file:
        transcript = file.read()

    r.extract_keywords_from_text(transcript)
    keywords = r.get_ranked_phrases()


    with open("keywords.txt", "w") as file:
        for keyword in keywords:
            file.write(keyword + "\n")


    keyword_texts = [' '.join(keyword.split()) for keyword in keywords]
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(keyword_texts)

    num_clusters = 5  
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(X)


    with open("clusters.txt", "w") as file:
        for cluster_idx in range(num_clusters):
            cluster_keywords = []
            for i, label in enumerate(kmeans.labels_):
                if label == cluster_idx:
                    cluster_keywords.append(keywords[i])
            file.write(f"Cluster {cluster_idx + 1}:\n")
            if len(cluster_keywords) > 10:
                cluster_keywords = cluster_keywords[:10]  
            file.write(", ".join(cluster_keywords) + "\n\n")


    print("Keywords:")
    for cluster_idx in range(num_clusters):
        cluster_keywords = []
    for i, label in enumerate(kmeans.labels_):
        if label == cluster_idx:
            cluster_keywords.append(keywords[i])
    print(f"Cluster {cluster_idx + 1}:")
    if len(cluster_keywords) > 10:
        cluster_keywords = cluster_keywords[:10]  
    print(", ".join(cluster_keywords))
    print()
    return cluster_keywords

def custom_search(keywords):
    with open("keywords.txt", "r") as file:
        keywords = file.read().split()[:20]  
    print("Keywords:", keywords)

    api_key = "AIzaSyCE0GYDLYWWjL4rQsEpSzrogcLvBjBI_Vc"

    from apiclient.discovery import build

    resource = build("customsearch", 'v1', developerKey=api_key).cse()

    search_query = ' '.join(keywords)

    result = resource.list(q=search_query, cx='009557628044748784875:5lejfe73wrw').execute()

    print("Search Results:")
    with open("results.txt", "w") as result_file:
        for item in result.get('items', []):
            title = item.get('title', 'N/A')
            link = item.get('link', 'N/A')
            result_file.write(f"Title: {title}\nLink: {link}\n\n")
            print("Title:", title)
            print("Link:", link)
            print()
            return result_file
    

if __name__ == '__main__':
    app.run(debug=True)
