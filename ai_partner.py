import streamlit as st
import os
from openai import OpenAI


# 配置 Streamlit 页面
st.set_page_config(
    page_title="AI伴侣",
    page_icon="😘",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': 'https://www.extremelycoolapp.com/bug',
        'About': '# This is a header. This is an *extremely* cool app!'
    }
)

# 设置页面标题和 Logo
st.title("AI伴侣")
st.logo("resource/logo.png")

# 设定 AI 的角色
system_prompt = "你是我的女朋友，可爱且超级喜欢我"

# 初始化当前会话的聊天记录
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示历史消息
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# 创建 DeepSeek 客户端
prompt = st.chat_input("Say something")

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

if prompt:
    # 显示并保存用户消息
    st.chat_message("user").write(prompt)
    print("提示词", prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # 请求模型生成回复
    response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
    )

    answer = response.choices[0].message.content
    
    print("LLM返回的结果:", answer)

    # 显示并保存 AI 回复
    st.chat_message("assistant").write(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
