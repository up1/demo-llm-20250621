from ollama import Client
client = Client(
  host='http://159.223.78.26:11434'
)

response = client.embed(
  model='bge-m3',
  input='I love dogs',
)

print(response["embeddings"])
print("Size : " + str(len(response["embeddings"][0])))