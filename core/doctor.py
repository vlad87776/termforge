import os
import shutil
import sys

def run_doctor():
    print("Running TermForge doctor...")
    print("")

    print(f"Python version: {sys.version.split()[0]}")

    git_path = shutil.which("git")
    if git_path:
        print(f"Git: OK ({git_path})")
    else:
        print("Git: NOT FOUND")

    storage = os.path.exists("/storage/emulated/0")
    if storage:
        print("Android storage: OK")
    else:
        print("Android storage: not accessible")

    cwd = os.getcwd()
    print(f"Current directory: {cwd}")

    print("")
    print("Doctor finished.")
