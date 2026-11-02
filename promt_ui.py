from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt
import streamlit as st
load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash"
)

st.header('Research Assistant')
paper_input= st.selectbox("selected Research paper Name",["Attention is all you Need ","BERT:Pre-training of deep Bidirectional Transformers","GPT-3:Language Models are few-shot learnner"])
style_input= st.selectbox("selected the style of the paper",["Beginner-friendly " , "Technical_friendly","Advance_friendly"])
length_input=st.selectbox("selected the length of the paper",["short(1-2)paragraph length","mediam(5-8)paragraphs","large(10-15)paragraph"])

template=load_prompt('template.json')




if st.button('Summarize'):
    chain= template | model
    result=chain.invoke({

    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})
    
    st.write(result.content)