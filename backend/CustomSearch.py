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