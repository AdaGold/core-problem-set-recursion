# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    #Function Call: factorial():
    # parameters: num (a natural number)
    # Return value: multiplication of all natural numbers up to and including num
    # Number cannot be negative to be factorial
    if n < 0:
        raise ValueError ("n cannot be negative")
    
    # Base case 
    if n == 1 or n == 0:
        return 1
    # Define this problem with a subproblem
    return n * factorial(n-1)

# reverse
def reverse(text):
    # Function Call: reverse():
    # parameters: text (a string text)
    # Return value: the same text but in reverse order by character

    # Base case
    if not text:
        return ""
    elif len(text) < 2:
        # maybe I need to say if text == None or "" return ""
        return text
    return text[-1] + reverse(text[:len(text)-1])

# bunny
def bunny(count):
    #Function Call: bunny():
    # parameters: count (number that represents a bunny with two ears)
    # Return value: total number of ears for the bunnies count given

    # Base case
    if not count:
        return 0
    elif count == 1:
        return 2
    # recursive case
    return bunny(count-1)+2

# is_nested_parens
def is_nested_parens(parens):
    #Function Call: is_nested_parens(parens):
    # parameters: parens (string parens of only parentheses)
    # Return value: rue if those parentheses are properly nested, 
    # and False if they are not 
    
    # Base case
    if len (parens) == 0:
        return True
    if len(parens) == 1:
        return False
    # Define this problem with a subproblem, recursive case
    if parens[0]=="(" and parens[-1]==")" \
    and is_nested_parens(parens[1:-1]):
        return True
    else:
        return False

