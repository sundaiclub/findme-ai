import openai
import os
from dotenv import load_dotenv
load_dotenv()



class OpenAiApi:
    def __init__(self):
        self.openai_api_key = openai.OpenAI(os.getenv("OPENAI_API_KEY"))

    def get_completion(self, prompt, model="gpt-4o-mini"):
        messages = [{"role": "user", "content": prompt}]
        response = openai.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0,  # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]