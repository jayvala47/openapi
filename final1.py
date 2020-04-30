import sys
from pathlib import Path

from ruamel.yaml import YAML

file_name = Path('in.yaml')

b = sys.argv[1]


yaml = YAML()
data = yaml.load(file_name)
paths = data['paths']['/pet']['post']['parameters']['schema']
paths.update(dict(ref=b))
print(paths)
yaml.dump(data, Path('out.yaml'))

