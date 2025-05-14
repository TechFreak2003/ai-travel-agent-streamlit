import streamlit as st
from agents.agent import call_openai_agent
import os
from dotenv import load_dotenv

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI Travel Agent", layout="centered")
st.title("🌍 AI Travel Agent")
st.markdown("Ask me about flights, hotels, or travel tips!")

user_input = st.text_input("✈️ Where do you want to go today?", placeholder="e.g., Find flights to Paris")

if st.button("Ask"):
    if not openai_key:
        st.error("OpenAI API key not found. Please set it in the .env file.")
    elif user_input.strip() == "":
        st.warning("Please enter a travel query.")
    else:
        with st.spinner("Thinking..."):
            response = call_openai_agent(user_input, openai_key)
            st.success(response)
