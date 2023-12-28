from config import TEST_DICTIONARY_PATH
from src.utils import get_all_operations


def test_get_all_operations():
    assert get_all_operations(TEST_DICTIONARY_PATH) == [{"name": "Danil", "surname": "Klimenko"},
                                                        {"fruit": "apple", "animal": "dog"}]
