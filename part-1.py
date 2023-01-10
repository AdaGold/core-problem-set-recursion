# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num < 0:
        raise ValueError
    if num == 0:
        return 1
    return factorial(num-1)*num


# reverse
def reverse(string):
    if len(string) == 0:
        return string
    return reverse(string[1:])+string[0]



# bunny
def bunny(bunnies):
    if bunnies==0:
        return 0
    return 2+bunny(bunnies-1)



# is_nested_parens
def compare(string, front, back):
    parens = {
        "(":")"
    }
    if front>=back:
        return True
    if parens.get(string[front])!=string[back]:
        return False
    elif front < (back+1):
        return compare(string, front+1, back-1)
        
def is_nested_parens(string):
    end = len(string) -1
    if len(string) == 0:
        return True
    return compare(string, 0, end)


