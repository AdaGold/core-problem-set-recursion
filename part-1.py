# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError('given number should be greater than zero')
    if n == 0:
        return 1
        
    return n * factorial(n-1)    



# reverse
def reverse(text):
    if len(text) == 0:
        return text
        
    first_letter = text[:1]
    letter_left = text[1:]
    



# bunny
def bunny(count):
    if count == 0:
        return count
    return 2 + bunny(count-1)  



# is_nested_parens

def is_nested_parens(parens):
    if len(parens) == 0:
        return True
        
    elif "()" not in parens:
        return False
        
    return is_nested_parens(parens.replace("()",""))        


