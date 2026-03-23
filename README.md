# TermForge

TermForge is a lightweight app builder prototype for Termux.

It allows you to create simple app projects, run them locally in your browser, and build a basic output directory directly from Termux on Android.

This project is focused on making app creation in Termux easier, cleaner, and more modern.

## Features

- Create new projects directly in Termux
- Built-in local preview server
- Basic build system
- Template-based project generation
- Project validation
- Lightweight Python-based CLI
- Designed and tested in Termux

## Current Version

0.0.2

## Goals

TermForge is being developed as a simple and modern tool for users who want to create app projects directly from Termux without relying on heavy or outdated workflows.

Main goals:

- simple setup
- simple commands
- clean project structure
- easy preview in browser
- support for templates
- future Android export support

## Requirements

You need:

- Termux
- Python
- Git

Install required packages:

    pkg update
    pkg install python git -y

## Installation

Clone the repository:

    git clone https://github.com/vlad87776/termforge.git
    cd termforge

Run the tool with:

    python termforge.py

## Project Structure

    termforge/
    ├── core/
    │   ├── doctor.py
    │   ├── project.py
    │   ├── builder.py
    │   ├── server.py
    │   └── utils.py
    ├── templates/
    │   ├── basic/
    │   │   ├── index.html
    │   │   ├── style.css
    │   │   └── app.js
    │   └── todo/
    │       ├── index.html
    │       ├── style.css
    │       └── app.js
    ├── .gitignore
    ├── README.md
    └── termforge.py

## Commands

### Show version

    python termforge.py version

### Show help

    python termforge.py help

### Run environment check

    python termforge.py doctor

### List available templates

    python termforge.py template list

### Create a new project with default template

    python termforge.py new myapp

### Create a new project with selected template

    python termforge.py new myapp --template todo

### Start local preview server

    cd myapp
    python ../termforge.py serve

Then open in browser:

    http://127.0.0.1:8000

You can also specify a custom port:

    python ../termforge.py serve 8080

### Build project

    python ../termforge.py build

The generated files will be placed in:

    dist/

## Templates

TermForge currently includes these templates:

### basic

A simple starter template with:

- heading
- text
- button
- JavaScript alert

### todo

A small todo-style example app with:

- task input
- add button
- dynamic task list

More templates are planned in future versions.

## Example Workflow

### 1. Create a project

    python termforge.py new todoapp --template todo

### 2. Enter the project directory

    cd todoapp

### 3. Run local preview

    python ../termforge.py serve

### 4. Open in browser

    http://127.0.0.1:8000

### 5. Build the project

    python ../termforge.py build

## How It Works

When you create a project, TermForge:

- creates a project folder
- creates src/, assets/, and dist/
- generates app.json
- copies files from the selected template into src/

When you build a project, TermForge:

- checks that the current folder is a valid TermForge project
- copies files from src/ into dist/

When you serve a project, TermForge:

- checks the project structure
- starts a local HTTP server
- lets you open the app in your mobile browser

## Project Validation

TermForge checks whether the current folder is a valid project by looking for:

- app.json
- src/

If these are missing, serve and build will stop with an error message.

## Current Status

TermForge is currently an early working prototype.

Implemented so far:

- project creation
- local preview server
- basic build system
- project validation
- template support
- tested in Termux on Android
- GitHub repository published

## Roadmap

### v0.0.1

- initial working prototype
- create project
- serve project
- build project
- basic template

### v0.0.2

- improved CLI structure
- template system
- template list command
- project validation
- todo template

### Planned for v0.0.3

- improved CLI output
- install script improvements
- cleaner project detection
- more templates

### Planned for future versions

- Android export prototype
- GitHub Actions integration
- web-based local interface
- better project management commands
- possible APK export workflow

## Development

TermForge is currently being developed directly in Termux.

Typical workflow:

    git add .
    git commit -m "update message"
    git push

## Notes

This project is still in a very early stage.

Right now the goal is not to replace large desktop development environments, but to build a lightweight and practical app-building workflow for Termux users.

## Author

Created by vlad87776

Built in Termux on Android

## License

No license has been added yet.
