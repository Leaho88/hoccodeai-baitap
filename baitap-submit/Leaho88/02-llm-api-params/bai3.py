import requests
from bs4 import BeautifulSoup

# Bước 1: Nhập URL từ người dùng
url = input("🔗 Nhập link website: ")

try:
    # Bước 2: Gửi yêu cầu HTTP để lấy HTML
    response = requests.get(url)
    response.raise_for_status()  # Báo lỗi nếu trang lỗi

    # Bước 3: Parse HTML bằng BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Bước 4: Lấy nội dung text từ trang
    main_content = soup.find("div", class_="detail-content afcbc-body")
    if main_content:
        text = main_content.get_text(separator="\n", strip=True)
        print(text[:1000])  # In thử 1000 ký tự đầu
    else:
        print("❌ Không tìm thấy nội dung bài viết.") 

    # Bước 5: In thử nội dung (chỉ in 1000 ký tự đầu)
    print("\n📄 Nội dung trang (rút gọn):\n")
    print(text[:1000])  # chỉ in thử phần đầu
    print("... (đã rút gọn)")

except Exception as e:
    print("❌ Lỗi khi tải trang:", e)
