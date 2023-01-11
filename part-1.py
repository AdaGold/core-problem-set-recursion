# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n <= -1:
        raise ValueError
    #base case
    if n == 0:
        return 1
    return n * factorial(n - 1)


# reverse
def reverse(text):
    if len(text) == 0:
        return text
    else:
        return reverse(text[1:])+text[0]
    


# bunny
def bunny(count):
    #base case
    if count == 0:
        return 0
    if count == 1:
        return 2
    return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True
    if len(parens)%2 != 0:
        return False
    
    #finds ending paren -> ')' in parens params
    ending_parens = parens.find(')')
    #finding starting paren -> ('(') looking from right to left
    starting_parens = parens[:ending_parens].rfind('(')
    
    if starting_parens == -1:
        return False
    
    return is_nested_parens(
        parens[:starting_parens] + parens[ending_parens + 1:]
    )
    

