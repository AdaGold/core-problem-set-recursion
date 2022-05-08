# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n==0:
        return 1
    if n<0:
        raise ValueError("n")
    fact=n * factorial(n-1)
    return fact


# reverse
def reverse(text):
    if len(text)<=1:
        return text
        
    first_character= text[0]  
    rest_of_string=text[1:]
    
    reversed_str=reverse(rest_of_string)
    output =reversed_str+first_character
    return output


# bunny
def bunny(count):
    if count <=0:
        return 0
        
    return 2+bunny(count-1)


# is_nested_parens

# helper function to calculate the number of "(" and ")"
def is_nested_parens_recurr(parens, opCnt, clCnt):
    if len(parens) == 0:
        return opCnt == clCnt
    
    firstCh = parens[0]

    if firstCh == '(':
        opCnt +=1
    else:
        if opCnt > clCnt:
            clCnt += 1
        else:
            return False
    
    restOfString = parens[1:]

    return is_nested_parens_recurr(restOfString, opCnt, clCnt)

def is_nested_parens(parens):
    return is_nested_parens_recurr(parens, 0, 0)


