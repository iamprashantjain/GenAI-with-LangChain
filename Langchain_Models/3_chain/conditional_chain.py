from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv; load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal


model = ChatOpenAI(model="gpt-4o-mini")
parser1 = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template = "classify the sentiment of the following feedback into positive or negative \n {feedback} \n {format_instructions}",
    input_variables = ['feedback'],
    partial_variables = {'format_instructions': parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template = "write an appropriate response to this positive feedback \n {feedback}",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template = "write an appropriate response to this negative feedback \n {feedback}",
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x: x['sentiment'] == 'positive', prompt2 | model | parser1),
    (lambda x: x['sentiment'] == 'negative', prompt3 | model | parser1),
    RunnableLambda(lambda x: "No sentiment found")
)

# Fix: Transform Feedback object to dict before passing to branch_chain
chain = classifier_chain | RunnableLambda(lambda fb: {'sentiment': fb.sentiment, 'feedback': fb.feedback}) | branch_chain

result = chain.invoke({'feedback':'this is terrible phone'})
print(result)