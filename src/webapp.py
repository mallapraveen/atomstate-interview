import os

import streamlit as st
from qa import qa

st.title("Atomstate Interview Question and Answering Code")

st.write("# QA with Hugging Face Transformers")

context = st.text_input("Enter the context")
question = st.text_input("Enter the question")

if st.button("Submit"):
    result = qa(question, context)
    st.write(f"Answer : {result}")

st.subheader(
    "For source code please visit my git [link](https://github.com/mallapraveen/atomstate-interview)"
)
st.subheader("[My Profile](https://github.com/mallapraveen)")
