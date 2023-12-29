from config import TEST_DICTIONARY_PATH
from src.utils import get_all_operations, get_only_executed_operations, get_sorted_operations, get_five_last_operations, \
    get_formatted_operations

test_list_for_executed = [{"state": "EXECUTED"}, {"state": "CANCELED"}, {}]
test_list_for_sorted = [{"date": "2015-06-12"}, {"date": "2020-05-07"}, {"date": "2017-02-10"}]
test_list_for_formatted_1 = [
    {
    "id": 536723678,
    "state": "EXECUTED",
    "date": "2018-06-12T07:17:01.311610",
    "operationAmount": {
      "amount": "26334.08",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Classic 4195191172583802",
    "to": "Счет 17066032701791012883"
  }
]

test_list_for_formatted_2 = [
    {
    "id": 893507143,
    "state": "EXECUTED",
    "date": "2018-02-03T07:16:28.366141",
    "operationAmount": {
      "amount": "90297.21",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 37653295304860108767"
  }
]

test_list_for_formatted_3 = [
    {
    "id": 390558607,
    "state": "EXECUTED",
    "date": "2019-02-12T00:08:07.524972",
    "operationAmount": {
      "amount": "16796.95",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 72645194281643232984",
    "to": "Счет 95782287258966264115"
  }
]

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


def test_get_formatted_operations():
    assert get_formatted_operations(test_list_for_formatted_1) == ["2018-06-12 Перевод организации\n"
                                                                   "Visa Classic 4195 19** **** 3802 -> Счет **2883\n"
                                                                   "26334.08 USD\n\n"]
    assert get_formatted_operations(test_list_for_formatted_2) == ["2018-02-03 Открытие вклада\n"
                                                                   "-> Счет **8767\n"
                                                                   "90297.21 руб.\n\n"]
    assert get_formatted_operations(test_list_for_formatted_3) == ["2019-02-12 Перевод организации\n"
                                                                   "Счет **2984 -> Счет **4115\n"
                                                                   "16796.95 USD\n\n"]
