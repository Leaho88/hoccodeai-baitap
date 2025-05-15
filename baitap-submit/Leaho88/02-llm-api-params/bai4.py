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

def read_input_file(file_path):
    with open(file_path,"r", encoding="utf-8") as f:
        return f.read().strip()

def split_into_chunks(text, max_char=1000):
    paragraphs = text.split("\n\n")
    chunks = []
    current_chunk=""
    for para in paragraphs:
        if len(current_chunk) + len(para) + 2 <= max_chars:
            current_chunk += para + "\n\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para + "\n\n"

    if current_chunk.strip():
        chunks.append(current_chunk.strip())
    return chunks