import sys
from pathlib import Path
import ruamel.yaml

from ruamel.yaml import YAML

yaml = ruamel.yaml.YAML()
with open('u.yaml')as stream:
   data = yaml.load(stream)
#file_name = Path('u.yaml')

value = sys.argv[1]
#size = int(sys.argv[2])


yaml = YAML()
#data = yaml.load(stream)
data['paths']['changed'] = changed
data['paths'][changed] = dict(changed=value)
yaml.dump(data, sys.stdout)
yaml.dump(data, Path('2u.yaml'))

