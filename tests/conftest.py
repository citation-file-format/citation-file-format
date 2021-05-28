import os
import pytest


@pytest.fixture
def cffstr(request):
    fixture = os.path.join(request.fspath.dirname, "CITATION.cff")
    with open(fixture, "r") as f:
        s = f.read()
    return s
