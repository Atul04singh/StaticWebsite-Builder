import subprocess
import sys
import os

# ✅ Files you mentioned for full web app generation
scripts = [
    "prompt_builder.py",
    "gemma_runner.py",
    "code_parser.py"
]

def safe_print(msg):
    try:
        print(msg)
    except UnicodeEncodeError:
        # If terminal can't print emojis or Unicode
        print(msg.encode('ascii', errors='ignore').decode())

safe_print("\n[*] WebApp Generator Flow Started\n")

for script in scripts:
    script_path = os.path.join(os.path.dirname(__file__), script)
    print(f"🚀 Running {script}...")

    result = subprocess.run(["python", script_path])

    if result.returncode != 0:
        print(f"❌ Error while running {script}. Stopping execution.")
        break
    else:
        print(f"✅ Finished {script}\n" + "-" * 50)

safe_print("\n🎉 Flow completed! Check your output folders.")
