# Vector Stores

This folder contains practical work exploring **vector stores and similarity search** with LangChain.

## FAISS Vector Search

A simple job-search demo that:

* Loads job listings from a text file
* Splits the text into smaller chunks
* Converts the chunks into vector embeddings
* Stores the embeddings using FAISS
* Converts a user query into an embedding
* Finds similar job-listing chunks using vector similarity search

### Concepts Learned

* Vector Stores
* FAISS
* Text Chunking
* Text Embeddings
* Similarity Search
* Semantic Search
* LangChain Document Loaders

### Technologies

* Python
* LangChain
* FAISS
* Ollama
* `nomic-embed-text`

This project uses Ollama locally for generating text embeddings instead of a cloud-based embedding API.
