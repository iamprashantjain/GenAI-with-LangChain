from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv;load_dotenv()

# Initialize model
model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    max_completion_tokens=300
)

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about langchain")
]

result = model.invoke((messages))
messages.append(AIMessage(content=result.content))

print(messages)