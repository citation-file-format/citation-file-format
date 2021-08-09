import pytest
from cffconvert import Citation
from examples.helpers import load_cff
from examples import validator


def test(fixture):
    # (argument fixture is injected from test/conftest.py using pytest fixture magic)
    cffstr = load_cff(fixture)
    can_test_with_cffconvert = "1.0.3" in fixture or "1.1.0" in fixture
    if can_test_with_cffconvert:
        if "fail" in fixture:
            with pytest.raises(Exception) as e_info:
                Citation(cffstr=cffstr, suspect_keys=[], validate=True, raise_exception=True)
        else:
            citation = Citation(cffstr=cffstr, suspect_keys=[], validate=True, raise_exception=True)
            assert citation.yaml is not None
    else:
        if "fail" in fixture:
            with pytest.raises(Exception) as e_info:
                validator.validate(fixture, 'schema.json')
        else:
            validator.validate(fixture, 'schema.json')
