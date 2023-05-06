# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num < 0:
        raise ValueError
    if num == 1 or num == 0:
        return 1
    return num * factorial(num-1)


# reverse
def reverse(text):
    rev = ""
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count - 1)


# is_nested_parens
import math
def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    lst = list(parens)
    half_index = len(parens) / 2
    # print(half_index)
    left_parens = lst[math.ceil(half_index):] 
    right_parens= lst[:math.floor(half_index)]
    # print(left_parens, riig)
    if left_parens[len(left_parens) - 1] != ')' or right_parens[len(right_parens) -1] != '(':
        return False
    return is_nested_parens(parens[1:-1])
    
print(is_nested_parens("(())))"))
print(is_nested_parens("(())"))
    


