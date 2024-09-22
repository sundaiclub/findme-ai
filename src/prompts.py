

query_gen_prompt = """
"Given the user's location , university, and interests in {interests}, generate a set of detailed and relevant search queries to discover the following:

Bio of the user.
{summary}

Events happening in or near the specified location that align with the user's interests.
Clubs or communities in the area that match the user's preferences.
Courses or educational programs that cater to the user's interests in this location.
Make sure the queries cover a range of platforms, such as event listings, local meetups, educational institutions, and social clubs.

Generate only 2 queries per category.

Give the output in the following format:

```json
{{"events" : [query_1, query_2, ...], "clubs" : [query_1, query_2, ...], "courses" : [query_1, query_2, ...]}}
```

Output:
"""

topic_extractor_prompt = """
You are provided with a set of questions and answers that reflect a user's inquiries, preferences, and interests. Your task is to thoroughly analyze the content of the questions and responses to extract the key topics the user is actively seeking information on or has expressed interest in.

Consider each question and its corresponding answer carefully. Identify both explicit topics (directly mentioned) and implicit topics (those inferred from context, patterns, or repeated themes across multiple questions). Ensure that the topics are broad enough to capture the user’s general areas of interest, but specific enough to provide meaningful insights.

For example:

If the questions revolve around coding languages or frameworks, the topics might include “Python,” “Web Development,” or “Machine Learning.”
If the questions pertain to a specific industry or problem, the topics might include “Healthcare AI,” “Data Privacy,” or “Automation.”
The topics should reflect what the user is trying to learn, explore, or understand better. Please list them in a clear, concise manner, without any extra commentary.

Questions and Answers: {questionnaire}

Format your response in the following structure:
```json
[ "topic_1", "topic_2", ... ]
```
Ensure that the topics are presented as a JSON array with each item in quotation marks.

Output:
"""