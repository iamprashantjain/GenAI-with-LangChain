from langchain_openai import ChatOpenAI
from dotenv import load_dotenv;load_dotenv()
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

# Initialize model
model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    max_completion_tokens=300
)

chat_history = [
    SystemMessage(content="You are a helpful assistant"),
]

# Chat loop
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))

    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    # Invoke model
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))

    # Print response
    print(f"AI: {result.content}")


print(chat_history)




# (venv) D:\AgenticAI\Langchain_Models>py 2_prompts\chatbot.py
# You: hi
# AI: Hello! How can I assist you today?
# You: who created you in short
# AI: I was created by OpenAI, an artificial intelligence research organization. If you have any specific questions about my capabilities or how I work, feel free to ask!
# You: exit
# Chat ended.
# [SystemMessage(content='You are a helpful assistant', additional_kwargs={}, response_metadata={}), HumanMessage(content='hi', additional_kwargs={}, response_metadata={}), AIMessage(content='Hello! How can I assist you today?', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]), HumanMessage(content='who created you in short', additional_kwargs={}, response_metadata={}), AIMessage(content='I was created by OpenAI, an artificial intelligence research organization. If you have any specific questions about my capabilities or how I work, feel free to ask!', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]), HumanMessage(content='exit', additional_kwargs={}, response_metadata={})]

# (venv) D:\AgenticAI\Langchain_Models>
