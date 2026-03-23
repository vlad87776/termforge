#!/usr/bin/env python3

import sys
from core.doctor import run_doctor
from core.project import create_project
from core.builder import build_project
from core.server import serve_project

VERSION = "0.0.1"

def show_help():
    print("TermForge v0.0.1")
    print("")
    print("Usage:")
    print("  termforge version")
    print("  termforge doctor")
    print("  termforge new <project_name>")
    print("  termforge build")
    print("  termforge serve [port]")

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
        if len(sys.argv) < 3:
            print("Error: project name required")
            print("Example: termforge new myapp")
            return
        project_name = sys.argv[2]
        create_project(project_name)

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

    else:
        print(f"Unknown command: {command}")
        show_help()

if __name__ == "__main__":
    main()
