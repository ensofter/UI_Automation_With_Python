import pytest


@pytest.mark.parametrize('int_for_test', [-100, -1, 0, 1, 100])
def test_integer_is_even(int_for_test):
    assert int_for_test % 2 == 0, f"Integer {int_for_test} isn't even"
