from langchain_openai import ChatOpenAI
from dotenv import load_dotenv;load_dotenv()
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

# Initialize model
model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    max_completion_tokens=300
)

# Streamlit UI
st.set_page_config(page_title="Research Tool")

st.header("Research Paper Summarizer")

# Research paper selection
paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners"
    ]
)

# Explanation style
style_input = st.selectbox(
    "Select Explanation Type",
    [
        "Beginner Friendly",
        "Technical"
    ]
)

# Explanation length
length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 lines)",
        "Medium (1-2 paragraphs)",
        "Detailed(3 Paragraphs)"
    ]
)


#load template
template = load_prompt(r'D:\AgenticAI\Langchain_Models\2_prompts\template.json')

# Button action
if st.button("Summarize"):

    chain = template | model
    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })

    st.subheader("Summary")
    st.write(result.content)