from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-01",
    azure_endpoint="https://semantic-openai.openai.azure.com/"
)

def get_embedding(text):
    response = client.embeddings.create(
        input=text,
        model="embedding-model"  # Azure deployment name
    )

    return response.data[0].embedding