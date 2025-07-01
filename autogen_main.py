import threading
import time
import subprocess
import sys
import os
from bol_watcher import watch_for_bol_files, process_pdf

def launch_agent_backend():
    subprocess.Popen(
        [sys.executable, "-m", "autogenstudio"],
        creationflags=subprocess.CREATE_NEW_CONSOLE if os.name == "nt" else 0
    )
    print("Agent backend launched.")

def launch_watcher():
    print("Starting shipment watcher...")
    watch_for_bol_files(process_pdf)

if __name__ == "__main__":
    watcher_thread = threading.Thread(target=launch_watcher, daemon=True)
    watcher_thread.start()
    launch_agent_backend()
    print("System is live. Press Ctrl+C to stop.")
    while True:
        time.sleep(60)

