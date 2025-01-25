# Hybrid-Ansatz mit Parent Document Retriever
from langchain import ChromaDB, ParentDocumentRetriever
from langchain.retrievers import BM25Retriever

# Kombiniere BM25 und Vektorsuche
hybrid_retriever = BM25Retriever.combine(
    vector_retriever,
    parent_document_retriever,
    weights=[0.5, 0.5]
)