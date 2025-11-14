"""
RAG module: build index from knowledge passages, query for relevant context.
Uses sentence-transformers for embeddings and FAISS for vector index.
"""

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pandas as pd
import os
import pickle
from typing import List, Tuple

EMBED_MODEL_NAME = "all-MiniLM-L6-v2"  # small, faast. Swap for higher quality if needed.

class RAGIndex:
    def __init__(self, embed_model_name=EMBED_MODEL_NAME, dim: int = None):
        self.embedder = SentenceTransformer(embed_model_name)
        self.index = None
        self.passages = []  # store passages metadata
        self.dim = dim or self.embedder.get_sentence_embedding_dimension()

    def build_from_df(self, df: pd.DataFrame, text_col="text", id_col=None):
        """
        df: pandas DataFrame with at least a column containing text snippets
        """
        texts = df[text_col].astype(str).tolist()
        ids = df[id_col].tolist() if id_col and id_col in df.columns else list(range(len(texts)))
        embeddings = self.embedder.encode(texts, show_progress_bar=True, convert_to_numpy=True)

        # build faiss index
        self.index = faiss.IndexFlatIP(self.dim)  # cosine via normalized vecters or inner product after normalize
        # Normalize embeddiings for cosine similarity
        faiss.normalize_L2(embeddings)
        self.index.add(embeddings)

        self.passages = [{"id": ids[i], "text": texts[i]} for i in range(len(texts))]

    def save(self, path_dir="data/rag_index"):
        os.makedirs(path_dir, exist_ok=True)
        faiss.write_index(self.index, os.path.join(path_dir, "index.faiss"))
        with open(os.path.join(path_dir, "passages.pkl"), "wb") as f:
            pickle.dump(self.passages, f)

    def load(self, path_dir="data/rag_index"):
        self.index = faiss.read_index(os.path.join(path_dir, "index.faiss"))
        with open(os.path.join(path_dir, "passages.pkl"), "rb") as f:
            self.passages = pickle.load(f)

    def query(self, query_text: str, top_k: int = 5) -> List[Tuple[float, dict]]:
        q_emb = self.embedder.encode([query_text], convert_to_numpy=True)
        faiss.normalize_L2(q_emb)
        D, I = self.index.search(q_emb, top_k)  # D = similarities, I = indices
        results = []
        for score, idx in zip(D[0].tolist(), I[0].tolist()):
            if idx < 0 or idx >= len(self.passages):
                continue
            results.append((float(score), self.passages[idx]))
        return results
