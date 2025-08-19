# agent_work1

## 📅 목차

- [2025-08-19](#2025-08-19)

<br><br><br>

---

## **2025-08-19**

---

### 1) GPT API 시작하기

* **API란?**
  응용 프로그램에서 GPT 모델을 불러와서 질문 → 응답을 자동으로 처리할 수 있도록 해주는 인터페이스.
* **시작 절차**:

  1. **API 키 발급**:

     * [OpenAI 계정](https://platform.openai.com/)에서 로그인 후 → 개인용 API 키 생성.
     * 이 키는 비밀번호처럼 중요한 정보이므로 노출되면 안 됨.
  2. **환경 설정**:

     * Python 예시:

       ```python
       from openai import OpenAI
       client = OpenAI(api_key="YOUR_API_KEY")

       response = client.chat.completions.create(
           model="gpt-4o-mini",
           messages=[{"role": "user", "content": "안녕하세요 GPT"}]
       )

       print(response.choices[0].message.content)
       ```
     * `model`에는 사용할 모델 이름 지정. (`gpt-4o`, `gpt-4o-mini`, `gpt-3.5-turbo` 등)
  3. **질문 & 답변 구조**:

     * `messages` 필드 안에 role과 content로 대화 맥락 전달.

       * `system`: 모델에게 역할/성격 지시.
       * `user`: 사용자 입력.
       * `assistant`: 모델의 응답.
* **활용 예시**:

  * 챗봇, 문서 요약기, 번역기, 코드 보조 도구 등.

---

### 2) OpenAI의 API 키로 질문하고 답변받기

* **API 키 사용 원리**:

  * OpenAI 서버로 요청을 보낼 때 인증 토큰처럼 사용됨.
  * 올바른 키가 있어야 모델이 응답을 반환.
* **중요 포인트**:

  * 키는 `.env` 같은 환경 변수에 저장 → 코드에 직접 노출하지 않는 게 안전.
  * 예시 (환경 변수 활용):

    ```python
    import os
    from openai import OpenAI

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    ```
* **응답 구조**:

  * JSON 형식으로 반환되며, `response.choices[0].message.content` 부분이 실제 답변.
  * 응답에는 토큰 사용량(`usage`)도 포함됨 → 비용 계산 가능.

---

### 3) Few-Shot Learning

* **정의**:
  모델이 \*\*적은 수의 예제(샘플)\*\*만 보고도 새로운 문제를 풀 수 있도록 하는 학습 방식.
  (반대: Zero-Shot → 예제 없이 해결, Many-Shot → 많은 예제 제공)
* **원리**:

  * GPT 같은 대규모 언어 모델은 사전 학습 시 이미 일반적인 패턴을 습득.
  * Prompt 안에 몇 개의 예시를 제공하면, 모델은 그 형식을 일반화해 새로운 입력에 적용.
* **예시**:

  ```text
  Q: 2+3은?
  A: 5
  Q: 4+7은?
  A: 11
  Q: 9+8은?
  A:
  ```

  → 모델이 "A: 17"로 답하도록 유도.
* **장점**:

  * 별도 학습(파인튜닝) 없이 원하는 태스크에 빠르게 적응.
  * 소량의 데이터로도 특정 포맷/스타일을 학습.
* **단점**:

  * Prompt 길이에 제약 있음(예시 많이 넣기 어려움).
  * 예제 선택에 따라 성능이 크게 달라짐.

---

📅[목차로 돌아가기](#-목차)

---
