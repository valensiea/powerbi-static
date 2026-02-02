import os
from pathlib import Path

POWER_BI_URL = os.getenv("POWER_BI_URL")

if not POWER_BI_URL:
    raise ValueError("POWER_BI_URL is not set")

template = Path("template.html").read_text()

output = template.replace("{{POWER_BI_URL}}", POWER_BI_URL)

Path("public").mkdir(exist_ok=True)
Path("public/index.html").write_text(output)

print("✅ public/index.html generated")
