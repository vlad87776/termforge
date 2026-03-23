import os
import json
import shutil

def get_templates_dir():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")

def list_templates():
    templates_dir = get_templates_dir()
    if not os.path.exists(templates_dir):
        return []

    return sorted([
        name for name in os.listdir(templates_dir)
        if os.path.isdir(os.path.join(templates_dir, name))
    ])

def create_project(project_name, template_name="basic"):
    base_dir = os.path.abspath(project_name)

    if os.path.exists(base_dir):
        print(f"Error: folder '{project_name}' already exists")
        return

    templates = list_templates()
    if template_name not in templates:
        print(f"Error: template '{template_name}' not found")
        print("Available templates:")
        for tpl in templates:
            print(f"  - {tpl}")
        return

    os.makedirs(base_dir)
    os.makedirs(os.path.join(base_dir, "src"))
    os.makedirs(os.path.join(base_dir, "assets"))
    os.makedirs(os.path.join(base_dir, "dist"))

    config = {
        "name": project_name,
        "version": "0.0.2",
        "template": template_name
    }

    with open(os.path.join(base_dir, "app.json"), "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

    template_dir = os.path.join(get_templates_dir(), template_name)

    for filename in os.listdir(template_dir):
        src = os.path.join(template_dir, filename)
        dst = os.path.join(base_dir, "src", filename)
        if os.path.isfile(src):
            shutil.copy(src, dst)

    print(f"Project '{project_name}' created successfully.")
    print(f"Template: {template_name}")
    print("Next steps:")
    print(f"  cd {project_name}")
    print(f"  python ../termforge.py serve")
