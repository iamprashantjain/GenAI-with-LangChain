from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv; load_dotenv()
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='generate a 1 line short joke {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='explain this joke in 2 words: {joke}',
    input_variables=['joke']
)

# Chain 1: Generate tweet
tweet_gen_chain = prompt1 | model | parser

# Chain 2: Parallel processing - take the tweet and do multiple things with it
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),  # Pass through the tweet as is
    'explanation': prompt2 | model | parser  # Generate explanation
})

# Final chain: Generate tweet first, then process it in parallel
final_chain = tweet_gen_chain | parallel_chain

# Invoke with topic
result = final_chain.invoke({'topic': 'artificial intelligence'})

print("JOKE:")
print(result['joke'])
print("\nEXPLANATION:")
print(result['explanation'])

# Debugger (optional)
import pdb; pdb.set_trace()