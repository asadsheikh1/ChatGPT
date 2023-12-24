import requests

def gpt4_generate_image_from_prompt(prompt):
    OPENAI_API_KEY = "[OPENAI_API_KEY]"

    url = "https://api.openai.com/v1/images/generations"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }

    data = {
        "model": "dall-e-3",
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024",
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        result = f"Error: {response.status_code}\n{response.text}"
        return result


print(gpt4_generate_image_from_prompt("Futuristic Car"))
