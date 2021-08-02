import pytest
import os
import json
import jsonschema
from ruamel.yaml import YAML
from flatten_json import flatten, unflatten_list


def test():

    with open("schema-guide.md", "r") as f:
        markdown = f.read()

        start = 0
        end = len(markdown)
        snippets = list()

        while start < end:
            snippet_start = markdown.find("```yaml\n", start, end)
            if snippet_start == -1:
                break
            snippet_end = markdown.find("```\n", snippet_start + 8, end)
            text = markdown[snippet_start:snippet_end + 4]
            indent_size = 0
            while text[8:][indent_size] == " ":
                indent_size += 1
            unindented = ""
            for line in text[8:-4].split("\n"):
                unindented += line[indent_size:]
                unindented += "\n"

            snippets.append(dict(start=snippet_start, end=snippet_end + 4, text=unindented))
            start = snippet_end + 4

        yaml = YAML(typ='safe')
        yaml.constructor.yaml_constructors[u'tag:yaml.org,2002:timestamp'] = yaml.constructor.yaml_constructors[u'tag:yaml.org,2002:str']
        schema_path = os.path.join(os.path.dirname(__file__), "..", "schema.json")
        with open(schema_path, "r") as sf:
            schema_data = json.loads(sf.read())
            for snippet in snippets:
                if "# incorrect" in snippet["text"]:
                    continue
                instance = yaml.load(snippet["text"])
                # defaults = yaml.load("authors:\n" +
                #                      "  - name: test\n" +
                #                      "title: test\n" +
                #                      "cff-version: 1.2.0\n" +
                #                      "message: test\n" +
                #                      "references:\n" +
                #                      "  - title: test\n" +
                #                      "    authors:\n" +
                #                      "      - name: test\n" +
                #                      "    type: generic\n")
                defaults = {
                    "authors": [
                        {
                            "family-names": "test"
                        }
                    ],
                    "title": "test",
                    "cff-version": "1.2.0",
                    "message": "test",
                    "references": [
                        {
                            "title": "test",
                            "authors": [
                                {
                                    "family-names": "test"
                                }
                            ],
                            "type": "generic"
                        }
                    ]
                }
                flattened_defaults = flatten(defaults, "/")
                flattened_instance = flatten(instance, "/")
                merged = unflatten_list({**flattened_defaults, **flattened_instance}, "/")
                try:
                    jsonschema.validate(instance=merged, schema=schema_data, format_checker=jsonschema.FormatChecker())
                except jsonschema.ValidationError as e:
                    print("Found a problem with snippet at char position {0}-{1}:\n {2}\n{3}".format(snippet["start"], snippet["end"], snippet["text"], e.message))
                    raise e
