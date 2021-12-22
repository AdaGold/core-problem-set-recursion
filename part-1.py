# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
     # base case
    if n < 0:
        raise ValueError
    if n == 0:
          return 1
    if n > 0:
        return n * factorial(n-1)


# reverse
def reverse(text):
    # if text =="":
    #     return text
    
    # return reverse(text[::-1])
    
    if len(text) <= 0:
        return text
    return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    if count == 0:
        return 0
        
    return bunny(count-1) + 2


# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True

    if parens[0] == "(" and parens[-1] == ")":
        # return without the first and last indices 
        return is_nested_parens(parens[1:-1])
    
    return False
    
    # slicing creates a new string
    #Challenge method - without creating new strings
#   def helper(left, right):
#         if right - left <= 0:
#           return True
#         if parens[left] == "(" and parens[right] ==")":
#             return helper(left + 1, right - 1)
#         else:
#             return False
            
#   return helper(0, len(parens) - 1)

