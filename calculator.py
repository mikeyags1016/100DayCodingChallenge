def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y is not 0:
        return x / y
    return ZeroDivisionError('Cannot divide by 0')


def modulus(x, y):
    if y is not 0:
        return x % y
    return ZeroDivisionError('Cannot divide by 0')


def exponent(x, y):
    return x ** y


operators = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division,
    '%': modulus,
    '**': exponent
}


def equation_definer(operator, x, y):
    return operators[operator](x, y)


def run_calculator():
    x = int(input("Enter a number: "))
    y = int(input("Enter a second number: "))
    operator = input("Enter your operation: ")

    print(equation_definer(operator, x, y))

