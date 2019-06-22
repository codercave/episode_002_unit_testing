def manipulate_string(value: str):
    if len(value) <= 1:
        raise ValueError
    elif len(value) == 2:
        return f'{value[1]}{value[0]}'
    else:
        return value[1: len(value) - 1]
