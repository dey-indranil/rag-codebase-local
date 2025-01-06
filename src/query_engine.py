from llama_index.llms.ollama import Ollama
from llama_index.core import Settings
from create_index import index

#remove later
import os
import psutil

# Get the current process
process = psutil.Process(os.getpid())

# Print memory usage in bytes
memory_in_bytes = process.memory_info().rss
print(f"Memory usage: {memory_in_bytes / (1024 * 1024):.2f} MB")
#remove later





# setting up the llm
llm = Ollama(model="llama3.1", request_timeout=60.0) 
#works
#tinyllama
#oom list
#starcoder2:3b
#llama3.2
#llama3.1
# ====== Setup a query engine on the index previously created ======
Settings.llm = llm # specifying the llm to be used
query_engine = index.as_query_engine(streaming=True, similarity_top_k=4)