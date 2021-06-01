import pytest
from cffconvert import Citation
from tests.helpers import load_cff


def test(fixture):
    # (argument fixture is injected from test/conftest.py using pytest fixture magic)
    cffstr = load_cff(fixture)
    if "fail" in fixture:
        with pytest.raises(Exception) as e_info:
            Citation(cffstr=cffstr, suspect_keys=[], validate=True, raise_exception=True)
    else:
        citation = Citation(cffstr=cffstr, suspect_keys=[], validate=True, raise_exception=True)
        assert citation.yaml is not None
