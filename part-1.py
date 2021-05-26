# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num == 0:
        return 1
    elif num < 0:
        raise ValueError(num)
    return num*factorial(num-1)


# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    first_letter = text[:1]
    remaining_word = text[1:]
    return reverse(remaining_word) + first_letter


# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens, left_side = 0):
    right_side = len(parens) -1 -left_side
    
    if len(parens) == 0:
        return True
    if left_side >= right_side:
        return True
    if parens[left_side] == "(" and parens[right_side] == ")":
        return is_nested_parens(parens, left_side + 1)
    else:
        return False

