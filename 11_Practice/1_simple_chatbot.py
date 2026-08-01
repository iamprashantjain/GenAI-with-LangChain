from langchain_openai import ChatOpenAI
from dotenv import load_dotenv;load_dotenv()


model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

response = model.invoke("whats the capital of delhi?")
print(response.content)