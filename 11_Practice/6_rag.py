from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
import tempfile
import os
from dotenv import load_dotenv;load_dotenv()


# 1. Load a PDF
pdf_path = input("Enter PDF file path: ")
loader = PyPDFLoader(pdf_path)
documents = loader.load()


# 2. Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = splitter.split_documents(documents)
print(f"Created {len(chunks)} chunks")



# 3. Create vector store
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(chunks, embeddings)


# 4. Create QA chain
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=model,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
    return_source_documents=True
)


# 5. Ask questions
while True:
    question = input("\nAsk about the document (or 'exit'): ")
    if question.lower() == "exit":
        break
    
    result = qa_chain.invoke({"query": question})
    print(f"\nAnswer: {result['result']}")
    
    # Show sources (optional)
    show_sources = input("Show sources? (y/n): ")
    if show_sources.lower() == "y":
        for doc in result["source_documents"]:
            print(f"\nSource: {doc.page_content[:200]}...")