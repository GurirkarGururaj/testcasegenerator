import streamlit as st
from openai import OpenAI
import os

st.set_page_config(page_title="AI Test Case Generator", page_icon="🧠")

st.title("🧠 AI Test Case Generator")
st.write("Paste a feature description below to generate detailed test cases.")

prompt = st.text_area("✏️ Feature Description", height=200)

if st.button("🚀 Generate Test Cases"):
    if not prompt.strip():
        st.warning("Please enter a feature description.")
    else:
        with st.spinner("Generating test cases..."):
            try:
                client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": f"Generate test cases for the following feature:\n{prompt}"}],
                    temperature=0.7,
                    max_tokens=500
                )
                result = response.choices[0].message.content
                st.success("✅ Test Cases Generated!")
                st.text_area("🧪 Generated Test Cases", result, height=300)
            except Exception as e:
                st.error(f"❌ Error: {e}")
