import re
from tqdm import tqdm

# File paths
processed_html_path = "output/processed_index.html"
content_file_path = "output/generated_content.txt"
output_path = "output/index.html"

# Step 1: Load placeholder data from generated_content.txt
placeholder_data = {}
with open(content_file_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if "=" in line:
            key, value = line.split("=", 1)
            key = key.strip()
            # Remove surrounding curly braces if present
            if key.startswith("{{") and key.endswith("}}"):
                key = key[2:-2].strip()
            placeholder_data[key] = value.strip()


# Step 2: Load processed HTML with placeholders
with open(processed_html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Step 3: Detect placeholders in processed HTML
placeholders_in_html = re.findall(r"\{\{\s*(\w+)\s*\}\}", html_content)

# Step 4: Track stats
replaced_count = 0
not_found = []

print("\n🔁 Replacing Placeholders:\n")

# Step 5: Replace placeholders using tqdm
for placeholder in tqdm(placeholders_in_html, desc="Processing"):
    key = placeholder.strip()
    value = placeholder_data.get(key)
    if value:
        html_content = html_content.replace(f"{{{{{placeholder}}}}}", value)
        print(f"✅ {placeholder} = {value}")
        replaced_count += 1
    else:
        print(f"❌ {placeholder} not found in generated_content.txt")
        not_found.append(placeholder)

# Step 6: Save final updated HTML
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# Step 7: Summary
print(f"\n✅ {replaced_count} placeholders replaced successfully.")
if not_found:
    print(f"❌ {len(not_found)} placeholders were NOT found in generated_content.txt.")
else:
    print("🎉 All placeholders matched and replaced!")
print(f"✅ Final HTML saved to: {output_path}")
