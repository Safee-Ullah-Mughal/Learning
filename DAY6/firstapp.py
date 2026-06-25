import requests
import json

# 1. FIXED: Added Content-Type and removed the '<' and '>' from the key
headers = {
    "Authorization": "Bearer MY API KEY",
    "Content-Type": "application/json"
}

# 2. The payload remains beautifully structured
payload = {
    "model": "openai/gpt-4o",
    "rule": "Make heading of question and answer then respond",
    "messages": [
        {
            "role": "user",
            "content": "What is the meaning of life? Answer in one short sentence."
        }
    ],
    # FIX: Tell the server to only reserve a tiny budget for this response!
    "max_tokens": 100 
}

print("Sending POST request to OpenRouter...")

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    data=json.dumps(payload)
)

# 3. Let's print out what we get back!
print("Status Code:", response.status_code)

if response.status_code == 200:
    clean_data = response.json()
    print("\n--- AI Response ---")
    print(clean_data["choices"][0]["message"]["content"])
else:
    print("\n--- Error Response ---")
    print(response.text)