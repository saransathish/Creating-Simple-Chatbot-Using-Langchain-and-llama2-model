from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st


st.title("SmartBot")
input_txt = st.text_input("please enter your queries...")


prompt = ChatPromptTemplate.from_messages(
    [("system" , "you are the helpful AI assistant. Your name is SmartBot") , 
     ("user" , "user query :{query}")
    ])

llm = Ollama(model = "llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_txt:
    st.write(chain.invoke({"query":input_txt}))