import pytest
from cffconvert import Citation


def test(cffstr):
    # (argument cffstr is injected from test/conftest.py using pytest fixture magic)
    with pytest.raises(Exception) as e_info:
        citation = Citation(cffstr=cffstr, suspect_keys=[], validate=True, raise_exception=True)
