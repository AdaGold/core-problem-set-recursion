# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError("Input must be greater than 0!")
        
    if n == 0:
        return 1
        
    return factorial(n-1) * n


# reverse
def reverse(text):
    if not text or len(text) == 1:
        return text
        
    return text[-1] + reverse(text[:-1])
        


# bunny
def bunny(count):
    if not count:
        return 0
        
    return 2 + bunny(count-1)



# is_nested_parens
def is_nested_parens(parens):
    if not parens:
        return True

    if parens[0:2] == '()':
        parens = parens[2:]
    elif parens[0] == '(' and parens[-1] == ')':
        parens = parens[1:-1]
    else:
        return False
            
        
    return is_nested_parens(parens)

parens_ex1 = '((((()()()))))'
parens_ex2 = '(((()(()))))'
parens_ex3 = '((()))'
parens_ex4 = '(())))'

assert is_nested_parens(parens_ex1)
assert is_nested_parens(parens_ex2)
assert is_nested_parens(parens_ex3) 
assert is_nested_parens(parens_ex4) == False

