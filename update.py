import yaml

with open("config.yaml", 'r') as stream:
    try:
        loaded = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

#dict['paths'] 
# Modify the fields from the dict
loaded['paths']['/pet.post.parameters.schema.$ref'] = "Version2"
loaded['paths']['api_key.name'] = "jay"
##loaded['paths.api_key']['name'] = "apikey"
#loaded['paths./pet.post.parameters.schema']['table'] = "data"

# Save it again
with open("swagger_modified1.yaml", 'w') as stream:
    try:
        yaml.dump(loaded, stream, default_flow_style=False)
    except yaml.YAMLError as exc:
        print(exc)
