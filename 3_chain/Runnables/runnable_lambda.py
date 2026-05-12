from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv; load_dotenv()
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableSequence

model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='generate a 1 line short joke about {topic}',
    input_variables=['topic']
)


prompt2 = PromptTemplate(
    template='explain this joke in 2 words: {joke}',
    input_variables=['joke']
)

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = ({
    'joke':RunnablePassthrough,
    'word_counter':RunnableLambda(lambda x:len(x.split())),
})

final_chain=RunnableSequence(joke_gen_chain, parallel_chain)
result = final_chain.invoke({'topic':'AI'})
print(result)
