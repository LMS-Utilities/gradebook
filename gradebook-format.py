import os
import re
import shutil
from pathlib import Path
from typing import Pattern

student_list = [
    
]

old_dir: Path = Path("1/")
new_dir: Path = Path("2/")
new_dir.mkdir(exist_ok=True)
pattern: Pattern = re.compile("_(.*)_attempt_")

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def student_id(path: Path):
    match = re.search(pattern, str(path))
    return match.groups()[0] if match else None

def move_formatter(item, new_item):
    print(f"\t{item}\n=>\t{new_item}", end="\n\n")

def main():
    if not new_dir.exists():
        new_dir.mkdir()

    for item in old_dir.iterdir():
        id_ = student_id(item)
        if id_ is None:
            print(f"does not match regex: {item}")
            continue

        if student_list != [] and id_ not in student_list:
            continue

        student_dir = Path(new_dir, id_)
        if not student_dir.exists():
            student_dir.mkdir()

        # copy root files to student dir
        if item.is_file():
            new_item = Path(student_dir, f"root_{id_}").with_suffix(item.suffix)
            move_formatter(item, new_item)
            shutil.copy(str(item), str(new_item))

        # copy files in dirs to student dir 
        if item.is_dir():
            move_formatter(item, student_dir)
            copytree(str(item), str(student_dir))
        
if __name__ == "__main__":
    main()
