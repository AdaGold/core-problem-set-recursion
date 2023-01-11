# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num < 0:
        raise ValueError()
    if num == 0:
        return 1

    return num*factorial(num-1)


# reverse
def reverse(word):
    if not word:
        return ""
    if len(word) == 1:
        return word
    
    
    return reverse(word[1:]) + word[0]


# bunny
def bunny(count):
    if count == 0:
        return 0
    if count == 1:
        return 2
    
    return 2 + bunny(count-1)
    


# is_nested_parens
def is_nested_parens(parens):
    parens_dict = {")": "("}
    
    if not parens:
        return True
    
    if len(parens) == 1:
        return False
    
    if parens[0] != parens_dict[parens[-1]]:
        return False
        
    return is_nested_parens(parens[1:-1])
