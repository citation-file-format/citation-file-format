import os
from pykwalify.core import Core

def test_cff_core_examples():

    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".cff"):
                filepath = os.path.join(root, file)


                c = Core(source_file=filepath, schema_files=["CFF-Core/schema.yaml"], yaml_extension="cff")
                c.validate(raise_exception=True)
