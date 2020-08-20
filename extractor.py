from pathlib import Path
import subprocess

directory = "2"

for item in Path(directory).iterdir():
    args = ["unar", str(item.name), "-o", item.stem]
    subprocess.Popen(args, cwd=directory)
