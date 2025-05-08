import os
import requests
from bs4 import BeautifulSoup
from groq import Groq
from dotenv import load_dotenv

load_dotenv();
client = Groq(api_key=os.environ.get("GROQ_API_KEY"));

# Init conversation
messages = [{
    "role": "system",
    "content":"you are my asssistent."
}]

# Bước 1: Nhập URL từ người dùng
url = input("🔗 Nhập link website: ")

try:
    # Bước 2: Gửi yêu cầu HTTP để lấy HTML
    response = requests.get(url)
    response.raise_for_status()  # Báo lỗi nếu trang lỗi

    # Bước 3: Parse HTML bằng BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Bước 4: Lấy nội dung text từ trang
    main_content = soup.find("div", class_="detail-content afcbc-body");
    reply = "";
    if main_content:
        text = main_content.get_text(separator="\n", strip=True)
        messages.append(
        {
        "role": "user",
        "content": "please summarize this articel: \n" +text
        }
    )
        
    # Bước 5: 

        stream = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            stream= True
        )

        for chunk in stream:
            content = chunk.choices[0].delta.content;
            if content:
                print(content, end="", flush=True);
                reply += content;
        print();
        messages.append({"role": "assistant", "content": reply});    
        
    else:
        print("❌ Không tìm thấy nội dung bài viết.");
except Exception as e:
    print("❌ Lỗi khi tải trang:", e)


