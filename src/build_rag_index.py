import pandas as pd
from rag import RAGIndex
import os

DATA_PATH = "data/passages.csv"   # your dataset
INDEX_DIR = "data/rag_index"                # output folder

def main():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Missing data file: {DATA_PATH}")

    print("Loading data...")
    df = pd.read_csv(DATA_PATH)

    if "text" not in df.columns:
        raise ValueError("Data must contain a 'text' column.")

    print("Building RAG index...")
    rag = RAGIndex()

    rag.build_from_df(df, text_col="text")

    print("Saving index...")
    rag.save(INDEX_DIR)

    print(f"RAG index built successfully → {INDEX_DIR}")

if __name__ == "__main__":
    main()
