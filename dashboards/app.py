# # import sys
# # import os
# # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# # from scripts.retriever import Retriever
# # from scripts.generator import Generator

# import sys
# print(sys.path)

# import streamlit as st
# from scripts.pipeline import RetrieveGeneratePipeline



# def main():
#     st.title("Retrieve-Generate System")

#     query = st.text_input("Enter your query:")
#     docs = st.text_area("Enter documents (one per line):").splitlines()

#     if st.button("Submit"):
#         if query and docs:
#             response = RetrieveGeneratePipeline(query, docs)
#             st.success(f"Response: {response}")

# if __name__ == "__main__":
#     main()

import streamlit as st
from scripts.pipeline import RetrieveGeneratePipeline
# Initialize the pipeline
pipeline = RetrieveGeneratePipeline()

# Streamlit App
def main():
    st.title("Context-Aware Retrieval-Augmented Text Generator")
    st.write("Ask a question, and the system will retrieve relevant documents and generate a context-aware response.")

    # Input Query
    query = st.text_input("Enter your query:")
    top_k = st.slider("Number of documents to retrieve:", min_value=1, max_value=10, value=3)

    if st.button("Submit"):
        if query.strip():
            try:
                # Process the query through the pipeline
                response = pipeline.process_query(query, top_k=top_k)
                st.success(f"Generated Response: {response}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a query.")

    # Dataset Preview (Optional)
    if st.checkbox("Show Dataset Preview"):
        try:
            st.write(pipeline.documents[:10])  # Display the first 10 documents
        except Exception as e:
            st.error(f"Could not load the dataset: {e}")

if __name__ == "__main__":
    main()
