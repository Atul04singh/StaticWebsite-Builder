import os
import sys
from tqdm import tqdm
from langchain_community.llms import Ollama

# ✅ Get inputs via command-line arguments
website_type = sys.argv[1] if len(sys.argv) > 1 else "general"
user_instruction = sys.argv[2] if len(sys.argv) > 2 else "Make it clean, modern, and user-friendly."

# 🧠 Load Ollama model
llm = Ollama(model="gemma3")

# 📁 Output folder setup
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

print(f"\n🚀 Generating content for a '{website_type}' website with tone: '{user_instruction}'...\n")

# 🔖 Placeholders and prompts
placeholder_prompts = {
    "{{NAVBAR_TITLE}}": f"Suggest a one-word brand name for a {website_type} website. Only return a single word. No explanation.",
    
    "{{NAVBAR_LINK_1}}": "Return a single-word navbar link like 'Home'. No explanation.",
    "{{NAVBAR_LINK_2}}": "Return a single-word navbar link like 'About'. No explanation.",
    "{{NAVBAR_LINK_3}}": "Return a single-word navbar link like 'Services'. No explanation.",
    "{{NAVBAR_LINK_4}}": "Return a single-word navbar link like 'Contact'. No explanation.",
    
    "{{HERO_TITLE}}": f"Write a short and catchy homepage headline for a {website_type} website. Max 5 words. Only return the headline.",
    "{{HERO_SUBTITLE}}": f"Write a one-sentence subtitle explaining what the {website_type} site offers. Only return the sentence.",
    "{{HERO_BUTTON_TEXT}}": "Suggest a short call-to-action button text like 'Get Started'. Only return the CTA text.",
    
    "{{FOOTER_TEXT}}": f"Write a simple copyright line for a {website_type} website. Only return the line.",
    "{{FOOTER_LINK_1}}": "Return a common footer link like 'Privacy Policy'. Only return the text.",
    "{{FOOTER_LINK_2}}": "Return a common footer link like 'Terms of Service'. Only return the text.",
}

# ➕ Section placeholders
for i in range(1, 4):
    placeholder_prompts[f"{{{{SECTION_{i}_TITLE}}}}"] = f"Suggest a short section title (max 3 words) for a {website_type} website. Only return the title."
    placeholder_prompts[f"{{{{SECTION_{i}_TEXT}}}}"] = f"Write a 1-2 sentence paragraph for section {i} on a {website_type} homepage. Only return the paragraph."

# ➕ Card placeholders
for j in range(1, 5):
    placeholder_prompts[f"{{{{CARD_{j}_TITLE}}}}"] = f"Suggest a short card title (2-3 words) highlighting a feature of a {website_type} website. Only return the title."
    placeholder_prompts[f"{{{{CARD_{j}_DESCRIPTION}}}}"] = f"Write a 1-sentence description for card {j} on a {website_type} homepage. Only return the sentence."
    placeholder_prompts[f"{{{{CARD_{j}_BUTTON_TEXT}}}}"] = "Return a short CTA button label like 'Learn More'. Only return the label."

# 🔮 Function to query LLM
def query_llm(prompt):
    try:
        response = llm.invoke(f"{prompt}\nTone: {user_instruction}")
        return response.strip()
    except Exception as e:
        print(f"❌ LLM error: {e}")
        return "Default Content"

# 💾 Save to file
output_file = os.path.join(output_dir, "generated_content.txt")
with open(output_file, "w", encoding="utf-8") as f:
    for placeholder, prompt in tqdm(placeholder_prompts.items(), desc="Generating Content"):
        result = query_llm(prompt)
        f.write(f"{placeholder}={result}\n")

print(f"\n✅ All content saved to '{output_file}' 🎉")
