import sys
from pathlib import Path

from ruamel.yaml import YAML

file_name = Path('u3.yaml')

b = sys.argv[1]


yaml = YAML()
data = yaml.load(file_name)
paths = data['paths']['/pet']
paths.update(dict(changed=b))
print(paths)
yaml.dump(data, Path('3u.yaml'))

