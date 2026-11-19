import os
import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
BACKEND_DIR = ROOT_DIR / "backend"
BACKEND_RUN = BACKEND_DIR / "run.py"
VENV_PYTHON = BACKEND_DIR / ".venv" / "Scripts" / "python.exe"

if __name__ == "__main__":
    os.chdir(BACKEND_DIR)
    py_exec = str(VENV_PYTHON) if VENV_PYTHON.is_file() else sys.executable
    sys.exit(subprocess.call([py_exec, str(BACKEND_RUN), *sys.argv[1:]]))
