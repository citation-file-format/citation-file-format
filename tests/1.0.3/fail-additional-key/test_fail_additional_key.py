import pytest
from cffconvert import Citation


def test(cffstr):
    with pytest.raises(Exception) as e_info:
        citation = Citation(cffstr=cffstr, suspect_keys=[], validate=True, raise_exception=True)
