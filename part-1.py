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
    return num * factorial(num-1)



# reverse
def reverse(word):
    if len(word) <= 1:
        return word
    return word[-1] + reverse(word[:-1])


# bunny
def bunny(bunnies):
    if bunnies == 0:
        return 0
    return 2 + bunny(bunnies-1)


# is_nested_parens
def is_nested_parens(string):
    if not string:
        return True
    if f"{string[0]}{string[-1]}" == "()" and is_nested_parens(string[1:-1]):
        return True
    else:
        return False

