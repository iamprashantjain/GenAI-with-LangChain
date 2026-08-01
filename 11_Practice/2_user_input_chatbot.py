from langchain_openai import ChatOpenAI
from dotenv import load_dotenv;load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

print("Chatbot: Hello! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    response = model.invoke(user_input)
    print(f"AI: {response.content}")