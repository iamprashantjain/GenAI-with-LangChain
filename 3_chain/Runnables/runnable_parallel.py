from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv; load_dotenv()
from langchain_core.runnables import RunnableSequence, RunnableParallel

model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = 'generate a 1 line short tweet about {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'generate a linkedin post in short about {topic}',
    input_variables = ['topic']
)

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin_post': RunnableSequence(prompt2, model, parser),
})

result = parallel_chain.invoke({'topic':'AI'})
print(result)


import pdb;pdb.set_trace()