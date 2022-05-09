# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num < 0:
        raise ValueError
    if num == 0:
        return 1
    return num * factorial(num-1)


# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    remaining_chars = text[1:]
    return reverse(remaining_chars) + text[0]


# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count-1)



# is_nested_parens
def is_nested_parens(parens):
    if not len(parens):
        return True
    
    if parens[0] == "(" and parens[len(parens) -1] == ")":
        return is_nested_parens(parens[1:len(parens)-1])
    return False

