import re
import jsonschema
import pytest
from copy import deepcopy
from ruamel.yaml import YAML
from tests.helpers import get_project_root


def read_lines():
    with open(get_project_root() / "schema-guide.md", "rt") as fid:
        lines = fid.readlines()
    nlines = len(lines)
    return lines, nlines


def find_snippet_starts(lines):
    rexp = r"^(?P<indent>[ ]*)```yaml"
    snippet_starts = []
    indents = []
    for iline, line in enumerate(lines):
        found = re.search(rexp, line)
        if found is not None:
            indent = len(found.group("indent"))
            snippet_starts.append(iline + 2)
            indents.append(indent)
    return snippet_starts, indents


def find_snippet_ends(lines, nlines, starts, indents):
    snippet_ends = []
    for iline, indent in zip(starts, indents):
        while iline - 1 < nlines:
            if lines[iline - 1] == " " * indent + "```\n":
                snippet_ends.append(iline - 1)
                break
            iline += 1
    return snippet_ends


def unindent_snippets(lines, starts, ends, indents):
    snippets = []
    for start, end, indent in zip(starts, ends, indents):
        snippet = [line[indent:] for line in lines[start - 1:end]]
        snippets.append(snippet)
    return snippets


def get_snippets():
    lines, nlines = read_lines()
    starts, indents = find_snippet_starts(lines)
    ends = find_snippet_ends(lines, nlines, starts, indents)
    snippets = unindent_snippets(lines, starts, ends, indents)
    return [pytest.param("".join(snippet), id=f"L{start}-L{end}") for start, end, snippet in zip(starts, ends, snippets)]


@pytest.fixture
def cff_required():
    return {
        "root": {
            "authors": [
                {
                    "name": "The author name"
                }
            ],
            "cff-version": "1.3.0",
            "message": "The message",
            "title": "The title"
        },
        "reference": {
            "authors": [
                {
                    "name": "The reference author name"
                }
            ],
            "title": "The reference title",
            "type": "generic"
        }
    }


@pytest.mark.parametrize("snippet", get_snippets())
def test(snippet: str, cff_required, schema):
    if snippet.startswith("# incorrect"):
        pytest.xfail(reason="deliberately incorrect snippet")

    yaml = YAML(typ="safe")
    yaml.constructor.yaml_constructors[u"tag:yaml.org,2002:timestamp"] = yaml.constructor.yaml_constructors[u"tag:yaml.org,2002:str"]
    cff_loaded = yaml.load(snippet)
    cff_updated = deepcopy(cff_loaded)

    if "preferred-citation" in cff_updated.keys():
        preferred_citation = cff_updated.get("preferred-citation")
        r = deepcopy(cff_required["reference"])
        r.update(preferred_citation)
        cff_updated["preferred-citation"] = r

    if "references" in cff_updated.keys():
        references = cff_updated.get("references", [])
        for i, reference in enumerate(references):
            r = deepcopy(cff_required["reference"])
            r.update(reference)
            cff_updated["references"][i] = r

    instance = deepcopy(cff_required["root"])
    instance.update(cff_updated)

    jsonschema.validate(instance=instance, schema=schema, format_checker=jsonschema.FormatChecker())
