from langchain_openai import ChatOpenAI
from dotenv import load_dotenv; load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate(
    template = "generate 2 interesting facts about {topic}",  # Fixed typo
    input_variables = ['topic']
)

model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

# "|" is called LCEL (langchain expression language)
chain = prompt | model | parser
chain.get_graph().print_ascii()

result = chain.invoke({'topic': 'cricket'})
print(result)