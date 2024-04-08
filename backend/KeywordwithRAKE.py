from rake_nltk import Rake
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


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


# print("Keywords:")
# for cluster_idx in range(num_clusters):
#     cluster_keywords = []
#     for i, label in enumerate(kmeans.labels_):
#         if label == cluster_idx:
#             cluster_keywords.append(keywords[i])
#     print(f"Cluster {cluster_idx + 1}:")
#     if len(cluster_keywords) > 10:
#         cluster_keywords = cluster_keywords[:10]  
#     print(", ".join(cluster_keywords))
#     print()
