import os
import re

# === Config ===
INPUT_FILE = "output/temp.md"
OUTPUT_DIR = "output"

def extract_code_blocks(text, lang):
    # Matches triple backtick code blocks like ```html ... ```
    pattern = rf"```{lang}\n(.*?)```"
    return re.findall(pattern, text, re.DOTALL)

def save_code_file(content, filename):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"✅ Saved: {filepath}")

def parse_and_save():
    if not os.path.exists(INPUT_FILE):
        print("❌ AI response file not found!")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    html_blocks = extract_code_blocks(content, "html")
    css_blocks = extract_code_blocks(content, "css")
    js_blocks = extract_code_blocks(content, "javascript")

    if html_blocks:
        save_code_file(html_blocks[0], "index.html")
    if css_blocks:
        save_code_file(css_blocks[0], "style.css")
    if js_blocks:
        save_code_file(js_blocks[0], "script.js")

if __name__ == "__main__":
    parse_and_save()


    
# update 2

def ask_for_updates():
    file_choice = input("👉 Which file do you want to update? (html/css/js/skip): ").lower()
    file_map = {
        "html": "index.html",
        "css": "style.css",
        "js": "script.js"
    }

    if file_choice in file_map:
        filepath = file_map[file_choice]
        with open(filepath, 'r', encoding='utf-8') as f:
            existing_code = f.read()
        
        update_instruction = input("✏️ What would you like to update? ")

        # Send to LLM here: existing_code + instruction → modified_code
        modified_code = call_llm_for_update(existing_code, update_instruction)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(modified_code)
        print(f"✅ {file_choice.upper()} updated successfully!")

    else:
        print("⏭️ Skipping update...")
