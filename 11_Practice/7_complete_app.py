import streamlit as st
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from pydantic import BaseModel, Field
import tempfile
import os
from dotenv import load_dotenv;load_dotenv()


st.set_page_config(page_title="My AI Assistant", layout="wide")
st.title("🤖 My AI Assistant")


# Initialize model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)


# --- Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None


# --- Tab 1: Chat ---
tab1, tab2, tab3 = st.tabs(["💬 Chat", "📄 PDF QA", "📊 Sentiment"])


with tab1:
    st.header("Chat with Memory")
    
    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me anything..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        # Get response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = model.invoke(prompt)
                st.write(response.content)
                st.session_state.messages.append({"role": "assistant", "content": response.content})

with tab2:
    st.header("Ask Questions About Your PDF")
    
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
    
    if uploaded_file is not None:
        if st.button("Process PDF"):
            with st.spinner("Processing..."):
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
                    tmpfile.write(uploaded_file.getvalue())
                    tmp_path = tmpfile.name
                
                loader = PyPDFLoader(tmp_path)
                documents = loader.load()
                
                splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
                chunks = splitter.split_documents(documents)
                
                embeddings = OpenAIEmbeddings()
                st.session_state.vectorstore = Chroma.from_documents(chunks, embeddings)
                
                os.unlink(tmp_path)
                st.success("PDF processed!")
        
        if st.session_state.vectorstore:
            question = st.text_input("Ask a question:")
            if question:
                qa_chain = RetrievalQA.from_chain_type(
                    llm=model,
                    chain_type="stuff",
                    retriever=st.session_state.vectorstore.as_retriever(search_kwargs={"k": 3})
                )
                result = qa_chain.invoke({"query": question})
                st.write("Answer:")
                st.write(result["result"])

with tab3:
    st.header("Sentiment Analyzer")
    
    class SentimentResult(BaseModel):
        sentiment: str = Field(description="positive, negative, or neutral")
        score: float = Field(description="Score from -1 to 1")
    
    structured_model = model.with_structured_output(SentimentResult)
    
    review = st.text_area("Paste a review to analyze:")
    if st.button("Analyze"):
        if review:
            result = structured_model.invoke(f"Analyze: {review}")
            col1, col2 = st.columns(2)
            col1.metric("Sentiment", result.sentiment)
            col2.metric("Score", f"{result.score:.2f}")