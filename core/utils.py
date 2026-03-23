import os
import json

def is_termforge_project(path="."):
    app_json = os.path.join(path, "app.json")
    src_dir = os.path.join(path, "src")
    return os.path.exists(app_json) and os.path.isdir(src_dir)

def load_project_config(path="."):
    app_json = os.path.join(path, "app.json")
    if not os.path.exists(app_json):
        return None

    with open(app_json, "r", encoding="utf-8") as f:
        return json.load(f)
