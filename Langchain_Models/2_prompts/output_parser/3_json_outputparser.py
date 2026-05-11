from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# OpenAI Model
model = ChatOpenAI(model="gpt-4o-mini")

parser = JsonOutputParser()

template = PromptTemplate(
    template="""
    Give me name, age & city of a fictional person.

    {format_instructions}
    """,

    input_variables=[],

    partial_variables={
        'format_instructions': parser.get_format_instructions()
    }
)

prompt = template.format()

print(prompt)