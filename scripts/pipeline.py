# from retriever import Retriever
# from generator import Generator
# import pandas as pd

# #####General function
# # def retrieve_generate_pipeline(query, documents):
# #     retriever = Retriever(documents)
# #     generator = Generator()

# #     top_docs = retriever.retrieve(query)
# #     context = " ".join([documents[i] for i in top_docs])
# #     response = generator.generate(context, query)
# #     return response

# ####Checking the example 
# def retrieve_generate_pipeline(query):
#     # Load documents from the processed dataset
#     df = pd.read_csv('data/processed/cleaned_dataset.csv')
#     documents = df['clean_text'].tolist()
    
#     retriever = Retriever(documents)
#     generator = Generator()

#     top_docs = retriever.retrieve(query)
#     context = " ".join([documents[i] for i in top_docs])
#     response = generator.generate(context, query)
#     return response

# if __name__ == "__main__":
#     docs = ["This is the first document.", "Here is the second document.", "And this is the third one."]
#     query = "What does the first document say?"
#     print(retrieve_generate_pipeline(query, docs))


from scripts.retriever import Retriever
from scripts.generator import Generator
import pandas as pd

class RetrieveGeneratePipeline:
    def __init__(self, dataset_path='data/processed/cleaned_dataset.csv'):
        """Initialize the pipeline with a dataset."""
        self.dataset_path = dataset_path
        self.documents = self._load_documents()
        self.retriever = Retriever(self.documents)
        self.generator = Generator()

    def _load_documents(self):
        """Load and preprocess documents from the dataset."""
        try:
            df = pd.read_csv(self.dataset_path)
            return df['clean_text'].tolist()
        except FileNotFoundError:
            raise Exception(f"Dataset not found at {self.dataset_path}. Please ensure the file exists.")

    def process_query(self, query, top_k=5):
        """Process a query to retrieve and generate a response."""
        top_docs_indices = self.retriever.retrieve(query, top_k=top_k)
        context = " ".join([self.documents[i] for i in top_docs_indices])
        response = self.generator.generate(context, query)
        return response

if __name__ == "__main__":
    pipeline = RetrieveGeneratePipeline()
    query = "What was discussed at the UN General Assembly about climate change?"
    try:
        response = pipeline.process_query(query, top_k=3)
        print("Generated Response:", response)
    except Exception as e:
        print("Error:", e)
