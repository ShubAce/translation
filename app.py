import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import re
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
st.title("Small scale LLM model  ")

input = st.text_area("Enter your query: ")

if st.button("Generate"):
    with st.spinner("Thinking..."):
        raw_output = chain.invoke({"input": input})
        
        # Extract <think> part (if exists)
        think_match = re.search(r"<think>(.*?)</think>", raw_output, re.DOTALL)
        thinking_text = think_match.group(1).strip() if think_match else "No internal thoughts found."
        
        # Remove <think> section from final output
        clean_output = re.sub(r"<think>.*?</think>", "", raw_output, flags=re.DOTALL).strip()
        
        st.success("Answer:")
        st.write(clean_output)
        
        # Add checkbox to optionally show the "thinking"
        if st.checkbox("🤔 Show what the model was thinking"):
            st.info(thinking_text)
