from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv;load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini",temperature=0.7)

template = ChatPromptTemplate([
    ("system","you are a helpful assistant"),
    MessagesPlaceholder(variable_name="history"),
    ("human","{input}")
])

chain = template | model

chat_history = []

print("I remmember conversation history, type 'exit' to exit")

while True:
    user_input = input("whats your question")
    if user_input.lower() == "exit":
        break

    response = chain.invoke({
        "input":user_input,
        "history":chat_history
    })


    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=response.content))

    print(f"AI: {response.content}")
    print(f"(Memory size: {len(chat_history)} messages)")
    print("-" * 50)