from openai import OpenAI

client = OpenAI(
    api_key="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",  # your Groq key here
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
