# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    elif n <= 1:
        return 1

    return n * factorial(n-1)


# reverse
def reverse(text):
    if text == "":
        return text
    else:
        return text[-1] + reverse(text[:-1])


# bunny
def bunny(count):
    if count == 0 :
        return 0
    else:
        return 2 + bunny((count-1))


# is_nested_parens

def is_nested_parens(parens):    
    beg =0
    end =len(parens)-1   

    return helper(parens, beg, end)          
    
def helper(parens, beg, end):
    if beg>end:
        return True
    dict_parens={"(":")","{":"}","[":"]"}
    return parens[beg] in dict_parens and parens[end]==dict_parens[parens[beg]] and helper(parens, beg+1, end-1)
