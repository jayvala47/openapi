import sys
from pathlib import Path

from ruamel.yaml import YAML

file_name = Path('upload.yaml')

value = sys.argv[1]
#size = int(sys.argv[2])


yaml = YAML()
data = yaml.load(file_name)
data['paths']['paramaters'] = parameters
data['paths'][parameters] = dict(paramatersConfig=dict($ref=value))
yaml.dump(data, sys.stdout)
yaml.dump(data, Path('file.yaml'))