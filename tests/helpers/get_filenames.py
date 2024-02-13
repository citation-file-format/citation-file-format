from itertools import chain
import pytest
from tests.helpers.get_project_root import get_project_root


def get_filenames():
    def get_id(f):
        if "examples-passing" in f.parts:
            return f"pass:{f.parts[-2]}"
        elif "examples-failing" in f.parts:
            return f"fail:{f.parts[-2]}"
        else:
            raise Exception("Unexpected clause")

    failing = (get_project_root() / "tests" / "examples-failing").glob("**/CITATION.cff")
    passing = (get_project_root() / "tests" / "examples-passing").glob("**/CITATION.cff")
    filenames = chain(passing, failing)
    return [pytest.param(f, id=get_id(f)) for f in filenames]
