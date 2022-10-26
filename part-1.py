# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
"""Write a function factorial that accepts an integer parameter n. It uses recursion to compute and return the value of n factorial (also written as n!)."""
def factorial(n):
    if n < 0:
        raise ValueError
    #base case
    if n == 1 or n== 0:
        return 1
    #recursive case
    return n * factorial(n-1)
    
    #oneline solution
    #return 1 if (n==1 or n==0) else n * factorial(n - 1);


# reverse
"""Write a function reverse that accepts a string text as a parameter. It returns the reverse of text by reversing all characters in the string."""
def reverse(text):
    if len(text) == 0:
        return text
    
    else:
        #print(text[1:], text[:1])
        return reverse(text[1:]) + text[0]
        #or return reverse(text[1:]) + text[:1]
    
    #non recursive solution
    #reverse(text[::-1])


# bunny
def bunny(count):
    """
    Write a function bunny that accepts an integer parameter count. 
    count represents a number of bunnies and each bunny has two big floppy ears. 
    We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).
    """
    #base case
    if count <= 1:
        return count * 2
    #recursive case
    return 2 + bunny(count-1)


# is_nested_parens
#compare consequence elements and slice it
def is_nested_parens_1(parens):
    """
    Write a function is_nested_parens that accepts a string parens of only parentheses. 
    It returns True if those parentheses are properly nested, and False if they are not. 
    You may assume that no non-parenthesis characters will be passed to this function.
    """
    #base case
    if parens == "":
        return True
    
    #recursive call
    for i in range(len(parens)):
        if parens[i] == '(':
            if i + 1 < len(parens):
                if parens[i+1] == ')':
                    return is_nested_parens(parens[:i] + parens[i+2:])
    
    return False    
    
    
#Learn solution: compare first and last element and slice it
def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    elif parens[:1] != "(" or parens[-1:] != ")":
        return False
    else:
        return is_nested_parens(parens[1:-1])

