
import streamlit as st
from agent_logic import ai_agent

st.set_page_config(page_title="📘 AI Exam Reviser (Hugging Face)", layout="centered")
st.title("📘 AI Exam Reviser")
st.subheader("Get summaries from open-source LLMs (no OpenAI required).")

user_input = st.text_input("Ask your question or topic:")

if st.button("Submit") and user_input:
    with st.spinner("Thinking..."):
        try:
            response = ai_agent(user_input)
            st.success("✅ Response:")
            st.markdown(response)
        except Exception as e:
            st.error(f"❌ Error: {e}")
