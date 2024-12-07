import streamlit as st

#from dotenv import load_dotenv
#load_dotenv()

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

st.title("최진호 바보")
subject=st.text_input("진호가 동기부여 받고 싶은 내용을 입력해주세요")
st.write("진호의 동기부여 : " + subject)

if st.button("누르면 바보"):
    with st.spinner("진호 올라잇중 ..."):
        result = chat_model.invoke(subject + "에 대한 동기부여가 되는 글을 작성해줘")
        st.write(result.content)