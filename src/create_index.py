from llama_index.core import Settings
from llama_index.core import VectorStoreIndex
from model_loader import embed_model
from local_docs_reader import docs

# ====== Create vector store and upload indexed data ======
Settings.embed_model = embed_model # we specify the embedding model to be used
index = VectorStoreIndex.from_documents(docs)