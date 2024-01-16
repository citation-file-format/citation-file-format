from pathlib import Path
import json
import pytest


@pytest.fixture
def schema():
    filename = Path(__file__).parent.parent / "schema.json"
    with open(filename, "r") as fid:
        txt = fid.read()
    return json.loads(txt)

