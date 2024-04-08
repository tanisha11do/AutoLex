
from transformers import pipeline

summarizer = pipeline("summarization")

with open("transcript.txt", "r") as file:
    transcript = file.read()
    
split_tokens = transcript.split(" ")
docs = []

for i in range(0, len(split_tokens), 850):
    selection = " ".join(split_tokens[i:(i+850)])
    docs.append(selection)

summaries = summarizer(docs)

summaries

summary = "\n\n".join(d["summary_text"] for d in summaries)

with open("summary.txt", "w") as file:
    file.write(summary)

print(summary)






