def fibonacci_at_index(index: int):
    a = 1
    b = 1
    for _ in range(1, index):
        temp = a
        a = a + b
        b = temp
    return a
