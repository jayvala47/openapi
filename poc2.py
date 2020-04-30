import sys
from pathlib import Path

from ruamel.yaml import YAML

file_name = Path('u.yaml')

value = sys.argv[1]
#size = int(sys.argv[2])


yaml = YAML()
data = yaml.load(file_name)
data['paths']['/pet']['post']['tags']['parameters'] = parameters
data['paths'][parameters] = dict(paramatersConfig=dict(ref=value))
yaml.dump(data, sys.stdout)
yaml.dump(data, Path('u.yaml'))
