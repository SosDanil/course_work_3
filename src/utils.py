import json
from config import OPERATIONS_PATH
from datetime import date


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


def get_five_last_operations(all_sorted_operations):
    """получает 5 последних операций из списка"""
    five_operations = all_sorted_operations[:5]
    return five_operations


def get_formatted_operations(not_formatted_operations):
    """форматирует данные в приемлимый для пользователя вид"""
    list_of_formatted_operations = []
    for operation in not_formatted_operations:
        only_date = operation["date"][:10]
        formatted_date = date.fromisoformat(only_date)

        description = operation["description"]
        amount = operation["operationAmount"]["amount"]
        currency = operation["operationAmount"]["currency"]["name"]

        to_list = operation["to"].split(" ")
        to_str = to_list[0]
        to_number = to_list[-1]
        formatted_to_number = to_number[-4:]

        from_list = operation.get("from")
        if from_list:
            from_list_split = from_list.split(" ")
            from_number = from_list_split[-1]
            if len(from_number) == 20:
                formatted_from_number = f"**{from_number[-4:]}"
            else:
                formatted_from_number = f"{from_number[:4]} {from_number[4:6]}** **** {from_number[-4:]}"
            from_str = from_list_split[:-1]
            formatted_from_str = " ".join(from_str)

            formatted_operation = (f"{formatted_date} {description}\n"
                                   f"{formatted_from_str} {formatted_from_number} -> {to_str} **{formatted_to_number}\n"
                                   f"{amount} {currency}\n\n")
        else:
            formatted_operation = (f"{formatted_date} {description}\n"
                                   f"-> {to_str} **{formatted_to_number}\n"
                                   f"{amount} {currency}\n\n")
        list_of_formatted_operations.append(formatted_operation)
    return list_of_formatted_operations

operations = get_all_operations(OPERATIONS_PATH)
notsorted_operations = get_only_executed_operations(operations)
sorted_operations = get_sorted_operations(notsorted_operations)
five_operations = get_five_last_operations(sorted_operations)
print(get_formatted_operations(five_operations))
# for operation in five_formatted_operations:
#     print(operation)

