from fibonacci_recursive import fibonacci_at_index


def test_fibonacci_base_case():
    assert fibonacci_at_index(0) == 1
    assert fibonacci_at_index(1) == 1


def test_fibonacci_index_2_3_6():
    assert fibonacci_at_index(2) == 2
    assert fibonacci_at_index(3) == 3
    assert fibonacci_at_index(6) == 13
