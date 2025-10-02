import os
import sys
import time
import ollama
import random
from tqdm import tqdm  # Progress bar

# 🛠 Function to Load Component File
def load_component(component_name, variant=1):
    file_path = f"components/{component_name}/variant_{variant}.html"
    if not os.path.exists(file_path):
        return f"<!-- {component_name} variant {variant} not found -->"
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# 🎯 Function to Get AI-Picked Variant
def select_component_variant(component_name, prompt):
    model = "llama3:latest"
    query = f"Given {component_name} variants, select the best one for this request: {prompt}. Reply only with a number."

    print(f"🔍 Selecting {component_name} variant...")
    for _ in tqdm(range(10), desc=f"Processing {component_name}", ascii=True):
        time.sleep(0.1)

    response = ollama.chat(model=model, messages=[{"role": "user", "content": query}])
    try:
        variant_number = int(response["message"]["content"].strip())
        return max(1, min(variant_number, 4))  # Clamp between 1–4
    except:
        return 1

# 🚀 Website Generator
def generate_website(user_prompt):
    navbar_variant = select_component_variant("navbar", user_prompt)
    hero_variant = select_component_variant("hero", user_prompt)
    section_variant_1 = select_component_variant("section", user_prompt)
    middle_section_variant = random.choice([v for v in range(1, 5) if v != section_variant_1])
    card_variant = select_component_variant("cards", user_prompt)
    footer_variant = select_component_variant("footer", user_prompt)

    print(f"\n✅ Selected Variants: Navbar {navbar_variant}, Hero {hero_variant}, Sections {section_variant_1}, {middle_section_variant}, {section_variant_1}, Card {card_variant}, Footer {footer_variant}")

    # Load HTML parts
    navbar = load_component("navbar", navbar_variant)
    hero = load_component("hero", hero_variant)
    section_1 = load_component("section", section_variant_1)
    middle_section = load_component("section", middle_section_variant)
    card = load_component("cards", card_variant)
    footer = load_component("footer", footer_variant)

    cards_grid = f"""
    <div class="grid grid-cols-4 grid-rows-4 gap-4">
        <div class="row-span-4">{card}</div>
        <div class="row-span-4">{card}</div>
        <div class="row-span-4">{card}</div>
        <div class="row-span-4">{card}</div>
    </div>
    """

    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Generated Website</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body>
        {navbar}
        {hero}
        {section_1}
        {middle_section}
        {section_1}
        {cards_grid}
        {footer}
    </body>
    </html>
    """

    os.makedirs("output", exist_ok=True)
    with open("output/index.html", "w", encoding="utf-8") as file:
        file.write(html_template)

    print("\n🎉 ✅ Website generated successfully! Check 'output/index.html'.")

# 🏁 Entrypoint
if __name__ == "__main__":
    user_input = sys.argv[1] if len(sys.argv) > 1 else "Modern and clean website"
    generate_website(user_input)
