# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n == 0:
        return 1
        
    if(n < 0):
        raise ValueError("Num must be greater than 0")
    
    return n * factorial(n -1)


# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    
    first_char = text[0] 
    rest = text[1: len(text)]
    # More Pythonic way to write above lines for string indexing/slicing
    # first_char = text[:1]
    # remaining_chars = text[1:]
    
    return reverse(rest) + first_char


# bunny
def bunny(count):
    if count == 0:
        return 0
    
    if count == 1: 
        return 2
    
    bunny1 = 2
    remain_bunnies = count - 1
    
    return bunny(remain_bunnies) + bunny1



# is_nested_parens

def is_nested_parens(parens):
    print(parens)
    if parens == "":
        return True
    
    if parens[0] == '(' and parens[-1] == ')':
        rest = parens[1: -1]
        return is_nested_parens(rest)
    
    else:
        return False
