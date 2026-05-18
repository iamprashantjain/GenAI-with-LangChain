from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv;load_dotenv()

model=ChatOpenAI(model='gpt-4o-mini')
parser=StrOutputParser()

prompt=PromptTemplate(
    template='write a summary for following {text}',
    input_variables=['text']
)

loader = PyPDFLoader(r"D:\AgenticAI\4_Document_loaders\dl-curriculum.pdf")
docs = loader.load()

print(docs)
# print(docs[0])
# print(docs[0].page_content)
# print(docs[0].metadata)

# chain = prompt | model | parser
# result = chain.invoke({'text':docs[0].page_content})
# print(result)