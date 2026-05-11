from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

# OpenAI Model
model = ChatOpenAI(model="gpt-4o-mini")

# 1st prompt --> detailed report
template1 = PromptTemplate(
    template="Write a report on {topic} in maximum 2 lines",
    input_variables=['topic']
)

# 2nd prompt --> summary
template2 = PromptTemplate(
    template="Write a 1 line summary on {text}",
    input_variables=['text']
)

parser = StrOutputParser()
#stroutputparser is helpful to make chains otherwise we will be doing it seperatly

chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({'topic':'black_hole'})
print(result)