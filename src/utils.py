import json


def get_all_operations(path):
    """загружает список словарей с данными операций"""
    with open(path, encoding="UTF-8") as file:
        content = file
        all_operations = json.load(content)
        return all_operations
