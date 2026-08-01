from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

template = ChatPromptTemplate.from_messages([
    ("system", "You are a {role} expert. Respond in a {tone} tone."),
    ("human", "{question}")
])

chain = template | model

while True:
    question = input("What's your question? ")
    if question.lower() == "exit":
        break

    role = input("Role (e.g., scientist, teacher, chef): ")
    tone = input("Tone (e.g., professional, casual, humorous): ")

    response = chain.invoke({
        "role": role,
        "tone": tone,
        "question": question
    })

    print(response.content)
    print("-" * 50)