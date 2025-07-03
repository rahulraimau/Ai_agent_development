import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

# ✅ Load custom .env file
load_dotenv(dotenv_path="apikey.env")
api_key = os.getenv("OPENAI_API_KEY")

# ✅ DEBUG check
assert api_key is not None, "❌ API key not loaded from apikey.env"

# ✅ Pass key directly
llm = ChatOpenAI(
    temperature=0.7,
    model_name="gpt-3.5-turbo",
    openai_api_key="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"
)

# Define prompts
input_prompt = PromptTemplate(
    input_variables=["student_input"],
    template="You are a helpful tutor. Extract the subject and topic from the student's input.\nInput: {student_input}\nOutput: Subject and Topic"
)
task_prompt = PromptTemplate(
    input_variables=["student_input"],
    template="Decide what the student wants: summary, quiz, or explanation.\nInput: {student_input}\nOutput: Action"
)
summary_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Give a concise and clear summary on the topic: {topic}"
)
quiz_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Create a 3-question multiple choice quiz on: {topic}"
)
explain_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain this topic in simple terms: {topic}"
)

# Chains
understanding_chain = LLMChain(llm=llm, prompt=input_prompt)
task_chain = LLMChain(llm=llm, prompt=task_prompt)
summary_chain = LLMChain(llm=llm, prompt=summary_prompt)
quiz_chain = LLMChain(llm=llm, prompt=quiz_prompt)
explain_chain = LLMChain(llm=llm, prompt=explain_prompt)

# Memory
memory = ConversationBufferMemory()

# Unified agent function
def ai_agent(student_input):
    topic_info = understanding_chain.run(student_input)
    memory.save_context({"input": student_input}, {"topic_info": topic_info})

    task = task_chain.run(student_input)
    memory.save_context({"input": student_input}, {"task": task})

    if "summary" in task.lower():
        result = summary_chain.run(topic=topic_info)
    elif "quiz" in task.lower():
        result = quiz_chain.run(topic=topic_info)
    elif "explain" in task.lower():
        result = explain_chain.run(topic=topic_info)
    else:
        result = "Sorry, I didn't understand your request."

    return result