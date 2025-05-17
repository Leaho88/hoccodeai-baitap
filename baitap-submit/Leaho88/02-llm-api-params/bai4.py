import os


def build_system_prompt(source_lang, target_lang, tone):
    return f""" 
        You are a professional translator. Your task is to translate the following content from {source_lang} to {target_lang}.
        The translation must be:
        - Accurate and complete.
        - Maintain the original meaning.
        - Follow this tone/style: "{tone}".
        - Preserve formatting and structure (headings, line breaks, lists, etc.) when possible.

        Start translation only after reading the entire input.
        If the input is a fragment, translate it in context and wait for more parts.
    """


print(build_system_prompt("Vietnamese", "English", "formal and academic"))


# ✅ Hàm này dùng để đọc nội dung từ một file văn bản
def read_input_file(file_path):
    # Mở file ở chế độ đọc ("r") với mã hóa UTF-8
    # Sử dụng "with" để đảm bảo file tự đóng sau khi đọc xong
    with open(file_path, "r", encoding="utf-8") as f:
        # Đọc toàn bộ nội dung trong file rồi loại bỏ khoảng trắng và dòng trống đầu/cuối bằng .strip()
        return f.read().strip()


# ✅ Hàm chia nội dung thành các đoạn nhỏ (chunk), không vượt quá số ký tự giới hạn
def split_into_chunks(text, max_chars=500):
    # Tách văn bản thành các đoạn (paragraph) dựa trên dấu xuống dòng đôi "\n\n"
    paragraphs = text.split(
        "\n\n"
    )  # Trả về một list (danh sách), không cần khai báo trước
    chunks = []  # Danh sách để lưu các đoạn đã chia
    current_chunk = ""  # Biến tạm để gom nội dung cho đến khi đủ dài

    # Duyệt từng đoạn văn trong danh sách
    for para in paragraphs:
        # Nếu cộng thêm đoạn này mà tổng độ dài vẫn <= giới hạn → tiếp tục gom vào current_chunk
        if len(current_chunk) + len(para) + 2 <= max_chars:
            current_chunk += (
                para + "\n\n"
            )  # Thêm đoạn vào chunk hiện tại và giữ ngắt dòng
        else:
            # Nếu vượt giới hạn → lưu chunk hiện tại vào danh sách kết quả
            chunks.append(current_chunk.strip())  # .strip() giúp xóa khoảng trắng thừa
            # Bắt đầu chunk mới từ đoạn vừa bị "tràn"
            current_chunk = para + "\n\n"

    # Sau vòng lặp, nếu vẫn còn nội dung trong current_chunk thì thêm vào
    if current_chunk.strip():
        chunks.append(current_chunk.strip())  # Tránh trường hợp đoạn rỗng bị thêm vào

    # Trả về danh sách các chunk đã chia
    return chunks
