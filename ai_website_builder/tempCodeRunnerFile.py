for i in range(1, 4):
    placeholder_prompts[f"{{{{SECTION_{i}_TITLE}}}}"] = f"Suggest a short section title (max 3 words) for a {website_type} website. Only return the title."
    placeholder_prompts[f"{{{{SECTION_{i}_TEXT}}}}"] = f"Write a 1-2 sentence paragraph for section {i} on a {website_type} homepage. Only return the paragraph."

# Add Card placeholders with clean instructions
for j in range(1, 5):
    placeholder_prompts[f"{{{{CARD_{j}_TITLE}}}}"] = f"Suggest a short card title (2-3 words) highlighting a feature of a {website_type} website. Only return the title."
    placeholder_prompts[f"{{{{CARD_{j}_DESCRIPTION}}}}"] = f"Write a 1-sentence description for card {j} on a {website_type} homepage. Only return the sentence."
    placeholder_prompts[f"{{{{CARD_{j}_BUTTON_TEXT}}}}"] = "Return a short CTA button label like 'Learn More'. Only return the label."