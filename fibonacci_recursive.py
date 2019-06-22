def fibonacci_at_index(index: int):
    if index == 0 or index == 1:
        return 1
    else:
        return fibonacci_at_index(index - 1) + fibonacci_at_index(index - 2)
