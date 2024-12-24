from sentence_transformers import SentenceTransformer

# Load a pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Use the model
embeddings = model.encode("This is a test sentence.")
print(embeddings)
