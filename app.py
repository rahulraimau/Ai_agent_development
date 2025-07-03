# app.py

import streamlit as st
from agent_logic import ai_agent

st.set_page_config(page_title="📘 AI Exam Reviser", layout="centered")

st.title("📘 AI Exam Reviser")
st.subheader("Get summaries, quizzes, or explanations for any topic you're revising.")

user_input = st.text_input("🧠 Ask a question (e.g., 'Give me a quiz on photosynthesis')")

if st.button("Submit") and user_input:
    with st.spinner("Thinking..."):
        try:
            response = ai_agent(user_input)
            st.success("✅ Response:")
            st.markdown(response)
        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.info("Tip: Check your API key, quota, or billing status at https://platform.openai.com/account/usage")