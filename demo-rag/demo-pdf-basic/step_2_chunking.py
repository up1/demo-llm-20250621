from step_1_read_pdf import read_pdf
from langchain.text_splitter import RecursiveCharacterTextSplitter


def chunk_text(texts):
    character_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", " ", ""],
        chunk_size=1000,
        chunk_overlap=0
        )
    character_split_texts = character_splitter.split_text('\n\n'.join(texts))
    return character_split_texts

if __name__ == "__main__":
    # Read the PDF file
    pdf_texts = read_pdf("./data/microsoft_annual_report_2022.pdf")
    
    # Chunk the text
    chunk_texts = chunk_text(pdf_texts)
    # Print the number of chunks
    print(f"\nTotal chunks: {len(chunk_texts)}")
    # Print the first chunk
    print("First chunk:")
    print(chunk_texts[0])

    # Add metadata to each chunk
    chunked_with_metadata = [
        {
            "text": chunk,
            "metadata": {
                "source": "./data/microsoft_annual_report_2022.pdf",
                "page": i + 1
            }
        }
        for i, chunk in enumerate(chunk_texts)
    ]
    # Print the first chunk with metadata
    print("\nFirst chunk with metadata:")
    print(chunked_with_metadata[1])
    