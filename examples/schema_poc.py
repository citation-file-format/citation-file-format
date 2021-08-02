import jsonschema
import argparse
from ruamel.yaml import YAML
import json


def validate(data_path, schema_path):
    with open(data_path, 'r') as fi:
        # Convert to Python object
        yaml = YAML(typ='safe')
        yaml.constructor.yaml_constructors[u'tag:yaml.org,2002:timestamp'] = yaml.constructor.yaml_constructors[u'tag:yaml.org,2002:str']
        yml_data = yaml.load(fi)

        with open(schema_path, 'r') as sf:
            schema_data = json.loads(sf.read())
            jsonschema.validate(instance=yml_data, schema=schema_data, format_checker=jsonschema.FormatChecker())


if __name__ == "__main__":
    """Run like this from the command line:
    `python3 -m schema_poc.py -d data.yml -s schema.json`
    """
    parser = argparse.ArgumentParser(  
        description='Validates a YAML file against a JSON Schema')  
    parser.add_argument(  
        '-d', '--data', type=str,  
        help='A YAML data file', required=True)
    parser.add_argument(
        '-s', '--schema', type=str,
        help='A JSON Schema file', required=True) 
    args = parser.parse_args()  
    validate(args.data, args.schema)
