from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model='gpt-5',
    #temperature=0.1,
    messages=[
        {'role': 'system', 'content': '너는 유치원생이야. 유치원생처럼 답변해 줘'},
        {'role': 'user', 'content': '참새'},
        {'role': 'assistant', 'content': '짹짹'},
        {'role': 'user', 'content': '오리'},
    ]
)

print(response)
print('------------------')
print(response.choices[0].message.content)

