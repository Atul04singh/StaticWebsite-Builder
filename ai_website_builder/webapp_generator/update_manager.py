import os
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

llm = Ollama(model="gemma3")  # Or any model you're running in Ollama

OUTPUT_DIR = "output"

file_map = {
    'html': 'index.html',
    'css': 'style.css',
    'js': 'script.js'
}

def get_file_choices():
    print("\n🛠️  Which file do you want to update?")
    print("Options: html / css / js / all / skip")
    choice = input("➡️ Enter your choice: ").strip().lower()

    if choice == "skip":
        print("⏭️  Skipping update process.")
        return []

    elif choice == "all":
        return [os.path.join(OUTPUT_DIR, file_map[key]) for key in file_map]

    elif choice in file_map:
        return [os.path.join(OUTPUT_DIR, file_map[choice])]

    else:
        print("❌ Invalid choice.")
        return get_file_choices()

def get_update_instruction(file_type):
    return input(f"\n💬 Describe what you want to update in the {file_type.upper()} file: ")

def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return None

def generate_updated_code(existing_code, instruction, file_type):
    template = PromptTemplate(
        input_variables=["code", "instruction", "file_type"],
        template="""
You are a coding assistant. Your job is to modify the existing {file_type} code based on the user's instruction.

🧾 User Instruction:
{instruction}

💻 Original {file_type.upper()} Code:
{code}

✏️ Provide the complete updated {file_type.upper()} code below (replace fully, not partial edits):
"""
    )

    prompt = template.format(code=existing_code, instruction=instruction, file_type=file_type)
    try:
        print("🤖 Querying LLM...\n")
        response = llm.invoke(prompt)
        return response
    except Exception as e:
        print(f"❌ LLM error: {e}")
        return existing_code  # Fallback

def save_updated_code(filepath, new_code):
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_code)
        print(f"✅ File '{filepath}' updated successfully!\n" + "-" * 40)
    except Exception as e:
        print(f"❌ Error saving file: {e}")

def run_update_flow():
    while True:
        filepaths = get_file_choices()

        if not filepaths:
            break

        for filepath in filepaths:
            file_type = os.path.splitext(os.path.basename(filepath))[0]
            existing_code = read_file(filepath)

            if existing_code is None:
                continue

            instruction = get_update_instruction(file_type)
            modified_code = generate_updated_code(existing_code, instruction, file_type)

            save_updated_code(filepath, modified_code)

        repeat = input("\n🔁 Do you want to make more updates? (yes / no): ").strip().lower()
        if repeat != "yes":
            print("\n👋 Exiting update manager. All done!")
            break

if __name__ == "__main__":
    run_update_flow()
