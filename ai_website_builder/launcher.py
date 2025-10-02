import subprocess
import sys

def run_script(script_args):
    print(f"\n🚀 Running {' '.join(script_args)}...\n")
    result = subprocess.run(script_args)
    if result.returncode != 0:
        print(f"❌ Error running: {' '.join(script_args)}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("❌ Usage: python launcher.py <choice> [optional_args...]")
        print("Choices: 1 = AI Build, 2 = Template, 3 = Web App")
        sys.exit(1)

    choice = int(sys.argv[1])
    optional_args = sys.argv[2:]  # e.g., ["Furniture", "Modern"]

    if choice == 1:
        run_script(["python", "templaterun.py"] + optional_args)

    elif choice == 2:
        run_script(["python", "run.py"])

    elif choice == 3:
        run_script(["python", "webapp_generator/app_runner.py"])

    else:
        print("❌ Invalid choice. Please use 1, 2, or 3.")
        sys.exit(1)

if __name__ == "__main__":
    main()
