# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n ==0:
        return 1
    if n == -1:
        raise ValueError("ohmyglob!")
    return factorial(n-1)*n


# reverse
def reverse(text):
    if len(text)==1 or len(text)==0:
        return text
        
    return text [::-1]


# bunny
def bunny(count):   
    return count+count


# is_nested_parens
def is_nested_parens(parens):
    return parens[:len(parens)//2][::-1]== parens[:len(parens)//2] 