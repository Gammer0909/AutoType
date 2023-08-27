import openai as ai
import json
import os


# Get the absolute path of the file
file_path = os.getcwd() + "/key.txt"

# Load API key
with open(file_path, "r") as f:
    ai.api_key = f.read().strip()


def GetResponse(prompt, model="gpt-3.5-turbo"):
        # Call GPT-4
        response = ai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are GPT. You are a helpful assistant."},
            {"role": "user", "content": "Hello, who are you? When you answer, please use markdown formatting, such as *this for italic*, **this for bold** and __this for underlined__."},
            {"role": "assistant", "content": "I am GPT. I am here to help you with your homework."},
            {"role": "user", "content": prompt},
        ]
    )
        return response.choices[0].message.content


