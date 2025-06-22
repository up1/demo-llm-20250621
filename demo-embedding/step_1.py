from sentence_transformers import SentenceTransformer

def get_sentence_embeddings(sentences):
    model = SentenceTransformer('BAAI/bge-m3')
    embeddings = model.encode(sentences, clean_up_tokenization_spaces=True)
    return embeddings

if __name__ == "__main__":
    sentences = ["I love dogs"]
    embeddings = get_sentence_embeddings(sentences)
    print(embeddings)
    print(embeddings.shape)