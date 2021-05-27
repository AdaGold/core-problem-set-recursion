# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

#1 factorial
"""
Write a function factorial 
that accepts an integer parameter n. 
It uses recursion 
to compute and 
return the value of n factorial (also written as n!).
"""
def factorial(num):
    #test if negative number
    if num<0:
        raise ValueError("Your number must be greater than 0!")
    
    # base case
    if num==0:
        return 1
    #recursive
    return num * factorial(num-1)

#2 reverse
"""
Write a function reverse 
that accepts a string text as a parameter. 

It returns the reverse of text 
by reversing all characters in the string.
"""
def reverse(text):
    #base case, Am I done?
    if len(text)<=1:
        return text
    
    #separating the input into data for the next node and data to keep
    character_string = text[1:]  #everything after 0 to the end
    first_character_string = text[0]
    
    next_node = reverse(character_string) #create next node. Waiting(memory)
    
    # turning point in recursion
    reversed_text = next_node + first_character_string 
    
    return reversed_text 
    
#3 bunny
"""
Write a function bunny 
that accepts an integer parameter count. 

count represents a number of bunnies 
and each bunny has two big floppy ears. 

We want to compute the total number of ears 
across all the bunnies recursively (without loops or multiplication).
"""
def bunny(count):
    #count = number of bunnies:2 floppy ears
    ears = 2
    
    if count == 1:
        return ears
        
    elif count == 0:
        return 0
    else:
        return ears+bunny(count-1)

#4 is_nested_parens
"""
Write a function is_nested_parens 
that accepts a string parens of only parentheses. 

It returns True 
if those parentheses are properly nested, 
and False if they are not. 

You may assume that no non-parenthesis characters 
will be passed to this function.
"""
def is_nested_parens(parens):
 
    # 1st base case, when properly nested string
    if len(parens)==0:
        return True
    
    if len(parens)==1:  #cover when just have 1 ")" left
        return False  

    right_side = parens[-1]
    left_side = parens[0]

    if left_side == "(" and right_side == ")":
        result = is_nested_parens(parens[1:-1])   #recursion
        return result
    else:
        return False    #end early
    
        

