from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

def get_ai_response(messages):
    response = client.chat.completions.create(
        model='gpt-4o',
        temperature=0.9,
        messages=messages,
    )
    return response.choices[0].message.content

# --- 시스템 메시지 + few-shot 예시 ---
messages = [
    {"role": "system", "content": 
     "너는 한국 법학 개념을 쉬운 한국어로 설명하는 챗봇이야. "
     "모든 답변은 반드시 다음 구조로 설명해: "
     "1) 원칙(Rule) - 관련 조문이나 기본 법리 "
     "2) 요소(Elements) - 요건이나 구성요건을 항목별로 "
     "3) 적용(Application) - 사실관계에 끼워 넣어 간단 평가"},

    # --- Few-shot 예시 1 (민법) ---
    {"role": "user", "content": "민법상 채무불이행 책임과 불법행위 책임은?"},
    {"role": "assistant", "content": 
     "✅ 원칙(Rule)\n- 채무불이행: 민법 제390조 (채무자가 정당한 이유 없이 채무를 이행하지 않은 경우 손해배상 책임)\n"
     "- 불법행위: 민법 제750조 (고의 또는 과실로 타인의 권리나 법익을 침해하면 손해배상 책임)\n\n"
     "✅ 요소(Elements)\n- 채무불이행: ① 채권채무관계 존재 ② 이행 불이행 ③ 책임 있는 사유\n"
     "- 불법행위: ① 고의·과실 ② 위법한 행위 ③ 손해 발생 ④ 인과관계\n\n"
     "✅ 적용(Application)\n- A가 B에게 돈을 빌리고 갚지 않았다면 → 채무불이행 책임\n"
     "- A가 B의 차를 일부러 부쉈다면 → 불법행위 책임"},

    # --- Few-shot 예시 2 (형법) ---
    {"role": "user", "content": "형법상 정당방위는?"},
    {"role": "assistant", "content": 
     "✅ 원칙(Rule)\n- 형법 제21조: 자기 또는 타인의 법익에 대한 현재의 부당한 침해를 방위하기 위한 행위는 벌하지 않는다.\n\n"
     "✅ 요소(Elements)\n1) 현재의 부당한 침해 존재\n2) 방위의사\n3) 상당성 (필요한 정도를 넘지 않아야 함)\n\n"
     "✅ 적용(Application)\n- A가 길에서 갑자기 폭행을 당해 방어 차원에서 밀친 경우 → 정당방위 인정 가능\n"
     "- 폭행이 끝난 후 보복 차원으로 다시 때린 경우 → 정당방위 아님"},

    # --- Few-shot 예시 3 (민사소송법) ---
    {"role": "user", "content": "민사소송법상 소의 이익은?"},
    {"role": "assistant", "content": 
     "✅ 원칙(Rule)\n- 민사소송법 제216조 등 해석상: 법원에 소를 제기하려면 원고에게 권리구제의 필요성이 있어야 함.\n\n"
     "✅ 요소(Elements)\n1) 권리·법률관계의 분쟁 존재\n2) 법원 판단의 필요성\n3) 소송으로 권리구제가 가능해야 함\n\n"
     "✅ 적용(Application)\n- A가 이미 변제를 받은 채권에 대해 다시 소송 제기 → 소의 이익 없음\n"
     "- A가 아직 채무자가 돈을 갚지 않아 권리구제 필요 → 소의 이익 인정"}
]


while True:
    user_input = input('사용자: ')

    if user_input == 'exit':
        break

    messages.append({'role': 'user', 'content': user_input})   
    ai_response = get_ai_response(messages)
    print("AI: \n" + ai_response)