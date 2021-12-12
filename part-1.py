# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0: 
        raise ValueError("no negatives allowed!")
    
    if n == 0:
        return 1
    return n * factorial(n-1)



# reverse

def reverse(text):
    if text == "":
        return text
    else:
        print(text[1:])
        return reverse(text[1:]) + text[0]

# bunny
def bunny(count):
    if count == 0:
        return count 
    
    return bunny(count-1) + 2
    
    #bunny(count = 0)
    #count = 0
    #return 0
    #--------
    #bunny(count = 1)
    #count = 1
    #0 + 2
    #-------
    #bunny(count = 2)
    #count = 2
    #2 + 2
    #-------
    #bunny(count = 3)
    #count = 3
    #4 + 2
    
    #_______________________________________
    #0 bunnies => 0
    #3 bunnies => 6


# is_nested_parens

def is_nested_parens(parens):
    if parens == "":
        return True
        
    else:
        
        s1 = parens[:len(parens)//2]
        s2 = parens[len(parens)//2:]
        #print(s1,s2)
        
        for paren in s1:
            if paren != "(":
                return False
        
        for paren in s2:
            if paren != ")":
                return False
        
        return True
