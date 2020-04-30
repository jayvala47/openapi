import sys
from pathlib import Path

from ruamel.yaml import YAML

file_name = Path('u.yaml')

value = sys.argv[1]
#size = int(sys.argv[2])


yaml = YAML()
data = yaml.load(file_name)
paths = data['paths']
paths.update(dict({'/pet': {'post': {'description': '', 
'parameters': [{'required': False, 'in': 'body', 'description': 'Pet object that needs to be added to the store', 'name': 'body', 
'schema': {'ref': 'value'}}], 'tags': ['pet'], 'produces': ['application/xml', 'application/json'], 'summary': 'Add a new pet to the store', 'operationId': 'addPet', 'consumes': ['application/json', 'application/xml'], 'x-swagger-router-controller': 'SampleController'}}}))

with open('u.yaml', 'wb') as stream:
   yaml.dump(data, stream)

#data['paths']['/pet']['post']['tags']['parameters'] = parameters
#data['paths'][parameters] = dict(paramatersConfig=dict(ref=value))
#yaml.dump(data, sys.stdout)
#yaml.dump(data, Path('u.yaml'))
