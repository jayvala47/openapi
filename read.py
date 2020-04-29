#!/usr/bin/env python3

import yaml

with open('file1.yaml') as f:

	data = yaml.load(f, Loader=yaml.FullLoader)
  	print(data)
    
#    docs = yaml.load_all(f, Loader=yaml.FullLoader)
#    for doc in docs:
#	
#     for k,v in doc.item():
#         print(k, "->", v)

paths = data['paths']
paths.update(dict({'/pet': {'post': {'description': '', 
'parameters': [{'required': False, 'in': 'body', 'description': 'Pet object that needs to be added to the store', 'name': 'body', 
'schema': {'$ref': 'Version2'}}], 'tags': ['pet'], 'produces': ['application/xml', 'application/json'], 'summary': 'Add a new pet to the store', 'operationId': 'addPet', 'consumes': ['application/json', 'application/xml'], 'x-swagger-router-controller': 'SampleController'}}}))

with open('file2.yaml', 'wb') as stream:
   yaml.safe_dump(data, stream, default_flow_style=False, 
                  explicit_start=True, allow_unicode=True, encoding='utf-8')
