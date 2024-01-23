from ruamel.yaml import YAML


def loadcff(filename):
    yaml = YAML(typ="safe")
    yaml.constructor.yaml_constructors[u"tag:yaml.org,2002:timestamp"] = yaml.constructor.yaml_constructors[u"tag:yaml.org,2002:str"]
    with open(filename, "r") as fid:
        return yaml.load(fid)
