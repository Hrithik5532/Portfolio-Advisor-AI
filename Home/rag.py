from llama_index import GPTVectorStoreIndex
import openai
import os

# Load the LlamaIndex knowledge base
INDEX_PATH = "portfolio/llama_index.json"
index = GPTVectorStoreIndex.load_from_disk(INDEX_PATH)

# OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def retrieve_knowledge(user_query):
    """
    Retrieve relevant knowledge using LlamaIndex.
    """
    response = index.query(user_query)
    return response.response


def generate_response(user_context, retrieved_knowledge, user_query):
    """
    Generate AI response by combining user context and retrieved knowledge.
    """
    prompt = f"""
    User Context: {user_context}
    Retrieved Knowledge: {retrieved_knowledge}
    User Query: {user_query}
    Provide detailed portfolio advice based on the above information.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}],
    )
    return response['choices'][0]['message']['content']
