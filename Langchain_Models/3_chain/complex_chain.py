from langchain_openai import ChatOpenAI
from dotenv import load_dotenv;load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt1 = PromptTemplate(
    template="""
    Generate exactly 2 Google reviews about {topic}.

    Rules:
    - Each review must be on a separate line
    - Each review should be only 1 line
    - Do not add numbering
    - Do not add explanations
    """,

    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="""
    For each review below, generate a sentiment score between -1 and 1.

    Return output in this format:
    Review: <review>
    Score: <score>

    Reviews:
    {text}
    """,

    input_variables=['text']
)

model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

chain = (
    prompt1
    | model
    | parser
    | (lambda x: {"text": x})
    | prompt2
    | model
    | parser
)

result = chain.invoke({'topic': 'Fogo de Chão'})

# (Pdb) result
# 'Review: The steak selection at Fogo de Chão is outstanding, with perfectly cooked meats that are full of flavor.  \nScore: 1\n\nReview: Fogo de Chão offers an incredible dining experience with attentive service and a vibrant atmosphere.  \nScore: 1'

import pdb;pdb.set_trace()