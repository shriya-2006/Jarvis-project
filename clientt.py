from openai import OpenAI

client = OpenAI(
    api_key="api_key="YOUR_GROQ_API_KEY",  # your Groq key here
    base_url="https://api.groq.com/openai/v1"    # <== this is key!
)

response = client.chat.completions.create(
    model="llama3-70b-8192",  # or try llama3-70b-8192 if needed
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the importance of fast language models?"}
    ]
)

print(response.choices[0].message.content)
