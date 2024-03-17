# IAM Role Policy Verifier

This Python module provides a method to verify the input JSON data format for AWS IAM Role Policies. The method checks if the input JSON Resource field contains a single asterisk, if so it returns `False`. In any other case it returns `True`.

## Usage
`example.py` contains an example usage of the method.
You can either use a json data in a python dictionary format or load a json file from resources directory.
```python
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
```
```python
## run from a json file located in resources
from src import verify_json
from src import load_json

json_data = load_json("example")
result = verify_json(json_data)
```

## Tests
To run all tests run `python -m unittest` command from the main directory.