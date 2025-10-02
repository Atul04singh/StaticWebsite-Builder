import os

def build_prompt():
    print("🛠️ Let's build a custom Web App or Game!\n")

    app_type = input("👉 What do you want to build? (e.g., Todo list, Calculator, Tic Tac Toe): ").strip()
    is_game = input("🎮 Is it a game? (y/n): ").strip().lower() == 'y'

    features = input("✨ Any specific features or functionality you want? (press Enter to skip): ").strip()
    style = input("🎨 Any specific design/style preferences? (e.g., modern, minimal, retro): ").strip()

    prompt = ""

    if is_game:
        prompt += f"Create a small web-based game called '{app_type}' using HTML, CSS, and JavaScript."
    else:
        prompt += f"Create a responsive web application for '{app_type}' using HTML, CSS, and JavaScript."

    if features:
        prompt += f" Include features like: {features}."

    if style:
        prompt += f" Use a {style} design approach."

    prompt += " Return only the HTML, CSS, and JavaScript code in separate code blocks without any explanation, description, or comments."


    return prompt


def save_prompt_to_file(prompt, folder='prompts', filename='game_or_webapp_prompt.txt'):
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(prompt)
    print(f"\n✅ Prompt saved to: {file_path}")
    return file_path


if __name__ == "__main__":
    final_prompt = build_prompt()
    print("\n📝 Generated Prompt:\n")
    print(final_prompt)

    save_prompt_to_file(final_prompt)
