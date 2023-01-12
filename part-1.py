# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError("ValueError") 
        
    if n == 0:
        return 1
    
    return n*factorial(n-1) 

print(factorial(5))

# reverse
def reverse(text):
    if type(text) != str:
        raise TypeError("TypeError")
    
    if len(text) == 0:
        return text
        
    return text[-1] + reverse(text[:len(text)-1])

print(reverse("cat"))

# bunny
def bunny(count):
    if type(count) != int:
        raise TypeError("TypeError")
        
    if count < 0:
        raise ValueError("ValueError")
    
    if count == 0:
        return 0
        
    return 2 + bunny(count-1)

print(bunny(3))

# is_nested_parens
def is_nested_parens(parens, i=0, cnt=0):
    if type(parens) != str:
        raise TypeError("TypeError")

    if parens == "":
        return ""
    
    if len(parens) == 0:
        return True
    elif parens[:1] != "(" or parens[-1:] != ")":
        return False
    else:
        return is_nested_parens(parens[1:-1])
    
    #other ---
    #def is_nested_parens(parens, i=0, cnt=0)
        # if i == len(parens): return cnt==0
        # if cnt<0:return False
        # if parens[i] == "(": return is_nested_parens(parens, i+1, cnt+1)
        # elif parens[i] == ")": return is_nested_parens(parens, i+1, cnt-1)
        # return is_nested_parens(parens, i+1, cnt)

print(is_nested_parens("(())"))

