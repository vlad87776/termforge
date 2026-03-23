#!/usr/bin/env python3

import sys
from core.doctor import run_doctor
from core.project import create_project, list_templates
from core.builder import build_project
from core.server import serve_project

VERSION = "0.0.2"

def show_help():
    print(f"TermForge v{VERSION}")
    print("")
    print("Usage:")
    print("  termforge version")
    print("  termforge doctor")
    print("  termforge new <project_name> [--template <name>]")
    print("  termforge template list")
    print("  termforge build")
    print("  termforge serve [port]")
    print("")
    print("Examples:")
    print("  termforge new myapp")
    print("  termforge new myapp --template basic")
    print("  termforge template list")
    print("  termforge serve 8080")

def handle_new_command(args):
    if len(args) < 1:
        print("Error: project name required")
        print("Example: termforge new myapp")
        return

    project_name = args[0]
    template_name = "basic"

    if "--template" in args:
        index = args.index("--template")
        if index + 1 < len(args):
            template_name = args[index + 1]
        else:
            print("Error: --template requires a value")
            return

    create_project(project_name, template_name)

def handle_template_command(args):
    if len(args) < 1:
        print("Error: template command required")
        print("Example: termforge template list")
        return

    subcommand = args[0]

    if subcommand == "list":
        templates = list_templates()
        print("Available templates:")
        for tpl in templates:
            print(f"  - {tpl}")
    else:
        print(f"Unknown template command: {subcommand}")

def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]

    if command == "version":
        print(VERSION)

    elif command == "doctor":
        run_doctor()

    elif command == "new":
        handle_new_command(sys.argv[2:])

    elif command == "template":
        handle_template_command(sys.argv[2:])

    elif command == "build":
        build_project()

    elif command == "serve":
        port = 8000
        if len(sys.argv) >= 3:
            try:
                port = int(sys.argv[2])
            except ValueError:
                print("Invalid port, using 8000")
        serve_project(port)

    elif command in ["help", "--help", "-h"]:
        show_help()

    else:
        print(f"Unknown command: {command}")
        print("")
        show_help()

if __name__ == "__main__":
    main()
