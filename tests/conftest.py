import json
import pytest
from tests.helpers.get_project_root import get_project_root


@pytest.fixture
def schema():
    filename = get_project_root() / "schema.json"
    with open(filename, "r") as fid:
        txt = fid.read()
    return json.loads(txt)

