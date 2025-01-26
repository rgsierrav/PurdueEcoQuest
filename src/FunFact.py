
import requests

def search_groq(query):
    api_url = 'https://api.groq.com'
    api_key = "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"  # replace with your actual API key
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    params = {
        'query': query
    }

    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return f'Error: {response.status_code}'

def main():
    query = input('What do you want to know more about ')
    results = search_groq(query)
    print(results)

if __name__ == '__main__':
    main()

import os
from groq import Groq

client = Groq(
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama-3.3-70b-versatile",
    stream=False,
)

print(chat_completion.choices[0].message.content)

#Need to make sure that it outpts an AI generated response.