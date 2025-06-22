from langchain_openai import OpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings

ollama_embed = OllamaEmbeddings(
    base_url="http://159.223.78.26:11434",
    model="bge-m3"
)

openai_embed = OpenAIEmbeddings(model="text-embedding-3-large")


def get_embeddings(embeddings, text):
    return embeddings.embed_query(text)

if __name__ == "__main__":
    text = "I love dogs"
    ollama_embeddings = get_embeddings(ollama_embed, text)
    openai_embeddings = get_embeddings(openai_embed, text)

    print("Ollama Embeddings:", ollama_embeddings)
    print("OpenAI Embeddings:", openai_embeddings)
    print("Dimension of Ollama embedding:", len(ollama_embeddings))
    print("Dimension of OpenAI embedding:", len(openai_embeddings))