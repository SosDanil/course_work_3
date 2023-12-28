from config import TEST_DICTIONARY_PATH
from src.utils import get_all_operations, get_only_executed_operations, get_sorted_operations, get_five_last_operations

test_list_for_executed = [{"state": "EXECUTED"}, {"state": "CANCELED"}, {}]
test_list_for_sorted = [{"date": "2015-06-12"}, {"date": "2020-05-07"}, {"date": "2017-02-10"}]


def test_get_all_operations():
    assert get_all_operations(TEST_DICTIONARY_PATH) == [{"name": "Danil", "surname": "Klimenko"},
                                                        {"fruit": "apple", "animal": "dog"}]


def test_get_only_executed_operations():
    assert get_only_executed_operations(test_list_for_executed) == [{"state": "EXECUTED"}]


def test_get_sorted_operations():
    assert get_sorted_operations(test_list_for_sorted) == [{"date": "2020-05-07"}, {"date": "2017-02-10"},
                                                           {"date": "2015-06-12"}]


def test_get_five_last_operations():
    assert get_five_last_operations([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5]
