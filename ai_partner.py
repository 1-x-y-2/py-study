import streamlit as st
import os
from openai import OpenAI

st.title("DeepSeek-like clone")

system_prompt = "You are a helpful assistant"

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")    

# 初始化对话记录并防止重复初始化
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示之前的对话记录
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Say something"):
    # 显示用户消息
    st.chat_message("user").markdown(prompt)

    # 添加用户消息到对话记录
    st.session_state.messages.append({"role" : "user", "content" : prompt})

    #机器人的消息处理
    with st.chat_message("ai"):
        stream = client.chat.completions.create(
            model="deepseek-v4-flash",
            messages=[
                {"role": "system", "content": system_prompt},
                *st.session_state.messages
            ],
            stream=True,
            reasoning_effort="high",
            extra_body={"thinking": {"type": "enabled"}}
            )

        response = st.write_stream(stream)

    st.session_state.messages.append({"role" : "assistant", "content" : response})


