from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv;load_dotenv()


# 1. Define the structure
class Sentiment(BaseModel):
    sentiment: str = Field(description="positive, negative, or neutral")
    score: float = Field(description="Score from -1 to 1")
    reason: str = Field(description="Why you chose this sentiment")


# 2. Create structured model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
structured_model = model.with_structured_output(Sentiment)

# 3. Analyze reviews
reviews = [
    "This product is amazing! Best purchase ever!",
    "Terrible quality, completely disappointed.",
    "It's okay, nothing special."
]


for review in reviews:
    result = structured_model.invoke(f"Analyze this review:\n{review}")
    print(f"Review: {review}")
    print(f"Sentiment: {result.sentiment}, Score: {result.score}")
    print(f"Reason: {result.reason}")
    print("-" * 50)