import subprocess
import sys

website_type = sys.argv[1] if len(sys.argv) > 1 else "general"
tone = sys.argv[2] if len(sys.argv) > 2 else "clean and modern"
use_ai_content = sys.argv[3] if len(sys.argv) > 3 else "yes"  # NEW FLAG

print("\n🚀 Starting Website Generation Pipeline...\n")

scripts = []

# Always include basic structure
scripts.append(["python", "main.py", website_type, tone])

# Expand placeholder pattern if used
scripts.append(["python", "expand_dynamic_placeholders.py"])

# Only run content generation if required
if use_ai_content.lower() == "yes":
    scripts.append(["python", "generate_text.py", website_type, tone])
    scripts.append(["python", "replace_placeholder.py"])

# Run all scripts
for script in scripts:
    print(f"\n▶️ Running: {' '.join(script)}")
    result = subprocess.run(script)
    if result.returncode != 0:
        print(f"❌ Error running: {' '.join(script)}")
        break
    else:
        print(f"✅ Completed: {' '.join(script)}\n" + "-" * 50)

print("\n🎉 Pipeline Complete.")
