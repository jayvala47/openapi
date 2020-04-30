import sys
from pathlib import Path

from ruamel.yaml import YAML

file_name = Path('config_in.yaml')

engine = sys.argv[1]
size = int(sys.argv[2])


yaml = YAML()
data = yaml.load(file_name)
data['storage']['engine'] = engine
data['storage'][engine] = dict(engineConfig=dict(cacheSizeGB=size))
yaml.dump(data, sys.stdout)
yaml.dump(data, Path('config.yaml'))
