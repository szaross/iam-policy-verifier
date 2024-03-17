SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "PolicyName": {"type": "string"},
        "PolicyDocument": {
            "type": "object",
            "properties": {
                "Version": {"type": "string"},
                "Statement": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "Sid": {"type": "string"},
                            "Effect": {"type": "string"},
                            "Action": {"type": "array", "items": {"type": "string"}},
                            "Resource": {"type": "string"},
                        },
                        "required": ["Resource"],
                    },
                },
            },
            "required": ["Statement"],
        },
    },
    "required": ["PolicyDocument"],
}
