import streamlit as st
from openai import OpenAI
import json
import os

from src.topic_extractor import extract_topics_from_answers
from src.query_generator import generate_queries
from src.prompts import query_gen_prompt, topic_extractor_prompt

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load questionnaire prompt
with open("streamlit-app/questionnaire-prompt.txt", "r") as f:
    questionnaire_prompt = f.read()

def get_ai_response(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return response.choices[0].message.content

def main():
    st.title("FindMe.AI")
    st.write("Answer 5 questions to generate your educational profile.")

    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.question_count = 0
        st.session_state.user_responses = []
    if st.session_state.question_count < 5:
        if len(st.session_state.messages) == 0:
            ai_message = get_ai_response([
                {"role": "system", "content": questionnaire_prompt},
                {"role": "user", "content": "Ask me the first question to understand my educational goals and preferences."}
            ])
            st.session_state.messages.append({"role": "assistant", "content": ai_message})

        for message in st.session_state.messages:
            st.write(f"{'You' if message['role'] == 'user' else 'AI'}: {message['content']}")

        user_input = st.text_input("Your response:", key=f"user_input_{st.session_state.question_count}")

        if st.button("Submit"):
            if user_input:
                st.session_state.messages.append({"role": "user", "content": user_input})
                st.session_state.user_responses.append(user_input)
                st.session_state.question_count += 1

                if st.session_state.question_count < 5:
                    ai_message = get_ai_response(st.session_state.messages + [
                        {"role": "system", "content": questionnaire_prompt},
                        {"role": "user", "content": "Based on my previous response, ask me the next question to further understand my educational goals and preferences."}
                    ])
                    st.session_state.messages.append({"role": "assistant", "content": ai_message})
                else:
                    st.write("Thank you for answering all the questions. Generating your profile summary...")
                    summary_prompt = f"Based on the following responses, generate a 10-sentence user summary describing the student's name, university, course information, preferences, goals for their time at university - both in and outside the classroom:\n\n"
                    summary_prompt += "\n".join([f"Q{i+1}: {resp}" for i, resp in enumerate(st.session_state.user_responses)])
                    
                    with st.spinner("Generating summary..."):
                        summary = get_ai_response([
                            {"role": "system", "content": "You are an AI assistant that generates concise and accurate user summaries based on educational preferences and goals."},
                            {"role": "user", "content": summary_prompt}
                        ])

                    st.session_state.summary = summary
                    st.write("Summary:", summary)

                    # Save chat and summary to JSON
                    data = {
                        "chat": st.session_state.messages,
                        "summary": summary
                    }
                    with open("user_profile.json", "w") as f:
                        json.dump(data, f, indent=2)

                    st.write("Chat and summary have been saved to user_profile.json")

                    if os.path.exists("user_profile.json"):
                        with open("user_profile.json", "r") as f:
                            data = json.load(f)
                            summary = data["summary"]
                    with st.spinner("Extracting Topics..."):
                        topics = extract_topics_from_answers(topic_extractor_prompt, summary)
                        st.write("Topics:", topics)

                    with st.spinner("Generating Queries..."):
                        queries = generate_queries(query_gen_prompt,str(topics), summary)
                        st.write("Queries:", queries)

    st.write(f"Questions answered: {st.session_state.question_count}/10")

if __name__ == "__main__":
    main()