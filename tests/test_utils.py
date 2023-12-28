from config import TEST_DICTIONARY_PATH
from src.utils import get_all_operations, get_only_executed_operations
test_list_for_executed = [{"state": "EXECUTED"}, {"state": "CANCELED"}, {}]


def test_get_all_operations():
    assert get_all_operations(TEST_DICTIONARY_PATH) == [{"name": "Danil", "surname": "Klimenko"},
                                                        {"fruit": "apple", "animal": "dog"}]


def test_get_only_executed_operations():
    assert get_only_executed_operations(test_list_for_executed) == [{"state": "EXECUTED"}]
