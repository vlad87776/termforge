import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

def serve_project(port=8000):
    current_dir = os.getcwd()
    src_dir = os.path.join(current_dir, "src")

    if not os.path.exists(src_dir):
        print("Error: src/ not found. Run this inside a TermForge project.")
        return

    os.chdir(src_dir)

    server = HTTPServer(("127.0.0.1", port), SimpleHTTPRequestHandler)

    print(f"Serving project at http://127.0.0.1:{port}")
    print("Press Ctrl+C to stop.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
