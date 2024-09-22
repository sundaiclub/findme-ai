import streamlit as st
from openai import OpenAI
import json
import os
from src.topic_extractor import extract_topics_from_answers
from src.query_generator import generate_queries
from src.prompts import query_gen_prompt, topic_extractor_prompt, pathway_creator
from src.brave_search import brave_search_and_scrape
from src.path_generator import create_path


# Set up OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load questionnaire prompt
with open("streamlit-app/questionnaire-prompt.txt", "r") as f:
    questionnaire_prompt = f.read()

# Set page config
st.set_page_config(page_title="FindMe.AI", page_icon="🎓", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        color: black;
    }
    .stTextArea > div > div > textarea {
        background-color: #ffffff;
        color: black;
        border: 1px solid #4CAF50;
        border-radius: 4px;
        padding: 10px;
        font-size: 16px;
        min-height: 100px;
        resize: vertical;
    }
    .stProgress > div > div > div > div {
        background-color: #4CAF50;
    }
    .stAlert {
        background-color: #E8F0FE;
        color: black;
    }
    h1, h2, h3, p {
        color: black;
    }
    .question-container {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .reportview-container {
        background-color: white;
    }
    .stButton > button {
        background-color: #2E8B57;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 0.5rem 1rem;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #3CB371;
    }
    </style>
    """, unsafe_allow_html=True)

def get_ai_response(messages):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error in AI response: {str(e)}")
        return None

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.question_count = 0
        st.session_state.user_responses = []
        st.session_state.current_question = ""
        st.session_state.show_next_question = True
        st.session_state.summary = ""

def main():
    st.title("🎓 FindMe.AI")
    st.write("Answer 10 questions to generate your educational profile.")

    initialize_session_state()

    # Progress bar
    progress = st.progress(st.session_state.question_count / 10)

    if st.session_state.question_count < 10:
        col1, col2 = st.columns([2, 1])

        with col1:
            if st.session_state.show_next_question:
                with st.spinner("Generating next question..."):
                    if len(st.session_state.messages) == 0:
                        ai_message = get_ai_response([
                            {"role": "system", "content": questionnaire_prompt},
                            {"role": "user", "content": "Ask me the first question to understand my educational goals and preferences."}
                        ])
                    else:
                        ai_message = get_ai_response(st.session_state.messages + [
                            {"role": "system", "content": questionnaire_prompt},
                            {"role": "user", "content": "Based on my previous response, ask me the next question to further understand my educational goals and preferences."}
                        ])
                    if ai_message:
                        st.session_state.current_question = ai_message
                        st.session_state.show_next_question = False
                    else:
                        st.error("Failed to generate the next question. Please try again.")
                        return

            st.markdown(f"<div class='question-container'>{st.session_state.current_question}</div>", unsafe_allow_html=True)

            # Create a form for user input
            with st.form(key=f"user_input_form_{st.session_state.question_count}"):
                user_input = st.text_area("Your response:", key=f"user_input_{st.session_state.question_count}", height=150)
                submit_button = st.form_submit_button("Submit ➤")

            if submit_button and user_input:
                with st.spinner("Processing your response..."):
                    # Add user response to messages and user_responses
                    st.session_state.messages.append({"role": "assistant", "content": st.session_state.current_question})
                    st.session_state.messages.append({"role": "user", "content": user_input})
                    st.session_state.user_responses.append(user_input)
                    st.session_state.question_count += 1
                    progress.progress(st.session_state.question_count / 10)

                    if st.session_state.question_count < 10:
                        st.session_state.show_next_question = True
                    else:
                        st.balloons()
                        st.success("Thank you for answering all the questions. Generating your profile summary...")
                        summary_prompt = f"Based on the following responses, generate a 10-sentence user summary describing the student's name, university, course information, preferences, goals for their time at university - both in and outside the classroom:\n\n"
                        summary_prompt += "\n".join([f"Q{i+1}: {resp}" for i, resp in enumerate(st.session_state.user_responses)])
                        
                        summary = get_ai_response([
                            {"role": "system", "content": "You are an AI assistant that generates concise and accurate user summaries based on educational preferences and goals."},
                            {"role": "user", "content": summary_prompt}
                        ])

                        if summary:
                            st.session_state.summary = summary

                            # Save chat and summary to JSON
                            data = {
                                "chat": st.session_state.messages,
                                "summary": summary
                            }
                            with open("user_profile.json", "w") as f:
                                json.dump(data, f, indent=2)

                            st.info("Chat and summary have been saved to user_profile.json")
                        else:
                            st.error("Failed to generate the summary. Please try again.")

                st.rerun()

        with col2:
            st.subheader("Your Progress")
            st.write(f"Questions answered: {st.session_state.question_count}/10")
            
    else:
        st.success("Profile Generation Complete!")
        st.subheader("Your Educational Profile Summary")
        if os.path.exists("user_profile.json"):
            with open("user_profile.json", "r") as f:
                data = json.load(f)
                summary = data["summary"]
        with st.spinner("Extracting Topics..."):
            topics = extract_topics_from_answers(topic_extractor_prompt, summary)

        with st.spinner("Generating Queries..."):
            queries = generate_queries(query_gen_prompt,str(topics), summary)

        with st.spinner("Retrieving Information..."):
            info = {}
            for k, v in queries.items():
                info[k] = [brave_search_and_scrape(q) for q in v]
        
        with st.spinner("Creating Pathways..."):
            pathways = {}
            for k, v in info.items():
                content = ''
                for res in v:
                    for k_, v_ in res.items():
                        content += f"{k_}: {v_}\n"
                pathways[k] = create_path(pathway_creator, k, summary, content)
        for k, v in pathways.items():
            with st.expander(k):
                st.markdown(f"<div>{v}</div>", unsafe_allow_html=True)

        if st.button("Start Over"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

if __name__ == "__main__":
    main()