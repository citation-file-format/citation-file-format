from cffconvert import Citation


def test(cffstr):
    # (argument cffstr is injected from test/conftest.py using pytest fixture magic)
    citation = Citation(cffstr=cffstr, suspect_keys=[], validate=True, raise_exception=True)
    assert citation.yaml is not None
