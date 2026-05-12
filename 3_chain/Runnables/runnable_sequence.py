from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv; load_dotenv()
from langchain_core.runnables import RunnableSequence

# Runnable 1: Generate a joke
prompt1 = PromptTemplate(
    template="write a 1 line joke about {topic}",
    input_variables=['topic']
)

model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

# Runnable 2: Explain the joke
prompt2 = PromptTemplate(
    template="explain the following joke in 2 words: {text}",
    input_variables=['text']
)

# Create the chain
chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

# Invoke
result = chain.invoke({'topic': 'AI'})
print(result)