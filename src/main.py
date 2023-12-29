from config import OPERATIONS_PATH
from utils import (get_all_operations, get_only_executed_operations, get_sorted_operations, get_five_last_operations,
                   get_formatted_operations)


def main():
    all_operations = get_all_operations(OPERATIONS_PATH)
    only_executed_operations = get_only_executed_operations(all_operations)
    sorted_operations = get_sorted_operations(only_executed_operations)
    five_last_operations = get_five_last_operations(sorted_operations)
    formatted_operations = get_formatted_operations(five_last_operations)

    for operation in formatted_operations:
        print(operation)


main()
