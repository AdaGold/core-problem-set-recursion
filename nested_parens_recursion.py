'''
Write a function is_nested_parens that accepts a string parens of only parentheses. 
It returns True if those parentheses are properly nested, and False if they are not. 
You may assume that no non-parenthesis characters will be passed to this function.

Example parens	Expected Output
"((()))"	True
""	True
"(())))"	False
Here are the tests:

def test_is_nested_parens():
    parens = "((()))"

    assert is_nested_parens(parens)


def test_is_nested_parens_empty_str():
    assert is_nested_parens("")


def test_is_nested_parens_not_matching_length():
    parens = "(())))"

    assert not is_nested_parens(parens)


'''

def nested_parens_recussion(parens):
    if parens == "" :
        return True
    elif parens[:1]!="(" or parens[-1:]!=")":
    # elif parens[:1] == parens[-1:]: #this logic also works
        print("odd parens here",parens)
        return False
    else:
        print(parens)
        return nested_parens_recussion(parens[1:-1])
        
print("Recursion result",nested_parens_recussion("((())))"))  



###SOLUTION#######



def is_nest_parens(parens):
    '''
    Here we looked for any '()' and then replace with an empty "", and continue to replace more until there is anothing
    
    '''
    if len(parens) == 0:
        return True
    
    elif "()" not in parens:
        return False
    
    else:
        return is_nested_parens(parens.replace("()", ""))


def is_nested_parens_advance(parens):    
    beg =0
    end =len(parens)-1   

    return helper(parens, beg, end)          
    
def helper(parens, beg, end):
    if beg>end:
        return True
    dict_parens={"(":")","{":"}","[":"]"}
    return parens[beg] in dict_parens and parens[end]==dict_parens[parens[beg]] and helper(parens, beg+1, end-1)


print("advance result",is_nested_parens_advance("((()(())))"))

parens = "((()(())))"
def is_nested_parens(parens):
    print(parens)
    if len(parens) == 0:
        return True
    elif parens[:1] != "(" or parens[-1:] != ")":
        return False
    else:
        return is_nested_parens(parens[1:-1])
    
# print(is_nested_parens(parens))

def is_nested_parens_2(parens):
    if len(parens) == 0:
        return True
    
    elif "()" not in parens:
        return False        
    return is_nested_parens(parens.replace("()", ""))

# print(is_nested_parens_2(parens))
