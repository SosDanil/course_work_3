import json
from config import OPERATIONS_PATH


def get_all_operations(path):
    """загружает список словарей с данными операций"""
    with open(path, encoding="UTF-8") as file:
        content = file
        all_operations = json.load(content)
        return all_operations


def get_only_executed_operations(all_operations):
    """получаем список только исполненных операций, без отмен"""
    executed_operations = []
    for dictionary in all_operations:
        if dictionary.get("state") == "EXECUTED":
            executed_operations.append(dictionary)
    return executed_operations


all_operations = get_all_operations(OPERATIONS_PATH)
print(get_only_executed_operations(all_operations))
