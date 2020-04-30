curl -X POST http://ec2-204-236-241-168.compute-1.amazonaws.com:8080/job/swagger_update/api/ -H "Jenkins-Crumb:875ee86f6b29832eb7753576610e00543f8c366b155a9c02b740f268ebbc08c8" --data "schema=$1"

echo "schema version is $1"

