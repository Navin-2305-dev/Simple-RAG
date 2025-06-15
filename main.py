from collections import Counter
import json
import math
import requests

def cosine_similarity(query, document):
    query_tokens = query.lower().split(" ")
    document_tokens = document.lower().split(" ")

    query_counter = Counter(query_tokens)
    document_counter = Counter(document_tokens)

    dot_product = sum(query_counter[token] * document_counter[token] for token in query_counter.keys() & document_counter.keys())
    query_magnitude = math.sqrt(sum(query_counter[token] ** 2 for token in query_counter))
    document_magnitude = math.sqrt(sum(document_counter[token] ** 2 for token in document_counter))
    similarity = dot_product / (query_magnitude * document_magnitude) if query_magnitude * document_magnitude != 0 else 0
    return similarity

# query='I love to enjoy fresh air and discover something new'
query = input("Enter your query: ")

corpus = [
    "Take a leisurely walk in the park and enjoy the fresh air.",
    "Visit a local museum and discover something new.",
    "Attend a live music concert and feel the rhythm.",
    "Go for a hike and admire the natural scenery.",
    "Have a picnic with friends and share some laughs.",
    "Explore a new cuisine by dining at an ethnic restaurant.",
    "Take a yoga class and stretch your body and mind.",
    "Join a local sports league and enjoy some friendly competition.",
    "Attend a workshop or lecture on a topic you're interested in.",
    "Visit an amusement park and ride the roller coasters."
]

# Sorting the Documents based on cosine similarity
a=[]
for i in corpus:
    a.append([i, cosine_similarity(query, i)])
a.sort(key=lambda x: x[1], reverse=True)

full_response = []
prompt = """
You are a bot that makes recommendations for activities. You answer should not include extra information.
This is the recommended activity: {relevant_document}
The user input is: {user_input}
Compile a recommendation to the user based on the recommended activity and the user input, and give in proper format
"""

url = 'http://localhost:11434/api/generate'

# Considering only the top 3 relevant documents
data = {
    "model": "mistral",
    "prompt": prompt.format(user_input=query, relevant_document=corpus[:3])
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers, stream=True)

for line in response.iter_lines():
        if line:
            decoded_line = json.loads(line.decode('utf-8'))
            full_response.append(decoded_line['response'])

print("Response from the server:", ' '.join(full_response))
