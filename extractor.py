from pathlib import Path
import subprocess

directory = "gradebook_format"

def switch(file: Path):
    if file.suffix == ".zip":
        return ["7z", "x", file.name, f"-o{file.stem}"]
    elif file.suffix == ".rar":
        return ["unrar", "x", file.name, f"{file.stem}/"]
    else:
        print(f"unknown {file}")
        raise Exception


for item in Path(directory).iterdir():    
    args = switch(item)
    print(args)
    subprocess.Popen(args, cwd=directory)
