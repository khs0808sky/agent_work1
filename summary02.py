from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

def summarize_txt(file_path: str):
    client = OpenAI(api_key=api_key)

    with open(file_path, 'r', encoding='utf-8') as f:
        txt = f.read()
    
    system_prompt = f'''
    너는 다음 글을 요약하는 봇이다. 아래 글을 읽고, 이 글을 처음 읽는 사람도 이해할 수 있게 요약해줘
    한 줄에 너무 길게 쓰지 말고 적당히 엔터를 쳐줘
    =========== 이하 텍스트 ============
    {txt}
    '''

    print(system_prompt)
    print('========================')

    response = client.chat.completions.create(
        model='gpt-5',
        messages=[
            {"role": "system", "content": system_prompt}
        ]
    )

    return response.choices[0].message.content

if __name__ == '__main__':
    file_path = './data/K-CON+LA+2022로+본+미국+내+K-Pop+현황+[미국22-06호].txt'

    summary = summarize_txt(file_path)
    print(summary)

    with open('./output/summary02.txt', 'w', encoding='utf-8') as f:
        f.write(summary)