import os
from dotenv import load_dotenv
import requests

load_dotenv()

URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent'

data = {"contents":
    [
        {"parts":
            [
                {"text":"Write a story about a magic backpack"}
            ]
        }
    ]
}

res = requests.post(
    url=URL,
    headers={
        "content-type": "application/json",
    },
    json=data,
    params={"key": os.getenv("GEMINI_API_KEY")}
)

print(res.json())