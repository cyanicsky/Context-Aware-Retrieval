# Context-Aware Retrieval-Augmented Text Generator

Welcome to the **Context-Aware Retrieval-Augmented Text Generator** project! This system combines document retrieval and large language model (LLM) generation to provide contextually relevant and meaningful answers to user queries.

This project was inspired by a PhD posting I came across that piqued my curiosity. I decided to take some time on the side to explore how such systems work (and even learn some new things along the way!).

---

## What Does This Project Do?
Have you ever asked a question and needed information pulled from multiple sources to get the best answer? This project is designed to:

1. **Retrieve**: Search for the most relevant documents from a dataset based on your query.
2. **Generate**: Use a language model to craft a detailed, context-aware response using the retrieved documents.

---

## Key Features
- **Document Retrieval**: Leverages TF-IDF-based search to rank and retrieve the most relevant documents.
- **Response Generation**: Utilizes a pre-trained T5 model to generate coherent and informative responses.
- **Interactive Dashboard**: Allows users to input queries and visualize results through a Streamlit interface.

---

## How to Run the Project
Follow these simple steps to get started:

1. Clone the repository to your local machine:
   ```bash
   git clone <repository_url>
   cd context-aware-retrieval
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app using the following command:
   ```bash
   python -m streamlit run dashboards/app.py
   ```

4. Open your browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

---

## Project Structure
```
context-aware-retrieval/
|-- dashboards/          # Streamlit app files
|   |-- app.py           # Main Streamlit application
|-- scripts/             # Core pipeline components
|   |-- retriever.py     # Document retrieval logic
|   |-- generator.py     # Text generation logic
|   |-- pipeline.py      # Retrieve-generate integration
|-- data/                # Raw and processed datasets
|-- requirements.txt     # Python dependencies
|-- README.md            # Project description (this file!)
```

---

## Example Query
When you run the app, try entering a query like:
> "What was discussed at the UN General Assembly about climate change?"

The system will:
1. Search for the most relevant documents in the dataset, based on the context.
2. Generate a concise and context-aware response based on the retrieved information.
This was the result that I got 
![image](https://github.com/user-attachments/assets/a30f16b1-d33a-4e55-999b-176b66f2f01a)

---

## To Note
This was done to figure out how such system works, therefore this uses a mere sample of a dataset to explore the domaine!

---

Happy querying! 🚀

