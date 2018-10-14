def is_float_or_negative(index):
    if type(index) is float or index < 0:
        return True
    return False


def is_not_number(index):
    try:
        int(index)
        return True
    except ValueError:
        return False

def fib(index):
    if is_not_number(index):
        if not is_float_or_negative(index):
            return 1 if index in (0, 1, 2) \
                else fib(index - 1) + fib(index - 2)
        raise ValueError('Cannot input non integer items')
    raise ValueError('Cannot input none characters')


