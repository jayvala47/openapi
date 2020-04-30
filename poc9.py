import ruamel.yaml
import sys
from pathlib import Path

from ruamel.yaml import YAML

value1 = sys.argv[1]
value2 = int(sys.argv[2])
value3 = int(sys.argv[3])

print(value1, value2, value3)

yaml = YAML()
#data = yaml.load(file_name)

yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True
yaml.explicit_start = True

with open('u1.yaml') as stream:
   data = yaml.load(stream)

test = data['test']
test.update(dict(name="%value1", age="%{value2}", version="%{value3}"))

with open('u1output.yaml', 'wb') as stream:
    yaml.dump(data, stream)
