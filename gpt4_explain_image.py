import base64
import os
import requests


def gpt4_explain_image(image_path, prompt):
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    OPENAI_API_KEY = "[OPENAI_API_KEY]"

    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=payload)
    response = response.json()

    assistant_message = response['choices'][0]['message']['content']
    return assistant_message


image_path = 'images/wrong.jpeg'
prompt = 'Is this image correct?'
print(gpt4_explain_image(image_path, prompt))
