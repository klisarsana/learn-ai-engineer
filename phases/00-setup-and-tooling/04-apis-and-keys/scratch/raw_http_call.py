import json
import os
import urllib.request

api_key = os.environ["GEMINI_API_KEY"]
model = os.environ.get("LLM_MODEL", "gemini-3.8-flash")

url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
headers = {
    "Content-Type": "application/json",
}
body = json.dumps({
    "contents": [{
        "parts": [{"text": "What is a neural network in one sentence?"}]
    }],
    "generationConfig": {
        "maxOutputTokens": 256
    }
}).encode()

req = urllib.request.Request(url, data=body, headers=headers, method="POST")
with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read())
    print(result["candidates"][0]["content"]["parts"][0]["text"])
