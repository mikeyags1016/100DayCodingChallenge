def is_valid_input(index):
    try:
        int(index)
        return True
    except ValueError:
        return False


def fibonacci(index):
    if is_valid_input(index):
        if index < 0 or type(index) is float:
            return -1
        else:
            if index == 0 or index == 1 or index == 2:
                return 1
            else:
                return fibonacci(index - 1) + fibonacci(index - 2)
    else:
        raise ValueError('Cannot input none integer items')

