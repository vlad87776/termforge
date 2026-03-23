# TermForge

TermForge is a lightweight app builder prototype for Termux.

It allows you to create simple app projects, run them locally, and build a basic output directory directly from Termux on Android.

## Features

- Create new projects
- Local preview server
- Simple build system
- Basic HTML/CSS/JS template
- Built and tested in Termux

## Current Version

`0.0.1`

## Requirements

- Termux
- Python
- Git

Install dependencies:

```bash
pkg update
pkg install python git -y

Project Structure
termforge/
├── core/
│   ├── doctor.py
│   ├── project.py
│   ├── builder.py
│   └── server.py
├── templates/
│   └── basic/
│       ├── index.html
│       ├── style.css
│       └── app.js
├── termforge.py
└── README.md

## Commands
Show version

python termforge.py version

Run environment check

python termforge.py doctor

Create a new project

python termforge.py new myapp

Start local preview server

cd myapp
python ../termforge.py serve

Then open: http://127.0.0.1:8000

Build project

python ../termforge.py build

## Status

Early working prototype.

## Roadmap

v0.0.2
better CLI output
project validation
more templates
improved install process

v0.0.3
android export prototype
GitHub Actions integration

## Author
Created in Termux by vlad87776
