import os 
os.environ['USER_AGENT'] = 'demoagent'

import bs4
from langchain_community.document_loaders import WebBaseLoader

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
print(docs)