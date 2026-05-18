from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path=r"D:\AgenticAI\4_Document_loaders",
    glob=".pdf",         #all pdf files
    loader_cls = PyPDFLoader
)


# docs = loader.load()
docs = loader.lazy_load()
print(docs.metadata)
