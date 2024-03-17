from jsonschema import validate, ValidationError
from src.schema import SCHEMA


def verify_json(data: dict) -> bool:
    try:
        validate(data, SCHEMA)
    except ValidationError as e:
        print(f"Couldn't validate json:" + e.message)
        raise e

    # "Statement" is a list, so we need to find an object that holds the "Resource" key
    statement = data["PolicyDocument"]["Statement"]
    resource_object = None
    for element in statement:
        if type(element) == dict and "Resource" in element:
            resource_object = element

    # this shouldn't really happen, as "Resource" is a required field
    if not resource_object:
        raise Exception

    resource = resource_object["Resource"]
    c = resource.count("*")
    return c != 1


if __name__ == "__main__":
    verify_json("example")
