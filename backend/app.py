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
from apiclient.discovery import build


app = Flask(__name__)
CORS(app)

@app.route('/get-transcript', methods=["POST","GET"])

def upload_audio():
    if request.method == 'POST':
        try:
        # Get the uploaded audio file
            audio_file = request.files['file']
            audio_path = 'uploaded_audio.mp3' 
            audio_file.save(audio_path)

        # Call audio processing function
            result = process_audio(audio_path)

            return jsonify(result)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Method not allowed'}), 405

def process_audio(audio_path):
    result = {}

    transcript = speech_to_text(audio_path)
    result['transcript'] = transcript
    summary = generate_summary(transcript)
    result['summary'] = summary
    keywords = generate_keywords(transcript)
    result['keywords'] = keywords
    clusters = cluster_keywords(keywords)
    result['clusters'] = clusters
    resources = custom_search(keywords)
    result['resources'] = resources
    
    return result 
   
# def speech_to_text(audio_path):
#     FRAME_RATE = 16000
#     CHANNELS=1
#     model = Model(model_name="vosk-model-en-us-0.22")

#     rec = KaldiRecognizer(model, FRAME_RATE)
#     rec.SetWords(True)

#     mp3 = AudioSegment.from_mp3(audio_path)
#     mp3 = mp3.set_channels(CHANNELS)
#     mp3 = mp3.set_frame_rate(FRAME_RATE)

#     step = 45000
#     transcript = ""
#     for i in range(0, len(mp3), step):
#         print(f"Progress: {i/len(mp3)}")
#         segment = mp3[i:(i+step)]

#         rec.AcceptWaveform(segment.raw_data)
#         result = rec.Result()

#         text = json.loads(result)["text"]
#         transcript += text
    
#     # Ensure that the entire transcript is captured before returning
#     return transcript

def speech_to_text(audio_path):
    FRAME_RATE = 16000
    CHANNELS = 1
    model = Model(model_name="vosk-model-en-us-0.22")

    rec = KaldiRecognizer(model, FRAME_RATE)
    rec.SetWords(True)

    mp3 = AudioSegment.from_mp3(audio_path)
    mp3 = mp3.set_channels(CHANNELS)
    mp3 = mp3.set_frame_rate(FRAME_RATE)

    step = 45000
    transcript = ""

    for i in range(0, len(mp3), step):
        # print(f"Processing segment {i/len(mp3)}")
        segment = mp3[i:(i+step)]

        rec.AcceptWaveform(segment.raw_data)
        result = json.loads(rec.Result())

        # print(f"Result for segment {i/len(mp3)}: {result}")

        if 'text' in result:
            transcript += result['text']
    
    print(f"Final Transcript: {transcript}")
    print("\n")
    return transcript


def generate_summary(transcript):
    summarizer = pipeline("summarization",  model="sshleifer/distilbart-cnn-12-6", revision="a4f8f3e")
    # summarizer = pipeline("summarization")
    split_tokens = transcript.split(" ")
    docs = []

    for i in range(0, len(split_tokens), 850):
        selection = " ".join(split_tokens[i:(i+850)])
        docs.append(selection)

    summaries = summarizer(docs,max_length=56, min_length=32, do_sample=False)
    summary = "\n\n".join(d["summary_text"] for d in summaries)
    print(f"Summary: {summary}")
    print("\n")
    return summary


def generate_keywords(transcript):
    r = Rake()
    r.extract_keywords_from_text(transcript)
    keywords = r.get_ranked_phrases()
    
    keyword_texts = [' '.join(keyword.split()) for keyword in keywords[:3]]

    print(f"Keywords: {keyword_texts}")
    print("\n")
    return keywords


# def cluster_keywords(keywords):
#     vectorizer = TfidfVectorizer(stop_words='english')
#     X = vectorizer.fit_transform(keywords)

#     num_clusters = 5
#     kmeans = KMeans(n_clusters=num_clusters, n_init=10)
#     kmeans.fit(X)
    
#     for cluster_idx in range(num_clusters):
#         cluster_keywords = []
#         for i, label in enumerate(kmeans.labels_):
#             if label == cluster_idx:
#                 cluster_keywords.append(keywords[i])
#         print(f"Cluster {cluster_idx + 1}:")
#         if len(cluster_keywords) > 10:
#             cluster_keywords = cluster_keywords[:10]  
#         print(", ".join(cluster_keywords))
#         print(f"Topics: {cluster_keywords}")
#         print("\n")
#     return cluster_keywords

def cluster_keywords(keywords):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(keywords)

    num_clusters = 5
    kmeans = KMeans(n_clusters=num_clusters, n_init=10)
    kmeans.fit(X)
    
    cluster_keywords_list = []

    for cluster_idx in range(num_clusters):
        cluster_keywords = []
        for i, label in enumerate(kmeans.labels_):
            if label == cluster_idx:
                cluster_keywords.append(keywords[i])
        print(f"Cluster {cluster_idx + 1}:")
        if len(cluster_keywords) > 10:
            cluster_keywords = cluster_keywords[:10]
        cluster_keywords_list.append(", ".join(cluster_keywords))
        print(", ".join(cluster_keywords))
        print(f"Topics: {cluster_keywords}")
        print("\n")
    
    return cluster_keywords_list

# def generate_keywords(transcript):
#     r = Rake()
#     r.extract_keywords_from_text(transcript)
#     keywords = r.get_ranked_phrases()

#     keyword_texts = [' '.join(keyword.split()) for keyword in keywords]
#     vectorizer = TfidfVectorizer(stop_words='english')
#     X = vectorizer.fit_transform(keyword_texts)

#     num_clusters = 5  
#     kmeans = KMeans(n_clusters=num_clusters, n_init=10)

#     kmeans.fit(X)
#     for cluster_idx in range(num_clusters):
#         cluster_keywords = []
#         for i, label in enumerate(kmeans.labels_):
#             if label == cluster_idx:
#                 cluster_keywords.append(keywords[i])
#         print(f"Cluster {cluster_idx + 1}:")
#         if len(cluster_keywords) > 10:
#             cluster_keywords = cluster_keywords[:10]  
#         print(", ".join(cluster_keywords))
#         print()
#     return cluster_keywords

# def custom_search(keywords):
#     keywords = keywords[:10]
#     api_key = "AIzaSyCE0GYDLYWWjL4rQsEpSzrogcLvBjBI_Vc"

#     resource = build("customsearch", 'v1', developerKey=api_key).cse()

#     search_query = ' '.join(keywords)

#     result = resource.list(q=search_query, cx='009557628044748784875:5lejfe73wrw').execute()

#     print("Search Results:")
#     result_output = []
#     for item in result.get('items', []):
#         title = item.get('title', 'N/A')
#         link = item.get('link', 'N/A')
#         result_output.append({"Title": title, "Link": link})
#         print(f"Title: {title}")
#         print(f"Link: {link}")
#         print()
#         print("\n")
    
#     return result_output

def custom_search(keywords):
    keywords = keywords[:1]
    api_key = "AIzaSyCE0GYDLYWWjL4rQsEpSzrogcLvBjBI_Vc"

    resource = build("customsearch", 'v1', developerKey=api_key).cse()

    search_query = ' '.join(keywords)
    print(f"Search Query: {search_query}")  

    try:
        result = resource.list(q=search_query, cx='009557628044748784875:5lejfe73wrw').execute()
    except Exception as e:
        print(f"Error executing search: {e}")
        return {"error": "Failed to execute search"}

    print("Search Results:")
    result_output = []
    items = result.get('items', [])
    
    if not items:
        print("No items found in search results")
        return result_output

    for item in items:
        title = item.get('title', 'N/A')
        link = item.get('link', 'N/A')
        result_output.append({"Title": title, "Link": link})
        print(f"Title: {title}")
        print(f"Link: {link}")
        print()
        print("\n")
    
    return result_output


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
