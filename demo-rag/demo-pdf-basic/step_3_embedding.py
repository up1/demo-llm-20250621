from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

from step_1_read_pdf import read_pdf
from step_2_chunking import chunk_text


def create_embedding(texts):
    """
    Create embeddings for the given texts.
    """
    embedding_function = SentenceTransformerEmbeddingFunction()
    return embedding_function(texts)


if __name__ == "__main__":
    # Read the PDF file
    pdf_texts = read_pdf("./data/microsoft_annual_report_2022.pdf")
    
    # Chunk the text
    chunk_texts = chunk_text(pdf_texts)

    # Create embeddings of first chunk
    embeddings = create_embedding(chunk_texts[0])
    print("First chunk:")
    print(chunk_texts[0])
    # Print the first embedding
    print("Size of embedding:", len(embeddings[0]))
    print("First embedding:")
    print(embeddings[0])