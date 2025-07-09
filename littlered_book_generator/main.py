import streamlit as st


from utils import  generate_little_red_book

st.header("小红书爆款AI写作助手 ✏️")

with st.sidebar:
    api_key=st.text_input("请输入DeepSeek APi密钥:", type="password")
    st.markdown("[获取DeepSeek API密钥](https://platform.deepseek.com)")

theme=st.text_input("为你的爆款想一个主题吧")
submit=st.button("提交并开始写作！")

if submit and not theme:
    st.info("想一个主题啊！！！！")
    st.stop()
if submit and not api_key:
    st.info("没有api想要白嫖啊？？？")
    st.stop()

if submit:
    with st.spinner("奴才在加载了~"):
        result= generate_little_red_book(theme, api_key)
    st.divider()
    left_colum,right_colum=st.columns([1,2])
    with left_colum:
        st.markdown("#### 小红书标题1")
        st.write(result.tittles[0])
        st.markdown("#### 小红书标题2")
        st.write(result.tittles[1])
        st.markdown("#### 小红书标题3")
        st.write(result.tittles[2])
        st.markdown("#### 小红书标题4")
        st.write(result.tittles[3])
        st.markdown("#### 小红书标题5")
        st.write(result.tittles[4])
    with right_colum:
        st.markdown("#### 小红书正文")
        st.write(result.content)