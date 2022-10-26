# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError("The number must be positive.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

# reverse
def reverse(string):
    s_list = list(string)
    return reverse_helper(s_list, 0, len(string) - 1)

def reverse_helper(s_list, left, right):
    if left >= right:
        string = ""
        return string.join(s_list)
    else:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        return reverse_helper(s_list, left + 1, right - 1)

# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count - 1)

# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    if len(parens) == 1:
        return False
    return parens[0] == '(' and parens[-1] == ')' and is_nested_parens(parens[1:-1])