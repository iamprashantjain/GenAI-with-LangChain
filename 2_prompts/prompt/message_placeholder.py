from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv;load_dotenv()

# Chat template
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful customer service agent"),
    
    MessagesPlaceholder(variable_name="chat_history"),
    
    ("human", "{query}")
])

# Load chat history
chat_history = []

with open(r"D:\AgenticAI\Langchain_Models\2_prompts\chat_history.txt", "r") as f:
    lines = f.readlines()

# Convert text lines into LangChain message objects
for line in lines:

    line = line.strip()

    # Convert text lines into LangChain message objects
for line in lines:

    line = line.strip()

    if line.startswith("HumanMessage"):
        
        content = line.split('content="')[1].split('")')[0]

        chat_history.append(
            HumanMessage(content=content)
        )

    elif line.startswith("AIMessage"):

        content = line.split('content="')[1].split('")')[0]

        chat_history.append(
            AIMessage(content=content)
        )

# Print loaded history
print(chat_history)

# Create prompt
prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "Where is my refund?"
})

# Print final formatted prompt
print(prompt)