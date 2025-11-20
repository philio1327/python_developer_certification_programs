import pytest
def test_contains_five():
    """
    Tests the 'contains_five' function.
    """
    # Example list for testing
    my_list = [1, 3, 5, 7, 9]
    assert contains_five(my_list) == True

def contains_five(list1) -> bool:
    if not isinstance(list1, list):
        return False
    return len(list1) == 5

