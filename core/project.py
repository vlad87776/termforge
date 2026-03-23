import os
import json
import shutil

def create_project(project_name):
    base_dir = os.path.abspath(project_name)

    if os.path.exists(base_dir):
        print(f"Error: folder '{project_name}' already exists")
        return

    os.makedirs(base_dir)
    os.makedirs(os.path.join(base_dir, "src"))
    os.makedirs(os.path.join(base_dir, "assets"))
    os.makedirs(os.path.join(base_dir, "dist"))

    config = {
        "name": project_name,
        "version": "0.0.1",
        "template": "basic"
    }

    with open(os.path.join(base_dir, "app.json"), "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

    template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates", "basic")

    for filename in ["index.html", "style.css", "app.js"]:
        src = os.path.join(template_dir, filename)
        dst = os.path.join(base_dir, "src", filename)
        shutil.copy(src, dst)

    print(f"Project '{project_name}' created successfully.")
    print(f"Next steps:")
    print(f"  cd {project_name}")
    print(f"  python ../termforge.py serve")
