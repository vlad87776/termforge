import os
import shutil

def build_project():
    current_dir = os.getcwd()
    src_dir = os.path.join(current_dir, "src")
    dist_dir = os.path.join(current_dir, "dist")

    if not os.path.exists(src_dir):
        print("Error: src/ not found. Run this inside a TermForge project.")
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
