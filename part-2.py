# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def is_nested_parens(parens):
    if parens == "":
        return True
    if parens[0] == "(" and parens[-1] == ")":
        return is_nested_parens(parens[1:-1])
    else:
        return False


# is_palindrome
# def is_palindrome(text):
#     def helper(left, right):
#         if right - left <= 0:
#             return True
#         elif text[left] == text[right]:
#             return helper(left + 1, right -1)
#         else:
#             return False 
            
#     return helper(0, len(text)-1)
    
def is_palindrome(text):
    if len(text) <= 1:
        return True
    elif text[:1] != text[-1:]:
        return False
    else:
        return is_palindrome(text[1:-1])


# digit_match
def digit_match(left, right, mathces=0):
    if left == 0 and right == 0:
        return mathces + 1
    elif left < 10 or right < 10:
        if left % 10 == right % 10:
            return mathces + 1
        else:
            return mathces
    elif left % 10 == right % 10:
        return digit_match(left // 10, right // 10, mathces + 1)
    else:
        return digit_match(left // 10, right // 10, mathces)

