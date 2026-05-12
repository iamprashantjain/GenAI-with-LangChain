from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv;load_dotenv()
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=32)

docs = [
    "Virat Kohli is an Indian cricketer and former captain known for his aggressive batting and records.",
    "Pat Cummins is an Australian cricketer and current captain known for his pace bowling and leadership.",
    "Joe Root is an English cricketer and former captain known for his classic batting technique.",
    "Kane Williamson is a New Zealand cricketer known for his calm demeanor and elegant batting.",
    "Babur Azam is a Pakistani cricketer and current captain known for his stylish batting and consistency."
]

query = "tell me about virat kohli"


doc_embeddings = embedding.embed_documents(docs)
query_embeddings = embedding.embed_query(query)

scores = cosine_similarity([query_embeddings], doc_embeddings)[0]
index,score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(query)
print(docs[index])
print(f"similarity score is: {score}")






