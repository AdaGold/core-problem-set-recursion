# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    # Base case
    if num == 0:
        return 1

    # Edge case - negative numbers    
    elif num < 0:
        raise ValueError

    # Recursive case    
    return num * factorial(num-1)

# reverse
def reverse(text):
    # Base case - when string is empty
    if len(text) == 0:
        return text
    
    # Recursive case --pause at func, storing text minus the first
    # letter in stack. Once func completes will add first letter to each 
    # return until returns final reverse string
    return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    # Base case
    if count == 0:
        return count

    # Recursive case    
    return 2 + bunny(count - 1)


# is_nested_parens
def is_nested_parens(parens):
    # Base case
    if len(parens) == 0:
        return True
    
    # Base case -- if odd number of characters in parens, each cannot 
    # have an opposing char 
    elif len(parens) % 2 != 0:
        return False
    
    else:
        # base case -- if we reach here, empty string in last set of parens
        # stops function
        if parens == "":
            return True

        # recursion case -- only "(" and ")" chars. If the chars don't equal
        # then return the next nested string
        if parens[0] != parens[-1]:
            return is_nested_parens(parens[1:-1])
            # returns parens from index 1 to index -1

        return False


