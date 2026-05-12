from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

# OpenAI Model
model = ChatOpenAI(model="gpt-4o-mini")


class Person(BaseModel):
    name: str = Field(description='Name of the person')

    age: int = Field(
        gt=18,
        description='Age of the person'
    )

    city: str = Field(
        description='City where the person lives'
    )


parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="""
    Generate name, age, and city of a fictional {place} person.

    {format_instructions}
    """,

    input_variables=['place'],

    partial_variables={
        'format_instructions': parser.get_format_instructions()
    }
)

prompt = template.invoke({'place': 'Indian'})
print(prompt)

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result) 


chain = template | model | parser
final_result = chain.invoke({'place': 'malaysian'})
print(final_result)