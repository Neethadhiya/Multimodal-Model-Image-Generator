import os
from dotenv import load_dotenv
from together import Together
from typing import Union

from fastapi import FastAPI
app = FastAPI()
load_dotenv()
import requests
STABILITY_API_KEY = os.getenv("STABILITY_API_KEY")
response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/ultra",
    headers={
        "authorization": f"Bearer {STABILITY_API_KEY}",
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": "Lighthouse on a cliff overlooking the ocean",
        "output_format": "webp",
    },
)

if response.status_code == 200:
    with open("./lighthouse.webp", 'wb') as file:
        file.write(response.content)
else:
    raise Exception(str(response.json()))