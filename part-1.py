# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError("Please input number greater than zero.")
    if n == 0:
        return 1
    return n * factorial(n-1)


# reverse
def reverse(text):
    text_len = len(text)
    r_string = "" #in recursion problems, is it okay to create variables that hold values from each stack?
    if text_len >= 1:
        r_string += text[-1]
        return r_string + reverse(text[:text_len-1])
    elif text_len == 0:
        return r_string


# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens):
    parens_len = len(parens) 
    
    if parens_len > 1:
        if parens[0] == "(" and parens[parens_len-1] == ")":
            return is_nested_parens(parens[1:parens_len-1])
    elif parens_len == 0:
        return True
    else:
        return False

# this last problem was difficult for me
# i had to solve it with a for loop before 
# i could come up with the answer above

# def is_nested_parens(parens):
#   matching = None
#   parens_len = len(parens) 

#   if parens_len % 2 == 0 and len(parens) > 1:
#     for elem in range(parens_len):
#       if parens[elem] == "(" and parens[parens_len -1] == ")":
#         matching = True
#         elem += 1
#         parens_len -= 1
#   elif len(parens) == 0:
#     matching = True
#   else:
#     matching = False

#   return matching

