from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import subprocess
import os

app = FastAPI()

# ✅ Serve static output files
app.mount("/output", StaticFiles(directory="output"), name="output")

@app.post("/launch/")
async def launch(
    choice: int = Form(...),
    website_type: str = Form(None),
    tone: str = Form(None)
):
    if choice not in [1, 2, 3]:
        return JSONResponse(content={"error": "Invalid choice. Must be 1, 2, or 3."}, status_code=400)

    args = [str(choice)]
    if website_type:
        args.append(website_type)
    if tone:
        args.append(tone)

    try:
        print(f"▶️ Running: python launcher.py {' '.join(args)}")
        result = subprocess.run(["python", "launcher.py"] + args, check=True)
    except subprocess.CalledProcessError:
        return JSONResponse(content={"error": f"Script failed for choice {choice}."}, status_code=500)

    output_path = os.path.join("output", "index.html")
    if os.path.exists(output_path):
        # NOTE: FileResponse is only used for direct download fallback (Postman).
        return FileResponse(output_path, media_type="text/html", filename="index.html")
    else:
        return JSONResponse(content={"error": "Output file not found."}, status_code=404)
