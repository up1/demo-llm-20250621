import os 
os.environ['USER_AGENT'] = 'demoagent'

import bs4
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

# 1. Load, chunk and index the contents from wikipedia and save to Vector DB(ChromaDB)
loader = WebBaseLoader(
    web_paths=(
        "https://aws.amazon.com/th/what-is/retrieval-augmented-generation/",
    ),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(class_="eb-faq-content")
    ),
)
docs = loader.load()
# Remove \n and \t from the text
for doc in docs:
    doc.page_content = doc.page_content.replace("\n", "").replace("\t", "")


# 2. Split the documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
print("Size of chunk:", splits.__len__())
for idx, text in enumerate(splits):
    text.metadata["id"] = idx

# Show the first 5 splits
for split in splits:
    print("ID:", split.metadata["id"])
    print(split.page_content)
    print("=====================")