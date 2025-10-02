import re
import os

# Set file paths
input_html_path = os.path.join("output", "index.html")
output_html_path = os.path.join("output", "processed_index.html")

# Load original HTML content
with open(input_html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Track indexes for each placeholder type
section_title_index = 1
section_text_index = 1
card_title_index = 1
card_description_index = 1
card_button_index = 1

# Replacement logic
def replace_dynamic_placeholder(match):
    global section_title_index, section_text_index
    global card_title_index, card_description_index, card_button_index

    placeholder = match.group(1)  # e.g., SECTION_{i}_TITLE or CARD_{j}_BUTTON_TEXT

    # SECTIONs
    if "SECTION_" in placeholder:
        if "_TITLE" in placeholder:
            replaced = f"{{{{SECTION_{section_title_index}_TITLE}}}}"
            section_title_index += 1
        elif "_TEXT" in placeholder:
            replaced = f"{{{{SECTION_{section_text_index}_TEXT}}}}"
            section_text_index += 1
        else:
            replaced = f"{{{{{placeholder}}}}}"
        return replaced

    # CARDs
    elif "CARD_" in placeholder:
        if "_TITLE" in placeholder:
            replaced = f"{{{{CARD_{card_title_index}_TITLE}}}}"
            card_title_index += 1
        elif "_DESCRIPTION" in placeholder:
            replaced = f"{{{{CARD_{card_description_index}_DESCRIPTION}}}}"
            card_description_index += 1
        elif "_BUTTON_TEXT" in placeholder:
            replaced = f"{{{{CARD_{card_button_index}_BUTTON_TEXT}}}}"
            card_button_index += 1
        else:
            replaced = f"{{{{{placeholder}}}}}"
        return replaced

    return f"{{{{{placeholder}}}}}"  # fallback (unchanged)

# ✅ Regex updated — this matches placeholders like {{SECTION_{i}_TITLE}} or {{CARD_{j}_BUTTON_TEXT}}
processed_html = re.sub(
    r"\{\{(SECTION_\{i\}_[A-Z_]+|CARD_\{j\}_[A-Z_]+)\}\}",
    replace_dynamic_placeholder,
    html_content
)

# Save the result
with open(output_html_path, "w", encoding="utf-8") as f:
    f.write(processed_html)

print(f"✅ Placeholder replacement done! Check '{output_html_path}'")
