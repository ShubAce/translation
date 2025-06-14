import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

groq_api_key = "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"

from langchain_groq import ChatGroq

model = ChatGroq(model="Gemma2-9b-It",api_key=groq_api_key)

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system","Act as a language translate which translate english to {language}"),
    ("user","{input}")
])

from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

chain = prompt|model|parser
st.title("English Language translator to your wanted language: ")

language = st.text_input("Enter the Language to translate english to: ")
input = st.text_area("Enter text here: ")


st.write(chain.invoke({"language":language,"input":input}))
