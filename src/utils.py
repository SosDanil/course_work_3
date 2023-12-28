import json


def get_all_operations(path):
    with open(path) as file:
        content = file
        all_operations = json.load(content)
        return all_operations
