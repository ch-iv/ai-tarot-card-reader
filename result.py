import json


def parse_json(output: str) -> dict:
    output = output.strip().replace("\\", "")

    j = json.loads(output)

    return j