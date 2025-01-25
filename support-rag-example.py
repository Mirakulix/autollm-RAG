from langchain_openai import AzureOpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers.parent_document_retriever import ParentDocumentRetriever
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.storage import LocalFileStore

embeddings = AzureOpenAIEmbeddings(
    azure_endpoint="your-azure-endpoint",
    azure_deployment="your-embedding-deployment",
    api_key="your-api-key",
    api_version="2023-05-15"
)

vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", " ", ""]
)

file_store = LocalFileStore("./storage/")

parent_retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    child_splitter=text_splitter,
    parent_splitter=text_splitter,
    byte_store=file_store
)

vector_retriever = vectorstore.as_retriever()

hybrid_retriever = BM25Retriever.combine(
    retrievers=[vector_retriever, parent_retriever],
    weights=[0.5, 0.5]
)