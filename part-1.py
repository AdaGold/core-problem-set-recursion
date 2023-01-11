# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(number):
    if number <= 1:
        if number < 0:
            raise ValueError("Negative Number")       
        return 1
    return number*factorial(number-1)

# reverse
def reverse(text):
    if len(text) == 0:
        return text
    return reverse(text[1:]) + text[0]

# bunny
def bunny(count):
    if not count:
        return 0
    if count == 1:
        return 2
    return 2 + bunny(count-1)

# is_nested_parens


