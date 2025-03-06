from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Create summarization pipeline
pipe = pipeline("summarization", model="facebook/bart-large-cnn")
hf = HuggingFacePipeline(pipeline=pipe)

# Create prompt template
prompt = PromptTemplate(
    input_variables=["text"],
    template="Please summarize the following text:\n\n{text}"
)

# Create chain
summarize_chain = LLMChain(llm=hf, prompt=prompt)

def summarize_text(text):
    result = summarize_chain.run(text)
    return result
