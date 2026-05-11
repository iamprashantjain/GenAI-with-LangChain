from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

# JSON Schema
json_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "key_themes": {
            "type": "array",
            "items": {"type": "string"},
            "description": "All key themes in a broader way discussed in the review"
        },
        "sentiment_reason": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Exact phrases from the review responsible for the sentiment. Do not paraphrase or generate new text."
        },
        "sentiment_score": {
            "type": "array",
            "items": {
                "type": "number",
                "minimum": -1,
                "maximum": 1
            },
            "description": "Sentiment score for the review ranging between -1 and 1"
        }
    },
    "required": [
        "key_themes",
        "sentiment_reason",
        "sentiment_score"
    ]
}

structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke(
    "Great service, friendly staff, and excellent experience overall. Highly recommended!"
)

print(result)

import pdb;pdb.set_trace()