import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv();
client = Groq(api_key=os.environ.get("GROQ_API_KEY"));

# Init conversation
messages = [{
    "role": "system",
    "content":"you are my asssistent."
}]

while True:
    user_input = input("I: ")
    if(user_input.lower() in ["exit", "quit"]):
        print("Done input")
        break;
    # Input question
    messages.append({
        "role": "user",
        "content": user_input
        });

    # Send message
    print("chatbot: ", end="",flush=True);
    reply = "";

    stream = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=100,
        temperature=0.7,
        stream=True,
        messages=messages
    )

    for chunk in stream:
        content = chunk.choices[0].delta.content;
        if content:
            print(content, end="", flush=True);
            reply +=content;
    print();
    messages.append({"role": "assistant", "content": reply});


