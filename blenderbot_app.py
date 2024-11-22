import streamlit as st
from streamlit_chat import message
import requests

# BlenderBot 모델 API URL
API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
API_TOKEN = "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"  # 여기에 Hugging Face API 토큰을 입력하세요
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Streamlit 헤더
st.header("🤖Sunjae's BlenderBot (Demo)")
st.markdown("[Be Original](https://yunwoong.tistory.com/)")

# 대화 상태 저장
if 'generated' not in st.session_state:
    st.session_state['generated'] = [] #챗봇 응답 저장

if 'past' not in st.session_state:
    st.session_state['past'] = [] #사용자 메시지 저장

# API 호출 함수
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# 사용자 입력 폼
with st.form('form', clear_on_submit=True):
    user_input = st.text_input('You: ', '', key='input')
    submitted = st.form_submit_button('Send')

if submitted and user_input:
    # API에 대화 기록과 사용자 입력 전달
    output = query({
        "inputs": {
            "past_user_inputs": st.session_state.past,
            "generated_responses": st.session_state.generated,
            "text": user_input,
        },
        "parameters": {"repetition_penalty": 1.33},
    })

    # 대화 상태 업데이트
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output["generated_text"])

# 대화 출력
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))