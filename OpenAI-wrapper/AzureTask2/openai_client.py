from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), base_url="https://api.openai.com/v1")

def call_openai_api(text):
    response = client.chat.completions.create(
        model="gpt-5-nano", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."}, 
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content