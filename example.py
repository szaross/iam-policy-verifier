## run from a dict object in python
from src import verify_json

json_data = {
    "PolicyName": "root",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "IamListAccess",
                "Effect": "Allow",
                "Action": ["iam:ListRoles", "iam:ListUsers"],
                "Resource": "*",
            }
        ],
    },
}
result = verify_json(json_data)

## run from a json file located in resources
from src import verify_json
from src import load_json

json_data = load_json("example")
result = verify_json(json_data)
