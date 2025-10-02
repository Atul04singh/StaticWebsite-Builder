import os
import shutil
import random
import sys

TEMPLATES_DIR = "templates"
OUTPUT_DIR = "output"

def list_dirs(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def choose_option(options, match_string=None):
    if not options:
        return None
    if match_string:
        for option in options:
            if match_string.lower() in option.lower():
                return option
        return options[0]  # fallback
    return options[0]

def choose_variant(path, user_input):
    variants = list_dirs(path)
    if not variants:
        print("❌ No variants found.")
        return None

    matched = None
    for variant in variants:
        if any(word in variant.lower() for word in user_input.lower().split()):
            matched = variant
            break

    if not matched:
        matched = random.choice(variants)
        print(f"🤖 No exact match found. Using closest match: {matched}")
    else:
        print(f"✅ Found a matching variant: {matched}")

    return os.path.join(path, matched)

def copy_src_to_output(variant_path):
    src_path = os.path.join(variant_path, "src")
    if not os.path.exists(src_path):
        print("❌ src/ folder not found in the selected variant.")
        return

    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    shutil.copytree(src_path, OUTPUT_DIR)
    print(f"📁 Template files copied to `{OUTPUT_DIR}/` successfully!")

def main():
    website_type = sys.argv[1] if len(sys.argv) > 1 else None
    description = sys.argv[2] if len(sys.argv) > 2 else ""

    template_types = list_dirs(TEMPLATES_DIR)
    if not template_types:
        print("❌ No template types found in templates/")
        return

    template_type = choose_option(template_types, website_type)
    selected_path = os.path.join(TEMPLATES_DIR, template_type)
    subdirs = list_dirs(selected_path)

    if not subdirs:
        print("❌ No subfolders inside selected template type.")
        return

    # Determine 1-layer or 2-layer structure
    first_subdir_path = os.path.join(selected_path, subdirs[0])
    is_two_layer = "src" not in list_dirs(first_subdir_path)

    if is_two_layer:
        subtype = choose_option(subdirs, website_type)
        subtype_path = os.path.join(selected_path, subtype)
        variant_path = choose_variant(subtype_path, description)
    else:
        variant_path = choose_variant(selected_path, description)

    if variant_path:
        copy_src_to_output(variant_path)

if __name__ == "__main__":
    main()
