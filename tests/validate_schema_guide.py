import pytest
import os
import json
import jsonschema
from ruamel.yaml import YAML


def test():

    def extract_snippets():
        start = 0
        end = len(markdown)
        while start < end:
            snippet_start = markdown.find("```yaml\n", start, end)
            if snippet_start == -1:
                break
            snippet_end = markdown.find("```\n", snippet_start + 8, end)
            text = markdown[snippet_start:snippet_end + 4]
            indent_size = 0
            while text[8:][indent_size] == " ":
                indent_size += 1
            unindented = "\n"
            for line in text[8:-4].split("\n"):
                unindented += line[indent_size:]
                unindented += "\n"
            snippets.append(dict(start=snippet_start, end=snippet_end + 4, text=unindented))
            start = snippet_end + 4
        return snippets

    with open("schema-guide.md", "r") as f:
        markdown = f.read()
        snippets = list()
        snippets = extract_snippets()

        yaml = YAML(typ='safe')
        yaml.constructor.yaml_constructors[u'tag:yaml.org,2002:timestamp'] = yaml.constructor.yaml_constructors[u'tag:yaml.org,2002:str']
        schema_path = os.path.join(os.path.dirname(__file__), "..", "schema.json")
        with open(schema_path, "r") as sf:
            schema_data = json.loads(sf.read())
            for i_snippet, snippet in enumerate(snippets):
                if "# incorrect" in snippet["text"]:
                    continue
                instance = yaml.load(snippet["text"])
                passes = False
                while not passes:
                    try:
                        jsonschema.validate(instance=instance, schema=schema_data, format_checker=jsonschema.FormatChecker())
                        passes = True
                        print("snippet {0}/{1} (chars {2}-{3}): OK".format(i_snippet + 1, len(snippets), snippet["start"], snippet["end"]))
                    except jsonschema.ValidationError as e:
                        path = "" if len(e.relative_path) == 0 else "/".join([str(p) for p in e.relative_path]) + "/"
                        if path == "":
                            if e.message.startswith("'authors' is a required property"):
                                instance["authors"] = []
                            elif e.message.startswith("'cff-version' is a required property"):
                                instance["cff-version"] = "1.2.0"
                            elif e.message.startswith("'message' is a required property"):
                                instance["message"] = "testmessage"
                            elif e.message.startswith("'title' is a required property"):
                                instance["title"] = "testtitle"
                            else:
                                raise Exception("undefined behavior: " + e.message)
                        elif path.startswith("authors"):
                            if e.message.startswith("[] is too short"):
                                instance["authors"].append({"name": "testname"})
                            else:
                                raise Exception("undefined behavior: " + e.message)
                        elif path.startswith("references"):
                            index = int(path.split("/")[1])
                            if e.message.startswith("'authors' is a required property"):
                                instance["references"][index]["authors"] = []
                            elif e.message.startswith("'title' is a required property"):
                                instance["references"][index]["title"] = "testtitle"
                            elif e.message.startswith("'type' is a required property"):
                                instance["references"][index]["type"] = "generic"
                            elif e.message.startswith("[] is too short"):
                                instance["references"][index]["authors"].append({"name": "testname"})
                            elif path.startswith("references/{0}/conference".format(index)):
                                if e.message.startswith("'name' is a required property"):
                                    instance["references"][index]["conference"]["name"] = "testname"
                            else:
                                raise Exception("undefined behavior: " + e.message)
                        elif path.startswith("preferred-citation"):
                            if e.message.startswith("'authors' is a required property"):
                                instance["preferred-citation"]["authors"] = []
                            elif e.message.startswith("'title' is a required property"):
                                instance["preferred-citation"]["title"] = "testtitle"
                            elif e.message.startswith("'type' is a required property"):
                                instance["preferred-citation"]["type"] = "generic"
                            elif e.message.startswith("[] is too short"):
                                instance["preferred-citation"]["authors"].append({"name": "testname"})
                            else:
                                raise Exception("undefined behavior: " + e.message)
                        else:
                            print("Found a problem with snippet at char position {0}-{1}:\n {2}\n{3}".format(snippet["start"], snippet["end"], snippet["text"], e.message))
                            raise e
