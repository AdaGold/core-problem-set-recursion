# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num < 0:
        raise ValueError("Input must be a non-negative integer.")
    if num == 0:
        return 1
    return num * factorial(num-1)


# reverse
def reverse(text):
    if text == "":
        return ""
    return text[-1] + reverse(text[:len(text)-1])


# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(string):
    if len(string) % 2 != 0:
        return False
    if string == "":
        return True
    return string[0] == "(" and string[-1] == ")" and is_nested_parens(string[1:len(string)-1])


