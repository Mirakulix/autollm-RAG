# AutoLLM RAG-Notizen

Eine Schnellreferenz für [AutoLLM](https://github.com/safevideo/autollm) - ein Framework für RAG-basierte LLM-Anwendungen.

## Installation

```bash
# Basis-Installation
pip install autollm

# Mit zusätzlichen Dokumentenlesern (GitHub, PDF, DOCX, EPUB, etc.)
pip install autollm[readers]
```

## Kern-Funktionen

1. Query Engine erstellen:
```python
from autollm import AutoQueryEngine, read_files_as_documents

documents = read_files_as_documents(input_dir="path/to/documents")
query_engine = AutoQueryEngine.from_defaults(documents)

response = query_engine.query("Ihre Frage hier")
```

2. FastAPI App erstellen:
```python
from autollm import AutoFastAPI
import uvicorn

app = AutoFastAPI.from_query_engine(query_engine)
uvicorn.run(app, host="0.0.0.0", port=8000)
```

## Wichtige Konfigurationsoptionen

### Query Engine Erweiterte Optionen

```python
query_engine = AutoQueryEngine.from_defaults(
    documents=documents,
    llm_model="gpt-3.5-turbo",       # LLM Modell
    llm_max_tokens="256",            # Max Tokens
    llm_temperature="0.1",           # Temperatur
    embed_model="huggingface/BAAI/bge-large-zh",  # Embedding Modell
    chunk_size=512,                  # Chunk-Größe
    chunk_overlap=64,                # Chunk-Überlappung
    similarity_top_k=3,              # Top-K ähnliche Dokumente
    vector_store_type="LanceDBVectorStore",  # Vector Store Typ
    enable_cost_calculator=True      # Kostenberechnung aktivieren
)
```

### Unterstützte LLM-Plattformen

- OpenAI/Azure
- HuggingFace
- Anthropic
- Google VertexAI
- AWS Bedrock
- Ollama
- [100+ weitere Modelle](https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json)

### Vector Stores

Standard: LanceDB (serverless, kostengünstig)
Unterstützt: [20+ Vector Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/vector_stores.html#vector-store-options-feature-support)

## Nützliche Links

- [Haupt-Repository](https://github.com/safevideo/autollm)
- [Quickstart Colab Notebook](https://colab.research.google.com/github/safevideo/autollm/blob/main/examples/quickstart.ipynb)
- [Video Tutorials](https://www.youtube.com/watch?v=sgKpBMGC6M0)
- [FAQ & Support](https://github.com/safevideo/autollm/discussions/categories/q-a)

## Besondere Features

- Automatische Kostenberechnung für 100+ LLMs
- Einzeilige FastAPI-App-Erstellung
- Migration von LlamaIndex möglich
- Serverless Vector Store (LanceDB) als Standard

## Support

- Email: support@safevideo.ai
- [GitHub Discussions](https://github.com/safevideo/autollm/discussions)
- [Feature Requests](https://github.com/safevideo/autollm/discussions/categories/feature-requests)