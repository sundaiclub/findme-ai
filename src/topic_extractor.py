from openai_api import OpenAIApi

openai_api = OpenAIApi()

prompt = """
Based the following questions and answers, extract the topics that the user is interested in and is looking for.

Questions and answers:
{questionnaire}


Respond in the following format:


```json
[topic_1, topic_2, ...]
```

Output:
"""



def extract_topics_from_answers(prompt, questionaire):

    
    prompt = prompt.format(questionnaire=questionaire)
    response = openai_api.get_completion(prompt)
    return response


questions = """What are your primary goals for joining a community or club?
a) Socializing and meeting new people
b) Expanding professional networks
c) Developing new skills or hobbies
d) Enhancing academic or career knowledge
Ans: a

Which areas of personal or professional development are most important to you?
a) Leadership and communication skills
b) Academic achievements and knowledge sharing
c) Professional mentorship and career advancement
d) Creative or artistic expression
Ans: b

What types of activities or events interest you the most?
a) Social mixers and networking events
b) Workshops and skill-building sessions
c) Study groups or academic clubs
d) Community service and volunteering
Ans: a

How much time are you willing to commit to community involvement?
a) Once a week
b) A few times a month
c) Occasional or one-time events
d) Open to regular and long-term commitments
Ans: c

What kinds of people do you hope to connect with in these communities?
a) People with similar academic or professional interests
b) Mentors or professionals in your field
c) Peers with shared hobbies or creative passions
d) A diverse group for broad social connections
Ans: d
"""


print(extract_topics_from_answers(prompt,questions))

    


