# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        raise ValueError("Inavalid input: input must be greater than zero")
    return n * factorial(n-1)


# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    # Use Python string slicing to get the
    # first character of text and the
    # remaining characters
    first_char = text[:1]
    remaining_chars = text[1:]
    return reverse(remaining_chars) + first_char



#or 
# def reverse(text):
#     if text == "":
#         return ""
#     return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    if count == 0:
        return 0
    return bunny(count -1)+2
    
# or
# def bunny(count):
#     if not count:
#         return count
#     return bunny(count -1)+2


# is_nested_parens

def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    elif parens[0]!= "(" or parens[-1]!=")":
        return False
    else:
        return is_nested_parens(parens[1:-1])
