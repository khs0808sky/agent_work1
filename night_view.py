from glob import glob
import json
from openai import OpenAI
from dotenv import load_dotenv
import os
import base64

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")  # 환경 변수에서 API 키 가져오기
client = OpenAI(api_key=api_key)  # OpenAI 클라이언트의 인스턴스 생성

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    

def analyze_images(image_paths, prompt):
    contents = [{"type": "text", "text": prompt}]
    
    for path in image_paths:
        base64_img = encode_image(path)
        contents.append({
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{base64_img}"}
        })
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": contents}]
    )
    return response.choices[0].message.content

# 비교할 이미지 경로 (서울 vs 도쿄 야경 사진)
images = ["./data/images/night_namsan_tower.jpg", "./data/images/night_dokyo_tower.jpg"]

# 프롬포트 작성
prompt = """
다음 두 장의 이미지는 각각 서울과 도쿄의 야경입니다. 다음 질문들에 답하는 형식으로 마크다운 보고서를 작성해주세요.

- **두 도시의 가장 큰 야경 차이점은 무엇인가요?**
- **불빛의 밀도와 색상에서 어떤 차이가 있나요?**
- **건물들의 배치나 구조는 어떻게 다른가요?**
- **각 도시의 야경이 주는 분위기와 느낌을 설명해주세요.**
- **결론적으로, 두 도시의 야경을 한 문장으로 요약하면?**
"""

# 분석시작
analysis = analyze_images(images, prompt)

# 보고서 저장
with open("./data/seoul_tokyo_night_report.md", "w", encoding="utf-8") as f:
    f.write("# 서울 vs 도쿄 야경 비교 보고서\n\n")
    f.write("## 이미지\n")
    f.write("### 서울 남산타워 야경\n")
    f.write("![Seoul Night](./images/night_namsan_tower.jpg)\n")
    f.write("### 도쿄 도쿄타워 야경\n")
    f.write("![Tokyo Night](./images/night_dokyo_tower.jpg)\n\n")
    f.write(analysis)