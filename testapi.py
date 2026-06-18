import requests

response = requests.get("https://api.agify.io?name=safee")

print(response.json())