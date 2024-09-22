from src.openai_api import OpenAIApi

import re
import ast

openai_api = OpenAIApi()


def parse_response(response):
    matches = re.findall(r"```json(.*?)```", response, re.DOTALL)
    if matches:
        return ast.literal_eval(matches[0].strip())
    else:
        return None

def extract_topics_from_answers(prompt, questionaire):
    prompt = prompt.format(questionnaire=questionaire)

    for i in range(3):
        try:
            response = openai_api.get_completion(prompt)
            response = parse_response(response)
            if response:
                return response
        except Exception as e:
            print(f"An error occurred: {e}")
    return response



    


