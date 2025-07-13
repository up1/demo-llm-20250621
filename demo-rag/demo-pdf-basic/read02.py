from langchain_community.document_loaders import PyPDFLoader

file_path = "./data/microsoft_annual_report_2022.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()
print(f"Number of documents loaded: {len(docs)}")
# Filter out documents that are empty
docs = [doc for doc in docs if doc.page_content.strip()]
print(f"Number of non-empty documents: {len(docs)}")
# Display the first 5 documents and their metadata
for i, doc in enumerate(docs[:5]):
    print(f"Document {i+1}:")
    print(doc.metadata)  # Print metadata of each document
    print(doc.page_content[:500])  # Print the first 500 characters of each document
    print("-" * 40)  # Separator for readability