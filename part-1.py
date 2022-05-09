# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if type(n) != int or n < 0:
        raise ValueError
    if n == 0:  # base case
        return 1
    return n * factorial(n-1) # recursive part



# reverse
def reverse(text):
    if len(text) <=1:
        return text # base case
    return text[-1] + reverse(text[0:-1])
    
# text = 'hello'
# returns:
# 1st: text[-1] + rev(text[0:-1]) ==> 'o' + rev('hell')
# 2nd: text[-1] + rev(text[0:-1]) ==> 'l' + rev('hel')
# 3rd: text[-1] + rev(text[0:-1]) ==> 'l' + rev('he')
# 4th: text[-1] + rev(text[0:-1]) ==> 'e' + rev('h') 
#5th : text                       ==> 'h'


# bunny
def bunny(count):
    if count == 0:
        return 0
    else:
        return 2 + bunny(count-1)
    


# is_nested_parens

def is_nested_parens(parens):
    if not parens:
        return True # base case
    if parens[0] == "(" and  parens[-1] == ")":
        parens = parens[1:-1]
        return is_nested_parens(parens) # recursive part
    else: 
        return False
        

