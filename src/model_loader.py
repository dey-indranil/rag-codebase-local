from langchain_community.embeddings import HuggingFaceEmbeddings
from llama_index.embeddings.langchain import LangchainEmbedding

def load_embedding_model(
    model_name: str = "BAAI/bge-small-en", device: str = "cpu"
    #BAAI/bge-large-en-v1.5
) -> HuggingFaceEmbeddings:
    model_kwargs = {"device": device}
    encode_kwargs = {
        "normalize_embeddings": True
    }  # set True to compute cosine similarity
    embedding_model = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs,
)

    return embedding_model

# setting up the embedding model
lc_embedding_model = load_embedding_model()
embed_model = LangchainEmbedding(lc_embedding_model)