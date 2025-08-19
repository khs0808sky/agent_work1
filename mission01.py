from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

SYSTEM_MSG = {
    "role": "system",
    "content": (
        "너는 한국 법학 연구가야. "
        "항상 한국 법 개념을 쉽게 체계적으로 설명해야 해."
        "출력은 반드시:\n"
        "1)원칙(Rule)\n2)요소(Elements)\n3)적용(Application)\n"
        "법조문 번호나 학설·판례는 간단히만 언급해."
    )
}

FEW_SHOTS = [
    {
        "role": "user",
        "content": "민법상 불법행위 책임이 뭐예요?"
    },
    {
        "role": "assistant",
        "content": (
            "1)원칙: 민법 제750조는 고의, 과실로 타인에게 손해를 가하면 배상 책임을 진다고 규정합니다.\n"
            "2)요건: \n"
            "   - 가해자의 위법한 행위\n"
            "   - 고의 또는 과실\n"
            "   - 손해 발생\n"
            "   - 행위와 손해 사이 인과관계\n"
            "3)적용: 예를 들어 타인의 물건을 부주의로 파손 되었다면, 과실, 손해, 인과관계가 인정되어 손해배상 책임이 발생합니다.\n"
        )
    }
]

def get_ai_response(messages):
    response = client.chat.completions.create(
        model='gpt-4o',
        temperature=0.9,
        messages=messages,
    )
    return response.choices[0].message.content


def main():
    base = [SYSTEM_MSG] + FEW_SHOTS[:]
    messages = base[:]
    print("한국 법 연구 시작. 'exit':종료")
    while True:
        u = input("사용자:").strip()
        if u.lower() == 'exit':
            break

        messages.append({"role": "user", "content": u})
        ai_message = get_ai_response(messages)
        print("AI: ", ai_message)
        messages.append({"role": "assistant", "content": ai_message})


if __name__ == "__main__":
    main()