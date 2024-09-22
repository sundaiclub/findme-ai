import openai
import os
from dotenv import load_dotenv
load_dotenv()



class OpenAIApi:
    def __init__(self):
        self.openai_api = openai.OpenAI()

    def get_completion(self, prompt, model="gpt-4o-mini"):
        messages = [{"role": "user", "content": prompt}]
        response = self.openai_api.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0,  # this is the degree of randomness of the model's output
        )
        return response.choices[0].message.content