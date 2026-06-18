import requests

# 1. We define the URL of a free, public API that gives random facts about cats
url = "https://catfact.ninja/fact"

print("Sending a GET request to the Cat Fact API...")

# 2. We send the GET request
response = requests.get(url)

# 3. We convert the response into a clean JSON format
data = response.json()

# 4. Let's see the raw JSON response!
print("\n--- The JSON Response Received ---")
print(data)

# 5. Let's extract just the specific value using its 'key'
print("\n--- Just the Fact ---")
print(data["fact"])