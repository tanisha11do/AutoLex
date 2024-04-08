with open("keywords.txt", "r") as file:
    keywords = file.read().split()[:20]  
print("Keywords:", keywords)

api_key = "AIzaSyCE0GYDLYWWjL4rQsEpSzrogcLvBjBI_Vc"

from apiclient.discovery import build

resource = build("customsearch", 'v1', developerKey=api_key).cse()

search_query = ' '.join(keywords)

result = resource.list(q=search_query, cx='009557628044748784875:5lejfe73wrw').execute()

print("Search Results:")
for item in result.get('items', []):
    print("Title:", item.get('title', 'N/A'))
    print("Link:", item.get('link', 'N/A'))
    print()
