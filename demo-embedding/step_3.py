import openai

client = openai.Client()

def get_openai_embeddings(sentences):
    embeddings = []
    for sentence in sentences:
        response = client.embeddings.create(
            input=sentence,
            model="text-embedding-3-large"
        )
        embeddings.append(response.data[0].embedding)
    return embeddings

if __name__ == "__main__":
    sentences = ["I love dogs"]
    embeddings = get_openai_embeddings(sentences)
    print(embeddings)
    print("Dimension of embedding:", len(embeddings[0]))
