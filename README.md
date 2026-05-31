# PyNads

Python Network Asset Documentation System s a lightweight Python application for documenting home‑network assets using a SQLite backend.
It provides an interactive CLI for entering device information and is designed to grow into a full CMDB‑style tool with export capabilities and component‑level tracking.

## Features

- Interactive CLI for adding network nodes
- Validation of OS type, IP configuration, and multi‑select fields
- SQLite backend with a future‑proof schema
- Fully testable with pytest
- Uses uv for fast, reliable Python environment management

## Requirements

Astral uv is required. Either it will be installed system-wide, or the user will install it after cloning the repsoitory.

### System-wide

System-wide install is performed as per https://docs.astral.sh/uv/getting-started/installation/, then these steps would be required to clone the repo and activate the venv:

```bash
git clone https://github.com/dmonlineuk/pynads && cd pynads
uv venv
. .venv/bin/activate
```

### Inside the virtual environment

The following will clone the repo, activate the venv and install uv:

```bash
git clone https://github.com/dmonlineuk/pynads && cd pynads
python -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
pip install uv
```

#### Development Environment

Run `uv sync --group dev` to enable development tools `isort`, `ruff` and `pytest`.

### Copilot Links

https://copilot.microsoft.com/shares/KCE4uk43ahhXyih81qSGJ

