from src.openai_api import OpenAIApi

openai_api = OpenAIApi()

def create_path(prompt, category, user_bio, web_data):
    prompt = prompt.format(
        category=category,
        summary=user_bio,
        web_search_results=web_data
    )

    response = openai_api.get_completion(prompt)
    return response
