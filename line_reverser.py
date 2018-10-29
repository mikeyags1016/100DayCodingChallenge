def is_palindrome(text):
    if text[::-1] == text:
        return True

    return False


def reverse_string(text):
    if not is_palindrome(text):
        return text[::-1]

    else:
        return text
