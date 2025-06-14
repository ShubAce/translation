import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "GenAIAPIWithOPENAI"
groq_api_key = "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"

from langchain_groq import ChatGroq

model = ChatGroq(model="qwen-qwq-32b",api_key=groq_api_key)

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system","Act as a helpfull assistant and give best answers to the query asked to you"),
    ("user","{input}")
])

from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

chain = prompt|model|parser
st.title("Small scale LLM model for Keenuu ")

input = st.text_area("Enter your query keenu: ")

if st.button("genrate"):
    st.write(chain.invoke({"input":input}))
