import jsonschema

from tests.helpers import get_filenames
from tests.helpers import loadcff
import pytest


@pytest.mark.parametrize("filename", get_filenames())
def test_cff_files(schema, filename):
    def assert_passes():
        try:
            jsonschema.validate(instance=instance, schema=schema, format_checker=jsonschema.FormatChecker())
        except jsonschema.exceptions.ValidationError as e:
            reason = e.message
            pytest.fail(reason=reason)

    def assert_fails():
        with pytest.raises(jsonschema.exceptions.ValidationError):
            jsonschema.validate(instance=instance, schema=schema, format_checker=jsonschema.FormatChecker())

    instance = loadcff(filename)
    if "examples-passing" in filename.parts:
        assert_passes()
    elif "examples-failing" in filename.parts:
        assert_fails()
    else:
        raise Exception("Unexpected clause")
