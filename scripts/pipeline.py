from retriever import Retriever
from generator import Generator
import pandas as pd

#####General function
# def retrieve_generate_pipeline(query, documents):
#     retriever = Retriever(documents)
#     generator = Generator()

#     top_docs = retriever.retrieve(query)
#     context = " ".join([documents[i] for i in top_docs])
#     response = generator.generate(context, query)
#     return response

####Checking the example 
def retrieve_generate_pipeline(query):
    # Load documents from the processed dataset
    df = pd.read_csv('data/processed/cleaned_dataset.csv')
    documents = df['clean_text'].tolist()
    
    retriever = Retriever(documents)
    generator = Generator()

    top_docs = retriever.retrieve(query)
    context = " ".join([documents[i] for i in top_docs])
    response = generator.generate(context, query)
    return response

if __name__ == "__main__":
    docs = ["This is the first document.", "Here is the second document.", "And this is the third one."]
    query = "What does the first document say?"
    print(retrieve_generate_pipeline(query, docs))
