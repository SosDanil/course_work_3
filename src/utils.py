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


def get_sorted_operations(not_sorted_operations):
    """сортирует операции по убыванию даты (от последних операций к ранним)"""
    dict_for_sorted = {}
    for dictionary in not_sorted_operations:
        dict_for_sorted[dictionary["date"]] = dictionary
    sorted_operations = sorted(dict_for_sorted.items(), reverse=True)
    sorted_list_operations = []
    for element in sorted_operations:
        sorted_list_operations.append(element[1])
    return sorted_list_operations


operations = get_all_operations(OPERATIONS_PATH)
notsorted_operations = get_only_executed_operations(operations)
print(get_sorted_operations(notsorted_operations))
