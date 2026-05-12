from langchain_openai import ChatOpenAI
from dotenv import load_dotenv;load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temprature=0, max_completion_tokens=10)

result = model.invoke("what is the capital of india?")
print(result.content)

import pdb;pdb.set_trace()

#this output will not just be plain text but much more detailed

# content='The capital of India is New Delhi.' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 8, 'prompt_tokens': 14, 'total_tokens': 22, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_provider': 'openai', 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_b6580bbee1', 'id': 'chatcmpl-Dd8qToRLJJiUA6dFQdecxmKzC7vx3', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None} id='lc_run--019e063d-a0dd-7bf0-99c9-213cb618eb02-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 14, 'output_tokens': 8, 'total_tokens': 22, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
# we can set temprature to get consistent output