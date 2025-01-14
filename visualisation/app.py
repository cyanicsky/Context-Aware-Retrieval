# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from scripts.retriever import Retriever
# from scripts.generator import Generator

import sys
print(sys.path)

import streamlit as st
from scripts.pipeline import retrieve_generate_pipeline



def main():
    st.title("Retrieve-Generate System")

    query = st.text_input("Enter your query:")
    docs = st.text_area("Enter documents (one per line):").splitlines()

    if st.button("Submit"):
        if query and docs:
            response = retrieve_generate_pipeline(query, docs)
            st.success(f"Response: {response}")

if __name__ == "__main__":
    main()
