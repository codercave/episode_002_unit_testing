from fibonacci_recursive import fibonacci_at_index


def test_index_zero_and_one():
    assert fibonacci_at_index(0) == 1
    assert fibonacci_at_index(1) == 1


def test_index_6():
    assert fibonacci_at_index(6) == 13
