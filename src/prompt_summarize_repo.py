from query_engine import query_engine
from llama_index.core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

qa_prompt_tmpl_str = (
    "Context information is below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Given the context information above I want you to think step by step to answer the query in a crisp manner, incase case you don't know the answer say 'I don't know!'.\n"
    "Query: {query_str}\n"
    "Answer: "
)

qa_prompt_tmpl = PromptTemplate(
    qa_prompt_tmpl_str
)

query_engine.update_prompts({"response_synthesizer:text_qa_template": qa_prompt_tmpl})

print("Welcome! Ask me questions about the repository. Type 'exit' to quit.")

while True:
    user_query = input("\nYour question: ")
    if not user_query:
        continue
    if user_query.lower() == 'exit':
        print("Goodbye!")
        break
    response = query_engine.query(user_query)
    print("\nAnswer:", response)
