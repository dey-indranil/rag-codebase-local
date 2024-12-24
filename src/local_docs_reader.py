import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader

load_dotenv()

# Fetch environment variables
local_directory_path = os.getenv("LOCAL_DIR_PATH", ".")
required_file_extensions = os.getenv("REQUIRED_FILE_EXTN", ".py,.ipynb,.js,.ts,.md").split(",")

if not local_directory_path:
    raise ValueError("The environment variable LOCAL_DIR_PATH is not set.")

# Initialize the local directory reader
loader = SimpleDirectoryReader(
    input_dir=local_directory_path,
    recursive=True,  # Set to True if you want to include subdirectories
    required_exts=required_file_extensions,  # Filter by file extensions
)

# Load the documents from the local directory
docs = loader.load_data()

# Print the loaded documents (optional)
for doc in docs:
    print(f"Document metadata: {doc.metadata}")
    #print(f"Document: {doc}")
    #print(f"Document: {doc.metadata['file_name']}")
    #print(f"Content: {doc.text[:200]}...")  # Print the first 200 characters for a preview
