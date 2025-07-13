# Ref: https://platform.openai.com/docs/guides/pdf-files?api-mode=chat&lang=python
from openai import OpenAI
client = OpenAI()

file_path = "./data/doc-scan.pdf"
file = client.files.create(
    file=open(file_path, "rb"),
    purpose="user_data"
)

completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "file",
                    "file": {
                        "file_id": file.id,
                    }
                },
                {
                    "type": "text",
                    "text": "Extract the text from the PDF file",
                },
            ]
        }
    ]
)

print(completion)
print(completion.choices[0].message.content)