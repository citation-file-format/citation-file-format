import os


def pytest_generate_tests(metafunc):
    """Generates a list of relative paths to CITATION.cff files under tests/, and
    uses them to parameterize a fixture by the name of 'fixture'."""
    d = os.path.join(".", "tests")
    fixtures = list()
    for root, dirs, files in os.walk(d):
        for name in files:
            if name == "CITATION.cff":
                fixtures.append(os.path.join(root, name))

    metafunc.parametrize("fixture", fixtures)
