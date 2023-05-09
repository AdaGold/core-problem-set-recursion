# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial

def factorial(n): 
    if n < 0:
        raise ValueError
        
    if n == 0: 
        return 1
    else: 
        sum = n * factorial(n-1)
        return sum
        

# reverse

def reverse(text): 
    if len(text) == 0: 
        return text
    else: 
        reverse_text = reverse(text[1:]) + text[0]
        return reverse_text

# bunny

def bunny(count): 
    if count == 0: 
        return count
    else: 
        return bunny(count - 1) + 2

# is_nested_parens

def is_nested_parens(parens): 
    if not len(parens): 
        return True
    else: 
        if parens[0] == "(" and parens[-1] == ")": 
            parens = is_nested_parens(parens[1:-1])
            return parens
        else:
            return False
