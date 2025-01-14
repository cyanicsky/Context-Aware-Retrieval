import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_data(input_path, output_path):
    """Clean and preprocess raw text data."""
    df = pd.read_csv(input_path)
    df['clean_text'] = df['text'].str.lower().str.replace('[^a-z0-9 ]', '', regex=True)
    df.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")

if __name__ == "__main__":
    preprocess_data('data/raw/dataset.csv', 'data/processed/cleaned_dataset.csv')