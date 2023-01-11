# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num < 0:
        raise ValueError
    elif num == 0:
        return 1
    else:
        return num * factorial(num-1)


# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    else: 
        first_char = text[0]
        remaining_chars = text[1:]
        return reverse(remaining_chars) + first_char

# bunny
def bunny(count):
    if count == 0:
        return 0
    else:
        return bunny(count-1) + 2


# is_nested_parens
def bunny(count):
    if count == 0:
        return 0
    else:
        return bunny(count-1) + 2

