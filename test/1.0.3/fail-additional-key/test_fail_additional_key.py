import pytest
import os
from cffconvert import Citation

def get_sibling_cff():
    realpath = os.path.realpath(__file__)
    dir = os.path.dirname(realpath)
    return os.path.join(dir, "CITATION.cff")


@pytest.fixture(scope="module")
def cffstr():
    fixture = get_sibling_cff()
    with open(fixture, "r") as f:
        s = f.read()
    return s


def test1(cffstr):
    with pytest.raises(Exception) as e_info:
        citation = Citation(cffstr=cffstr, suspect_keys=[], validate=True, raise_exception=True)
