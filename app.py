import os
from apikey import apikey
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain , SimpleSequentialChain
import streamlit as st

os.environ['OPENAI_API_KEY'] = apikey


st.title('Poem GPT')
prompt = st.text_input('Give your prompt')
#Prompt template
title_template = PromptTemplate(
    input_variables = ['topic'],
    template= 'Wrie me a poem on {topic}'
)

#LLM

llm = OpenAI(
temperature=0,
model_name="gpt-3.5-turbo",
frequency_penalty = 0.5,
max_tokens=500,
streaming=True,
)

title_chain = LLMChain(llm=llm , prompt = title_template , verbose = True)
if prompt:
    response =title_chain.run(topic=prompt)
    st.write(response)