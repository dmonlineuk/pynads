import os
import tempfile

import pytest


@pytest.fixture
def temp_db(monkeypatch):
    # Create a temporary file
    fd, path = tempfile.mkstemp()
    os.close(fd)

    # Patch the DB path
    monkeypatch.setenv("DB_PATH", path)

    yield path

    # Cleanup
    os.remove(path)
