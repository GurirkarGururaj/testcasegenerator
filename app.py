import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI Test Case Generator", layout="centered")

st.title("🧠 AI Test Case Generator")
st.write("Paste a feature description below to generate detailed test cases.")

feature_input = st.text_area("✏️ Feature Description", height=300)

if st.button("Generate Test Cases") and feature_input.strip():
    with st.spinner("Thinking..."):
        prompt = f"""
        You are a senior QA engineer. Based on the feature description below, generate a detailed list of functional, edge case, and negative test cases.

        Feature Description:
        {feature_input}

        Format:
        - Test Case ID
        - Scenario
        - Steps
        - Expected Result
        - Type (Functional/Edge/Negative)
        """

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
                max_tokens=1500,
            )

            test_cases = response['choices'][0]['message']['content']
            st.markdown("### ✅ Generated Test Cases")
            st.code(test_cases, language='markdown')

        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")
else:
    st.info("Enter a feature description and click 'Generate Test Cases'")
