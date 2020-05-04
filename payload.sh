#!/bin/bash
v=$1
curl -X POST http://ec2-52-90-102-175.compute-1.amazonaws.com:8080/job/swagger_update/build \
  --user admin:11800846c23b5eba4c0874c4bb84deaad7 \
  --data-urlencode json='{"parameter": [{"name":"schema", "value":"'"$v"'"}]}'

echo schema ref version is $1
