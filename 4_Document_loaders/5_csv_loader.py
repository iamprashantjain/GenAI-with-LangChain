from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path=r"D:\AgenticAI\4_Document_loaders\Social_Network_Ads.csv")
docs = loader.load()

print(len(docs))

