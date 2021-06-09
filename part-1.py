# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial

def factorial(n):

    if n < 0:
        raise ValueError
        
    if n < 2:
        return 1
    
    else:
        return n * factorial(n - 1)



# reverse

def reverse(text):

    rev = "".join(reversed(text))
    
    return rev


# bunny

# def bunny(count):
#     return count * 2

def bunny(count):
    if not count:
        return count
    else:
        return 2 + bunny(count-1)

# is_nested_parens

# def is_nested_parens(parens):
    
#     count = 0
    
#     for i in parens:
#         if i == ")":
#             if count <= 0:
#                 return False
                
#             count -= 1
#         elif i == "(":
#             count += 1
    
#     return count == 0

def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    elif parens[:1] != "(" or parens[-1:] != ")":
        return False
    else:
        return is_nested_parens(parens[1:-1])


