
import os
from dotenv import load_dotenv
from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFaceHub

# Load Hugging Face API key
load_dotenv("apikey.env")
hf_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Set up LLM from Hugging Face Hub
llm = HuggingFaceHub(
    repo_id="tiiuae/falcon-7b-instruct",
    model_kwargs={"temperature": 0.5, "max_new_tokens": 256},
    huggingfacehub_api_token=hf_key
)

summary_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Give a short summary of the topic: {topic}"
)
summary_chain = LLMChain(llm=llm, prompt=summary_prompt)

def ai_agent(user_input):
    return summary_chain.run(topic=user_input)
