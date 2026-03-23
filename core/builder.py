import os
import shutil
from core.utils import is_termforge_project

def build_project():
    current_dir = os.getcwd()
    src_dir = os.path.join(current_dir, "src")
    dist_dir = os.path.join(current_dir, "dist")

    if not is_termforge_project(current_dir):
        print("Error: this is not a TermForge project.")
        print("Missing app.json or src/")
        return

    if os.path.exists(dist_dir):
        shutil.rmtree(dist_dir)

    os.makedirs(dist_dir)

    for filename in os.listdir(src_dir):
        src_file = os.path.join(src_dir, filename)
        dst_file = os.path.join(dist_dir, filename)

        if os.path.isfile(src_file):
            shutil.copy(src_file, dst_file)

    print("Build complete.")
    print(f"Output: {dist_dir}")
