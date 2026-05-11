from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
You are a research paper expert.

Explain the research paper "{paper_input}" in a {style_input} style.

Keep the explanation {length_input}.

Also explain:
1. Main idea of the paper
2. Key contribution
3. Real-world use case
""",
    input_variables=["paper_input", "style_input", "length_input"],
    validate_templte=True
)

template.save('template.json')