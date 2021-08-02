import pytest
import os
import json
import jsonschema
from ruamel.yaml import YAML


def test():

    with open("schema-guide.md", "r") as f:
        markdown = f.read()

        start = 0
        end = len(markdown)
        snippets = list()

        while start < end:
            snippet_start = markdown.find("```yaml", start, end)
            if snippet_start == -1:
                break
            snippet_end = markdown.find("```", snippet_start + 7, end)
            snippets.append(markdown[snippet_start:snippet_end + 3])
            start = snippet_end + 3

        yaml = YAML(typ='safe')
        yaml.constructor.yaml_constructors[u'tag:yaml.org,2002:timestamp'] = yaml.constructor.yaml_constructors[u'tag:yaml.org,2002:str']
        schema_path = os.path.join(os.path.dirname(__file__), "..", "schema.json")
        defaults = yaml.load("authors:\n  - name: test\ntitle: test\ncff-version: 1.2.0\nmessage: test")
        with open(schema_path, "r") as sf:
            schema_data = json.loads(sf.read())
            for snippet in snippets:
                instance = yaml.load(snippet[8:-3])
                merged = {**defaults, **instance}
                try:
                    jsonschema.validate(instance=merged, schema=schema_data, format_checker=jsonschema.FormatChecker())
                except jsonschema.ValidationError as e:
                    print(snippet[8:-3])
                    raise e
