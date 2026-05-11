from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv;load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel  #to execute chains parallely

model1 = ChatOpenAI(model="gpt-4o-mini")
model2 = ChatAnthropic(model_name="claude-3")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = "generate short and simple notes from folloing text \n {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template = "generate 5 short questions and answers from the following \n {text}",
    input_variables=['text']
)


prompt3 = PromptTemplate(
    template = "merge provided notes and quiz into single document \n notes -> {notes} and quiz -> {quiz}",
    input_variables=['notes', 'quiz']
)

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser,
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """## Support Vector Machine (SVM) – A Short Note

A **Support Vector Machine (SVM)** is a supervised machine learning algorithm used primarily for **classification** and also for regression tasks (SVR). Its core idea is to find the optimal **hyperplane** that best separates data points of different classes in a high-dimensional space.

### How It Works
- In a two-class problem, SVM identifies the hyperplane that maximizes the **margin** – the distance between the hyperplane and the nearest data points from each class.
- These closest points are called **support vectors**. They alone define the decision boundary.
- If data is not linearly separable, SVM uses **kernel functions** (e.g., linear, polynomial, RBF) to map data into a higher dimension where a clear separation is possible.

### Key Features
- **Effective in high dimensions** – works well even when number of features exceeds samples.
- **Memory efficient** – only support vectors are retained after training.
- **Versatile** – different kernels allow handling of complex, non-linear boundaries.
- **Sensitive to scaling** – feature normalization is essential.
- **Not ideal for very large datasets** – training time can be high.

### Common Applications
Text classification, image recognition, bioinformatics (e.g., protein classification), and handwriting recognition.

In short, SVM is a powerful, geometry-driven classifier known for its accuracy and robustness, especially in moderate-sized, high-dimensional problems."""

result = chain.invoke({'text':text})
print(result)