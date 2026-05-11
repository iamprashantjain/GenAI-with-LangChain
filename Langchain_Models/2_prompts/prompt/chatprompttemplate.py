# from langchain_core.prompts import ChatPromptTemplate
# from dotenv import load_dotenv;load_dotenv()

# from langchain_core.messages import (
#     SystemMessage,
#     HumanMessage
# )


# # Create chat template
# chat_template = ChatPromptTemplate.from_messages([
#     SystemMessage(content="You are a helpful {domain} expert"),
#     HumanMessage(content="Explain in simple terms, what is {topic}")
# ])

# # Invoke template
# prompt = chat_template.invoke({
#     "domain": "cricket",
#     "topic": "doosra"
# })

# # Print formatted messages
# print(prompt)


# =============

from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

# FIX: use tuple format instead of SystemMessage/HumanMessage objects
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {domain} expert"),
    ("human", "Explain in simple terms, what is {topic}")
])

# Invoke template
prompt = chat_template.invoke({
    "domain": "cricket",
    "topic": "doosra"
})

# Print formatted messages
print(prompt)