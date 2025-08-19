from openai import OpenAI

api_key = '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'

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model='gpt-4o',
    temperature=0.8,
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistent'},
        {'role': 'user', 'content': '2022년 월드컵 우승 팀은 어디야?'}
    ]
)

print(response)
print('------------------')
print(response.choices[0].message.content)

