from langchain_openai import ChatOpenAI
from dotenv import load_dotenv;load_dotenv()
from pydantic import BaseModel, Field


model = ChatOpenAI(model="gpt-4o-mini")

# Schema
class Review(BaseModel):
    key_themes: list[str] = Field(
        description="All key themes in broader way discussed in the review"
    )

    sentiment_reason: list[str] = Field(
        description="Exact phrases from the review responsible for the sentiment. Do not paraphrase or generate new text."
    )

    sentiment_score: list[float] = Field(
        description="Sentiment score for the review ranging between -1 and 1"
    )


structured_model = model.with_structured_output(Review)

result = structured_model.invoke(
    "Great service, friendly staff, and excellent experience overall. Highly recommended!"
)

print(result)

import pdb;pdb.set_trace()