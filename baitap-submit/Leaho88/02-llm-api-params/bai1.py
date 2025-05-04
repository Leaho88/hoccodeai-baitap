import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv;
client = Groq(api_key=os.environ.get("GROQ_API_KEY"));

stream = client.chat.completions.create(model="llama-3.3-70b-versatile",
                                                 stream=True,
                                                 messages=[{
                                                     "role": "user",
                                                     "content":"hello! How are you today?A",
                                                 }])
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="");