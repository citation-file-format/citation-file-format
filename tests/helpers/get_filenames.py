from pathlib import Path
import pytest


def get_filenames():
    def get_id(f):
        if "examples-passing" in f.parts:
            return f"pass:{f.parts[-2]}"
        elif "examples-failing" in f.parts:
            return f"fail:{f.parts[-2]}"
        else:
            raise Exception("Unexpected clause")
    filenames = Path(__file__).parent.parent.glob("**/*.cff")
    return [pytest.param(f, id=get_id(f)) for f in filenames]
