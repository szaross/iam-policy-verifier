from json import load


def load_json(file_name: str) -> dict:
    with open(f"../resources/{file_name}.json") as f:
        data = load(f)
    return data


def load_json_test(file_name: str) -> dict:
    with open(f"resources/{file_name}.json") as f:
        data = load(f)
    return data
