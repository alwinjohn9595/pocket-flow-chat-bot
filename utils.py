from groq import Groq

import os

def call_llm(messages):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY", "your-groq-api-key"))
    
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=messages,
        temperature=0.7
    )

    return response.choices[0].message.content



if __name__ == "__main__":
    # Test the LLM call
    messages = [{"role": "user", "content": "In a few words, what's the meaning of life?"}]
    response = call_llm(messages)
    print(f"Prompt: {messages[0]['content']}")
    print(f"Response: {response}")

