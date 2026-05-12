from langchain_openai import ChatOpenAI
from dotenv import load_dotenv;load_dotenv()
from typing import TypedDict, Annotated

model = ChatOpenAI(model="gpt-4o-mini")

# Schema
class Review(TypedDict):
    # Exact text copied from the review only
    sentiment_reason: Annotated[
        str,
        "Exact line or phrase from the review responsible for the sentiment. Do not generate or paraphrase."
    ]
    
    sentiment: str
    
    sentiment_score: Annotated[
        float,
        "Sentiment score ranging from -1 (very negative) to 1 (very positive)"
    ]


structured_model = model.with_structured_output(Review)

result = structured_model.invoke(
    "Great service, friendly staff, and excellent experience overall. Highly recommended!"
)

print(result)

import pdb;pdb.set_trace()