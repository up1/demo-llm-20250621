import chromadb
from chromadb.utils.embedding_functions import (
    OpenAIEmbeddingFunction,
    SentenceTransformerEmbeddingFunction,
)

from step_1_read_pdf import read_pdf
from step_2_chunking import chunk_text


def save_to_vectordb(texts):
    """
    Save the embeddings and texts to a vector database.
    """
    # Create embeddings for the texts
    # embedding_function = SentenceTransformerEmbeddingFunction()
    embedding_function = OpenAIEmbeddingFunction()

    # Initialize the ChromaDB client
    client = chromadb.PersistentClient(path="./db")

    # Create a new collection
    chroma_collection = client.create_collection("microsoft_annual_report_2022", embedding_function=embedding_function)

    # Add the embeddings and texts to the collection
    ids = [str(i) for i in range(len(texts))]
    chroma_collection.add(ids=ids, documents=texts)


if __name__ == "__main__":
    # Read the PDF file
    pdf_texts = read_pdf("./data/microsoft_annual_report_2022.pdf")
    
    # Chunk the text
    chunk_texts = chunk_text(pdf_texts)
    
    # Save to vector database
    save_to_vectordb(chunk_texts)
    print("Saved to vector database.")