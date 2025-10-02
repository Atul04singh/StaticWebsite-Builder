import os
import threading
import time
from langchain_ollama import OllamaLLM

# === Config ===
PROMPT_FILE = "prompts/game_or_webapp_prompt.txt"
OUTPUT_FILE = "output/temp.md"

def read_prompt(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Prompt file not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()

def save_response(text, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"\n✅ Response saved to: {file_path}")

# 🔁 Simple Spinner Animation
def spinner_animation(stop_event):
    spinner = ['|', '/', '-', '\\']
    idx = 0
    while not stop_event.is_set():
        print(f"\r⏳ Thinking... {spinner[idx % len(spinner)]}", end='', flush=True)
        idx += 1
        time.sleep(0.1)
    print("\r✅ Model responded.              ")

if __name__ == "__main__":
    print("📖 Reading prompt...")
    prompt = read_prompt(PROMPT_FILE)
    print(f"📝 Prompt:\n{prompt}\n")

    print("🚀 Invoking Ai Model using LangChain + Ollama...")

    # Start spinner
    stop_event = threading.Event()
    spinner_thread = threading.Thread(target=spinner_animation, args=(stop_event,))
    spinner_thread.start()

    # Run the model
    llm = OllamaLLM(model="gemma3")
    response = llm.invoke(prompt)

    # Stop spinner
    stop_event.set()
    spinner_thread.join()

    print("\n📩 Response from Gemma:\n")
    print(response)

    save_response(response, OUTPUT_FILE)
